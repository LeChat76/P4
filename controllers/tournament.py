import os
from datetime import datetime
from views.tournament import TournamentView
from views.player import PlayerView
from models.tournament import TournamentModel
from models.player import PlayerModel
from models.match import MatchModel
from constantes import MENU_TOURNAMENT_CREATION, MENU_TOURNAMENT_DISPLAY,\
    MENU_TOURNAMENT_START, MENU_TOURNAMENT_RECOVERY, MENU_TOURNAMENT_EXIT,\
    NB_JOUEURS_BY_MATCH


class TournamentController:
    """ Tournament controller class """
    def __init__(self):
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.tournament_model = TournamentModel()
        self.player_model = PlayerModel()
        self.match_model = MatchModel()

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
        new_tournament = self.tournament_view.add_tournament_menu()
        for tournament in new_tournament:
            tournament_to_add = TournamentModel(tournament[0], tournament[1],
                                                tournament[2], tournament[3])
            tournament_to_add.add_tournament()

    def display_tournament(self):
        """ method to display tournaments completed, current or all """
        while True:
            tournament_to_display = self.tournament_view.display_tournament()
            if tournament_to_display == "display_all_tournaments":
                result = self.tournament_model.search_all_tournaments()
                if result == "no_result":
                    self.tournament_view.choice_menu("Aucun tournoi à"
                                                     " afficher. Appuyez sur"
                                                     " [ENTRER] pour revenir"
                                                     " au menu.")
                    break
                else:
                    if (len(result)) == 1:
                        print(str(len(result)) + " résultat.")
                    elif (len(result)) > 1:
                        print(str(len(result)) + " résultats.")
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'],
                                              item['nb_round']))
                    choix = self.tournament_view.choice_menu("Faire une autre"
                                                             " recherche"
                                                             " (O/n)? ")
                    if choix == "N":
                        break

            elif tournament_to_display == "display_completed_tournaments":
                result = self.tournament_model.search_completed_tournaments()
                if result == "no_result":
                    choix = self.tournament_view.choice_menu("Aucun tournoi à"
                                                             " afficher."
                                                             " Recommencer"
                                                             " (O/n)? ")
                    if choix == "N":
                        break
                else:
                    if (len(result)) == 1:
                        print(str(len(result)) + " résultat.")
                    elif (len(result)) > 1:
                        print(str(len(result)) + " résultats.")
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'],
                                              item['nb_round']))
                    choix = self.tournament_view.choice_menu("Faire une autre"
                                                             " recherche"
                                                             " (O/n)? ")
                    if choix == "N":
                        break

            elif tournament_to_display == "display_current_tournaments":
                result = self.tournament_model.search_current_tournaments()
                if result == "no_result":
                    choix = self.tournament_view.choice_menu("Aucun tournoi à"
                                                             " afficher."
                                                             " Recommencer"
                                                             " (O/n)? ")
                    if choix == "N":
                        break
                else:
                    if (len(result)) == 1:
                        print(str(len(result)) + " résultat.")
                    elif (len(result)) > 1:
                        print(str(len(result)) + " résultats.")
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'],
                                              item['nb_round']))
                    choix = self.tournament_view.choice_menu("Faire une autre"
                                                             " recherche"
                                                             " (O/n)? ")
                    if choix == "N":
                        break

            elif tournament_to_display == "display_not_started_tournaments":
                result = self.tournament_model.search_not_started_tournaments()
                if result == "no_result":
                    choix = self.tournament_view.choice_menu("Aucun tournoi à"
                                                             " afficher."
                                                             " Recommencer"
                                                             " (O/n)? ")
                    if choix == "N":
                        break
                else:
                    if (len(result)) == 1:
                        print(str(len(result)) + " résultat.")
                    elif (len(result)) > 1:
                        print(str(len(result)) + " résultats.")
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'],
                                              item['nb_round']))
                    choix = self.tournament_view.choice_menu("Faire une autre"
                                                             " recherche"
                                                             " (O/n)? ")
                    if choix == "N":
                        break

    def begin_new_tournament(self):
        """ request for needed information (which tournament and players to
         associate) to begin new tournament """
        players_available_list = []
        players_uuid_list = []
        match = None
        while True:
            players_available = self.player_model.search_all_players()
            if players_available == "no_result" or len(players_available) <= 1:
                self.tournament_view.choice_menu("Liste des joueurs vide."
                                                 " Merci d'en créer au moins"
                                                 " deux.\ndisponibles pour"
                                                 " démarrer un tournoi"
                                                 " [ENTRER] pour revenir au"
                                                 " menu.")
                break
            """ create list of players (uuid) """
            for i in range(len(players_available)):
                item = players_available[i]
                players_available_list.append(item['player_uuid'])

            """ create list of available tournaments (tournament not already
             started) """
            not_started_tournament =\
                self.tournament_model.search_not_started_tournaments()
            if not_started_tournament == "no_result":
                self.tournament_view.choice_menu("Aucun tournoi disponible."
                                                 " Vous devez en créer un"
                                                 " nouveau. [ENTRER] pour"
                                                 " continuer.")
                break

            """ displayer list of available tournaments """
            print("Liste des tournois non démarrés:")
            for i in range(len(not_started_tournament)):
                item = not_started_tournament[i]
                print(str(i + 1) + " - " +
                      str(TournamentModel(item['name'],
                                          item['town'],
                                          item['nb_round'])))

            """ choose tournament """
            result = self.tournament_view.select_menu(not_started_tournament)
            selected_tournament = not_started_tournament[int(result) - 1]
            selected_tournament_uuid = selected_tournament['tournament_uuid']

            tournament_nb_round = self.tournament_model.\
                search_nb_round_for_tournament(selected_tournament_uuid)
            """ compare nb rounds and nb players available to check if some
            players will play with the same players twice - formula is nb
            round should not be superior of nb players available - 1
            example : if there is 8 players, nb match = 7 so nb round max
            should be equal or inferior to 7 """
            if int(tournament_nb_round) > (int(len(players_available)) - 1):
                print("Ce tournoi comporte "
                      + str(tournament_nb_round)
                      + " round(s) donc pas assez de joueurs disponibles"
                        " pour éviter que certains ne se rencontrent deux"
                        " fois.")

            """ Selection of players to add to the selected tournament """
            nb_players = 0
            nb_players_available = len(players_available_list)

            """ check if nb players available is pair because in case of
             nb players selected is odd, sometime a player will not play
             so it's mandatory to select only pair numbers of players """
            if nb_players_available % 2 != 0:
                nb_players_available_pair = False
            else:
                nb_players_available_pair = True
            while True:
                print(str(nb_players_available) + " joueurs disponibles:")
                for i in range(len(players_available_list)):
                    player_uuid = players_available_list[i]
                    player =\
                        self.player_model.extract_player_fname_and_name(
                            player_uuid)
                    print(str(i + 1) + " - " + player + ".")
                print(str(nb_players) + " sélectionné(s).")
                result = self.player_view.select_available_players_menu(
                    len(players_available_list), nb_players)
                if result == "end_players_selection":
                    break
                selected_player_uuid = (players_available_list[int(result)
                                                               - 1])
                players_uuid_list.append(selected_player_uuid)
                nb_players_available -= 1
                nb_players += 1
                players_available_list.remove(selected_player_uuid)
                if nb_players_available == 1 and nb_players_available_pair\
                        is False:
                    print("Il ne reste plus qu'une personne, impossible de"
                          " former une paire.\n"
                          "Fin de la selection.")
                    break
                elif nb_players_available == 0 or nb_players_available_pair ==\
                        "True":
                    print("Plus de personne à ajouter.")
                    break

            self.tournament_model.store_players_uuids(selected_tournament_uuid,
                                                      players_uuid_list)
            print('Tournoi "' + selected_tournament['name'] + '" prêt.')
            if (nb_players - 1) < int(tournament_nb_round):
                print("Pour information : vu le faible nombre de joueurs"
                      " sélectionnés et le grand nombre de rounds,"
                      " certains joueurs se rencontreront deux fois.")
            elif (nb_players - 1) > int(tournament_nb_round):
                print("Pour information : vu le faible nombre de rounds du"
                      " tournoi et la quantité de joueurs"
                      " sélectionnés, certains joueurs ne se rencontreront"
                      " pas.")

            self.tournament_view.choice_menu("Appuyez sur une [ENTRER] pour"
                                             " continuer.")

            """ beginning of the tournament """
            current_round = 1
            date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
            self.tournament_model.\
                store_tournament_start_date(selected_tournament_uuid, date)
            nb_round = self.tournament_model.search_nb_round_for_tournament(
                selected_tournament_uuid)
            nb_match = int(len(players_uuid_list) / NB_JOUEURS_BY_MATCH)

            for j in range(int(nb_round)):
                """ loop for all rounds """
                round_start_date = \
                    (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                players_list =\
                    self.player_model.create_player_list(players_uuid_list)
                matchs_list = self.tournament_model\
                    .extract_matchs_uuid_list_of_tournament(
                     selected_tournament_uuid)
                previous_matchs_players_list = self.match_model\
                    .create_matchs_players_list(matchs_list)
                players_list = self.player_model\
                    .check_players_list(players_list,
                                        previous_matchs_players_list)
                if players_list[1]:
                    print("/!\\ Certains joueurs de ce round ont déjà joués "
                          "ensemble /!\\")
                players_list = players_list[0]

                current_match = 1
                for i in range(0, nb_match * 2, 2):
                    """ loop for all matches for one round"""
                    player_one_uuid = players_list[i]
                    player_two_uuid = players_list[i + 1]
                    player_one = self.player_model.\
                        extract_player_fname_and_name(player_one_uuid)
                    player_two = self.player_model.\
                        extract_player_fname_and_name(player_two_uuid)
                    print("Tour : " + str(current_round) + "/" + str(nb_round)
                          + ", match " + str(current_match)
                          + "/" + str(nb_match) + " opposant " + player_one
                          + " à " + player_two + ".")
                    scores = self.player_view.record_score(player_one,
                                                           player_two)
                    match = MatchModel(selected_tournament_uuid, current_round,
                                       current_match, player_one_uuid,
                                       player_two_uuid, scores[0], scores[1])
                    match.create_tuple_for_match()
                    current_match += 1

                self.tournament_model.store_current_round(
                    selected_tournament_uuid, current_round)
                round_end_date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                self.tournament_model.store_round_date(
                    selected_tournament_uuid, current_round, round_start_date,
                    round_end_date)
                current_round += 1
                if int(nb_round) >= current_round:
                    choix = self.tournament_view.choice_menu(
                        "Continuer l'enregistrement des scores (O/n) ?")
                    if choix == "N":
                        match_id_list = match.store_match()
                        self.tournament_model.store_match_id(
                            selected_tournament_uuid,
                            match_id_list)
                        break
                else:
                    date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                    self.tournament_model.store_tournament_end_date(
                        selected_tournament_uuid, date)
                match_id_list = match.store_match()
                self.tournament_model.store_match_id(selected_tournament_uuid,
                                                     match_id_list)
            self.tournament_view.choice_menu("Fin du tour. Appuyez sur"
                                             " [ENTRER] pour revenir au menu.")
            break

    def resume_tournament(self):
        """ method to resume a not ended tournament """
        match = None
        not_ended_tournament = self.tournament_model.\
            search_current_tournaments()
        if not_ended_tournament == "no_result":
            self.tournament_view.choice_menu("Aucun tournoi(s) non terminé(s)."
                                             "Appuyez sur [ENTRER]"
                                             " pour continuer.")
        else:
            """ displayer list of not ended tournaments """
            print("Liste des tournois non démarrés:")
            for i in range(len(not_ended_tournament)):
                item = not_ended_tournament[i]
                print(str(i + 1) + " - " +
                      str(TournamentModel(item['name'],
                                          item['town'],
                                          item['nb_round'])))

            """ choose tournament """
            result = self.tournament_view.select_menu(not_ended_tournament)
            selected_tournament = not_ended_tournament[int(result) - 1]
            tournament_uuid = selected_tournament['tournament_uuid']
            tournament_info = self.tournament_model.\
                extract_all_infos_tournaments(tournament_uuid)
            players_uuid_list = tournament_info[7]
            nb_round = int(tournament_info[4])
            current_round = int(tournament_info[5]) + 1
            print(f"Ce tournoi comporte {len(players_uuid_list)} joueurs :")
            for player_uuid in players_uuid_list:
                print(" - " + self.player_model.extract_player_fname_and_name(
                    player_uuid))
            print(f"Le prochain round est le"
                  f" {current_round} ème.")

            """ resume the tournament """
            nb_match = int(len(players_uuid_list) / NB_JOUEURS_BY_MATCH)

            for j in range(current_round - 1, nb_round):
                """ loop for all rounds """
                round_start_date = \
                    (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                """ extract matches ids from a tournament """
                matchs_list = self.tournament_model \
                    .extract_matchs_uuid_list_of_tournament(tournament_uuid)
                """ create players list from previous matches """
                previous_matchs_players_list = self.match_model \
                    .create_matchs_players_list(matchs_list)
                """ extract previous scores from matches """
                previous_scores = \
                    self.match_model.extract_previous_scores(players_uuid_list,
                                                             matchs_list)
                """ store scores in players.json file """
                self.player_model.\
                    store_score_from_previous_match(players_uuid_list,
                                                    previous_scores)
                """ create players list sorted by scores """
                players_list =\
                    self.player_model.create_player_list(players_uuid_list)
                """ check players list to avoid players
                 already played together (if possible) """
                players_list = self.player_model\
                    .check_players_list(players_list,
                                        previous_matchs_players_list)
                if players_list[1]:
                    print("/!\\ Certains joueurs de ce round ont déjà joués "
                          "ensemble /!\\")
                players_list = players_list[0]

                current_match = 1
                for i in range(0, nb_match * 2, 2):
                    """ loop for all matches for one round"""
                    player_one_uuid = players_list[i]
                    player_two_uuid = players_list[i + 1]
                    player_one = self.player_model.\
                        extract_player_fname_and_name(player_one_uuid)
                    player_two = self.player_model.\
                        extract_player_fname_and_name(player_two_uuid)
                    print("Tour : " + str(current_round) + "/" + str(nb_round)
                          + ", match " + str(current_match)
                          + "/" + str(nb_match) + " opposant " + player_one
                          + " à " + player_two + ".")
                    scores = self.player_view.record_score(player_one,
                                                           player_two)
                    """ TROUVER LE MOYEN D'AJOUTER ANCIENS MATCHS """
                    match = MatchModel(tournament_uuid, current_round,
                                       current_match, player_one_uuid,
                                       player_two_uuid, scores[0], scores[1])
                    match.create_tuple_for_match()
                    current_match += 1

                self.tournament_model.store_current_round(tournament_uuid,
                                                          current_round)
                round_end_date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                self.tournament_model.store_round_date(tournament_uuid,
                                                       current_round,
                                                       round_start_date,
                                                       round_end_date)
                current_round += 1
                if int(nb_round) >= current_round:
                    choix = self.tournament_view.choice_menu(
                        "Continuer l'enregistrement des scores (O/n) ?")
                    if choix == "N":
                        match_id_list = match.store_match()
                        self.tournament_model.store_match_id(tournament_uuid,
                                                             match_id_list)
                        break
                else:
                    date = (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
                    self.tournament_model.store_tournament_end_date(
                        tournament_uuid, date)
                match_id_list = match.store_match()
                self.tournament_model.store_match_id(tournament_uuid,
                                                     match_id_list)
            self.tournament_view.choice_menu("Fin du tour. Appuyez sur"
                                             " [ENTRER] pour revenir au menu.")
