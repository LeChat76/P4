import sys
from datetime import datetime
from views.tournament import TournamentView
from views.player import PlayerView
from models.tournament import TournamentModel
from models.player import PlayerModel
from models.match import MatchModel
from constantes import MENU_TOURNAMENT_CREATION, MENU_TOURNAMENT_DISPLAY, MENU_TOURNAMENT_START,\
    MENU_TOURNAMENT_RECOVERY, MENU_TOURNAMENT_EXIT, NB_JOUEURS_BY_MATCH


class TournamentController:
    """ Tournament controller class """
    def __init__(self):
        self.text = None
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()

    def menu_tournament(self):
        """ Tournament Menu """
        while True:
            choix = self.tournament_view.tournament_menu()
            if choix == MENU_TOURNAMENT_CREATION:
                self.add_tournament()
            elif choix == MENU_TOURNAMENT_DISPLAY:
                self.display_tournament()
            elif choix == MENU_TOURNAMENT_START:
                self.begin_new_tournament()
            elif choix == MENU_TOURNAMENT_RECOVERY:
                self.resume_tournament()
            elif choix == MENU_TOURNAMENT_EXIT:
                break

    def add_tournament(self):
        """ method to record new tournaments """
        new_tournament = self.tournament_view.add_tournament()
        for tournament in new_tournament:
            tournament_to_add = TournamentModel(tournament_name=tournament[0], tournament_town=tournament[1],
                                                tournament_nb_round=tournament[2],
                                                tournament_description=tournament[3])
            tournament_to_add.save_tournament()

    def display_tournament(self):
        """ method to display tournaments completed, current or all """
        while True:
            tournament_to_display = self.tournament_view.display_tournament()
            if tournament_to_display == "display_all_tournaments":
                result = TournamentModel.search_all_tournaments()
                if result == "no_result":
                    self.tournament_view.choice("Aucun tournoi à afficher. Appuyez sur [ENTRER] pour revenir au menu.")
                    break
                elif result == "error":
                    self.tournament_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                                       " le et recommencez.")
                    sys.exit()
                else:
                    self.tournament_view.text_to_print(str(len(result)) + " résultat(s).")
                    for tournament in result:
                        self.tournament_view.text_to_print(tournament)
                    choix = self.tournament_view.choice("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break
            elif tournament_to_display == "display_completed_tournaments":
                result = TournamentModel.search_completed_tournaments()
                if result == "no_result":
                    choix = self.tournament_view.choice("Aucun tournoi à afficher. Recommencer (O/n)? ")
                    if choix == "N":
                        break
                elif result == "error":
                    self.tournament_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                                       " le et recommencez.")
                    sys.exit()
                else:
                    self.tournament_view.text_to_print(str(len(result)) + " résultat(s).")
                    for tournament in result:
                        self.tournament_view.text_to_print(tournament)
                    choix = self.tournament_view.choice("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

            elif tournament_to_display == "display_current_tournaments":
                result = TournamentModel.search_current_tournaments()
                if result == "no_result":
                    choix = self.tournament_view.choice("Aucun tournoi à afficher. Recommencer (O/n)? ")
                    if choix == "N":
                        break
                elif result == "error":
                    self.tournament_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                                       " le et recommencez.")
                    sys.exit()
                else:
                    self.tournament_view.text_to_print(str(len(result)) + " résultat(s).")
                    for tournament in result:
                        self.tournament_view.text_to_print(tournament)
                    choix = self.tournament_view.choice("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

            elif tournament_to_display == "display_not_started_tournaments":
                result = TournamentModel.search_not_started_tournaments()
                if result == "no_result":
                    choix = self.tournament_view.choice("Aucun tournoi à afficher. Recommencer (O/n)? ")
                    if choix == "N":
                        break
                elif result == "error":
                    self.tournament_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                                       " le et recommencez.")
                    sys.exit()
                else:
                    self.tournament_view.text_to_print(str(len(result)) + " résultat(s).")
                    for tournament in result:
                        self.tournament_view.text_to_print(tournament)
                    choix = self.tournament_view.choice("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

    def begin_new_tournament(self):
        """ request for needed information (which tournament and players to associate) to begin new tournament """
        players_available_list = []
        match = None
        while True:
            players_available = PlayerModel.search_all_players()
            if players_available == "error":
                self.tournament_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                                   " le et recommencez.")
                sys.exit()
            if players_available == "no_result" or len(players_available) <= 1:
                self.tournament_view.choice("Liste des joueurs vide. Merci d'en créer au moins deux\ndisponibles"
                                            " pour démarrer un tournoi [ENTRER] pour revenir au menu.")
                break
            # create list of players (uuid)
            for player in players_available:
                players_available_list.append(player)

            # create list of available tournaments (tournament not already started)
            not_started_tournament = TournamentModel.search_not_started_tournaments()
            if not_started_tournament == "no_result":
                self.tournament_view.choice("Aucun tournoi disponible. Vous devez en créer un nouveau. [ENTRER]"
                                            " pour continuer.")
                break
            elif not_started_tournament == "error":
                self.tournament_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                                   " le et recommencez.")
                sys.exit()

            # displayer list of available tournaments
            self.tournament_view.text_to_print("Liste des tournois non démarrés:")
            index = 0
            for tournament in not_started_tournament:
                index += 1
                self.tournament_view.text_to_print(str(index) + " - " + str(tournament))

            # choose tournament
            result = self.tournament_view.select(not_started_tournament)
            tournament = not_started_tournament[int(result) - 1]

            tournament_nb_round = tournament.search_nb_round_for_tournament()
            # compare nb rounds and nb players available to check if some players will play with the same
            # players twice - formula is nb# round should not be superior of nb players available - 1
            # example : if there is 8 players, nb match = 7 so nb round max should be equal or inferior to 7
            if tournament_nb_round == "error":
                self.tournament_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                                   " le et recommencez.")
                sys.exit()
            elif int(tournament_nb_round) > (int(len(players_available)) - 1):
                self.tournament_view.text_to_print("Ce tournoi comporte " + str(tournament_nb_round)
                                                   + " round(s) donc pas assez de joueurs disponibles"
                                                   " pour éviter que certains ne se rencontrent plusieurs fois.")
            # Selection of players to add to the selected tournament
            nb_players = 0
            nb_players_available = len(players_available_list)

            # check if nb players available is pair because in case of nb players selected is odd,
            # sometime a player will not play so it s mandatory to select only pair numbers of players
            if nb_players_available % 2 != 0:
                nb_players_available_pair = False
            else:
                nb_players_available_pair = True
            players_list = []
            while True:
                self.tournament_view.clear_screen()
                self.tournament_view.text_to_print(str(nb_players_available) + " joueurs disponibles:")
                index = 0
                for player in players_available_list:
                    index += 1
                    player_fname_name = player.extract_player_fname_and_name()
                    self.tournament_view.text_to_print(str(index) + " - " + player_fname_name + ".")
                self.tournament_view.text_to_print(str(nb_players) + " sélectionné(s).")
                result = self.player_view.select_available_players(len(players_available_list), nb_players)
                if result == "end_players_selection":
                    break
                selected_player = (players_available_list[int(result) - 1])
                players_list.append(selected_player)
                nb_players_available -= 1
                nb_players += 1
                players_available_list.remove(selected_player)
                if nb_players_available == 1 and nb_players_available_pair is False:
                    self.tournament_view.text_to_print("Il ne reste plus qu'une personne, impossible de former une"
                                                       " pair.\nFin de la selection.")
                    break
                elif nb_players_available == 0 or nb_players_available_pair == "True":
                    self.tournament_view.text_to_print("Plus de personne à ajouter.")
                    break

            tournament.store_players(PlayerModel.extract_player_uuid_list(players_list))
            self.tournament_view.text_to_print('Tournoi "' + tournament.tournament_name + '" prêt.')
            if (nb_players - 1) < int(tournament_nb_round):
                self.tournament_view.text_to_print("Pour information : vu le faible nombre de joueurs sélectionnés"
                                                   " et le grand nombre de rounds, certains joueurs se rencontreront"
                                                   " plusieurs fois.")
            elif (nb_players - 1) > int(tournament_nb_round):
                self.tournament_view.text_to_print("Pour information : vu le faible nombre de rounds du tournoi et la"
                                                   " quantité de joueurs sélectionnés, certains joueurs ne se"
                                                   " rencontreront pas.")

            self.tournament_view.choice("Appuyez sur une [ENTRER] pour continuer.")
            self.tournament_view.clear_screen()

            # beginning of the tournament
            PlayerModel.delete_score_player_object(players_list)
            current_round = 1
            date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
            tournament.store_tournament_start_date(date)
            nb_round = tournament.search_nb_round_for_tournament()

            nb_match = int(len(players_list) / NB_JOUEURS_BY_MATCH)

            for j in range(int(nb_round)):
                # loop for all rounds
                round_start_date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                players_list = PlayerModel.sort_player_list(players_list)
                matchs_list = TournamentModel.extract_matchs_uuid_list_of_tournament(tournament)
                previous_matchs_players_list = MatchModel.create_matchs_players_list(matchs_list)
                PlayerModel.update_score_in_player_object(players_list)
                players_list = PlayerModel.check_players_list(players_list, previous_matchs_players_list)
                if players_list[1]:
                    self.tournament_view.text_to_print(
                        "/!\\ Certains joueurs de ce round ont déjà joués ensemble /!\\")
                players_list = players_list[0]

                current_match = 1
                for i in range(0, nb_match * 2, 2):
                    # loop for all matches for one round
                    p1 = players_list[i]
                    p2 = players_list[i + 1]
                    player_one = p1.extract_player_fname_and_name()
                    player_two = p2.extract_player_fname_and_name()
                    self.tournament_view.text_to_print("Tour : " + str(current_round) + "/" + str(nb_round)
                                                       + ", match " + str(current_match) + "/" + str(nb_match)
                                                       + " opposant " + player_one + " à " + player_two + ".")
                    scores = self.player_view.record_score(player_one, player_two)
                    match = MatchModel(tournament.tournament_uuid, current_round, current_match, p1.player_uuid,
                                       p2.player_uuid, scores[0], scores[1])
                    match.create_tuple_for_match()
                    current_match += 1

                tournament.store_current_round(current_round)
                round_end_date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                tournament.store_round_date(current_round, round_start_date, round_end_date)
                current_round += 1
                if int(nb_round) >= current_round:
                    choix = self.tournament_view.choice("Continuer l'enregistrement des scores (O/n) ?")
                    if choix == "N":
                        match_id_list = match.store_match()
                        tournament.store_match_id(match_id_list)
                        break
                else:
                    date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                    tournament.store_tournament_end_date(date)
                match_id_list = match.store_match()
                tournament.store_match_id(match_id_list)
            self.tournament_view.choice("Fin du tour. Appuyez sur [ENTRER] pour revenir au menu.")
            break

    def resume_tournament(self):
        """ method to resume a not ended tournament """
        match = None
        not_ended_tournament = TournamentModel.search_current_tournaments()
        if not_ended_tournament == "no_result":
            self.tournament_view.choice("Aucun tournoi(s) non terminé(s). Appuyez sur [ENTRER] pour continuer.")
        elif not_ended_tournament == "error":
            self.tournament_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                               " le et recommencez.")
            sys.exit()
        else:
            # displayer list of not ended tournaments
            self.tournament_view.text_to_print("Liste des tournois non démarrés:")
            index = 0
            for tournament in not_ended_tournament:
                index += 1
                self.tournament_view.text_to_print(str(index) + " - " + str(tournament))

            # choose tournament
            result = self.tournament_view.select(not_ended_tournament)
            tournament = not_ended_tournament[int(result) - 1]
            players_uuid_list = tournament.tournament_list_players
            nb_round = tournament.tournament_nb_round
            current_round = int(tournament.tournament_current_round) + 1
            self.tournament_view.text_to_print(f"Ce tournoi comporte {len(players_uuid_list)} joueurs :")
            players = []
            for player_uuid in players_uuid_list:
                player = PlayerModel.create_player_object(player_uuid)
                players.append(player)
                self.tournament_view.text_to_print(" - " + str(player))
            self.tournament_view.text_to_print(f"Le prochain round est le {current_round} ème.")

            # resume the tournament
            nb_match = int(len(players_uuid_list) / NB_JOUEURS_BY_MATCH)

            for j in range(current_round - 1, nb_round):
                # loop for all rounds
                round_start_date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                # extract matches ids from a tournament
                matchs_list = TournamentModel.extract_matchs_uuid_list_of_tournament(tournament)
                # create players list from previous matches
                previous_matchs_players_list = MatchModel.create_matchs_players_list(matchs_list)
                # extract previous scores from matches
                previous_scores = MatchModel.extract_previous_scores(players_uuid_list, matchs_list)
                # store scores in players.json file
                PlayerModel.store_score_from_previous_match(players_uuid_list, previous_scores)
                # create players list sorted by scores
                players_list = PlayerModel.sort_player_list(players)
                # check players list to avoid players already played together (if possible)
                players_list = PlayerModel.check_players_list(players_list, previous_matchs_players_list)
                if players_list[1]:
                    self.tournament_view.text_to_print(
                        "/!\\ Certains joueurs de ce round ont déjà joués ensemble /!\\")
                players_list = players_list[0]

                current_match = 1
                for i in range(0, nb_match * 2, 2):
                    # loop for all matches for one round
                    player_one = players_list[i].extract_player_fname_and_name()
                    player_two = players_list[i + 1].extract_player_fname_and_name()
                    player_one_uuid = players_list[i].extract_player_uuid()
                    player_two_uuid = players_list[i + 1].extract_player_uuid()
                    self.tournament_view.text_to_print("Tour : " + str(current_round) + "/" + str(nb_round)
                                                       + ", match " + str(current_match) + "/" + str(nb_match)
                                                       + " opposant " + player_one + " à " + player_two + ".")
                    scores = self.player_view.record_score(player_one, player_two)
                    match = MatchModel(tournament.tournament_uuid, current_round, current_match, player_one_uuid,
                                       player_two_uuid, scores[0], scores[1])
                    match.create_tuple_for_match()
                    current_match += 1

                tournament.store_current_round(current_round)
                round_end_date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                tournament.store_round_date(current_round, round_start_date, round_end_date)
                current_round += 1
                if int(nb_round) >= current_round:
                    choix = self.tournament_view.choice("Continuer l'enregistrement des scores (O/n) ?")
                    if choix == "N":
                        match_id_list = match.store_match()
                        tournament.store_match_id(match_id_list)
                        break
                else:
                    date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                    tournament.store_tournament_end_date(date)
                match_id_list = match.store_match()
                tournament.store_match_id(match_id_list)
            self.tournament_view.choice("Fin du tour. Appuyez sur [ENTRER] pour revenir au menu.")

    def text_to_print(self, text):
        """ method to print a text with method text_to_print in view model """
        TournamentView.text_to_print(text)
