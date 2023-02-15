from datetime import datetime
from views.start_menu import MainMenu
from views.tournament import TournamentView
from views.player import PlayerView
from models.tournament import TournamentModel
from models.player import PlayerModel
from models.match import MatchModel

MAINMENU = MainMenu()
TOURNAMENT_VIEW = TournamentView()
TOURNAMENT_MODEL = TournamentModel()
PLAYER_VIEW = PlayerView()
PLAYER_MODEL = PlayerModel()
MATCH_MODEL = MatchModel()
MENU_TOURNAMENT_CREATION = 1
MENU_TOURNAMENT_DISPLAY = 2
MENU_TOURNAMENT_START = 3
MENU_TOURNAMENT_RECOVERY = 4
MENU_TOURNAMENT_EXIT = 5


class TournamentController:

    def menu_2(self):
        """ Tournament Menu """
        while True:
            choix = TOURNAMENT_VIEW.tournament_menu()
            if choix == MENU_TOURNAMENT_CREATION:
                self.add_tournament()
            elif choix == MENU_TOURNAMENT_DISPLAY:
                self.display_tournament()
            elif choix == MENU_TOURNAMENT_START:
                self.begin_new_tournament()
            # elif choix == MENU_TOURNAMENT_RECOVERY:
            #     self.recover_tournament()
            elif choix == MENU_TOURNAMENT_EXIT:
                break

    @staticmethod
    def add_tournament():
        """ method to record new tournaments """
        new_tournament = TOURNAMENT_VIEW.add_tournament_menu()
        for tournament in new_tournament:
            tournament_to_add = TournamentModel(tournament[0], tournament[1], tournament[2], tournament[3])
            tournament_to_add.add_tournament()

    @staticmethod
    def display_tournament():
        """ method to display tournaments completed, current or all """
        while True:
            tournament_to_display = TOURNAMENT_VIEW.display_tournament()
            if tournament_to_display == "display_all_tournaments":
                result = TOURNAMENT_MODEL.search_all_tournaments()
                if result == "no_result":
                    TOURNAMENT_VIEW.choice_menu("Aucun tournoi à afficher. Appuyez sur [ENTRER] pour revenir"
                                                        " au menu.")
                    break
                else:
                    if (len(result)) == 1:
                        print(str(len(result)) + " résultat.")
                    elif (len(result)) > 1:
                        print(str(len(result)) + " résultats.")
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'], item['nb_round']))
                    choix = TOURNAMENT_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

            elif tournament_to_display == "display_completed_tournaments":
                result = TOURNAMENT_MODEL.search_completed_tournaments()
                if result == "no_result":
                    choix = TOURNAMENT_VIEW.choice_menu("Aucun tournoi à afficher. Recommencer (O/n)? ")
                    if choix == "N":
                        break
                else:
                    if (len(result)) == 1:
                        print(str(len(result)) + " résultat.")
                    elif (len(result)) > 1:
                        print(str(len(result)) + " résultats.")
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'], item['nb_round']))
                    choix = TOURNAMENT_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

            elif tournament_to_display == "display_current_tournaments":
                result = TOURNAMENT_MODEL.search_current_tournaments()
                if result == "no_result":
                    choix = TOURNAMENT_VIEW.choice_menu("Aucun tournoi à afficher. Recommencer (O/n)? ")
                    if choix == "N":
                        break
                else:
                    if (len(result)) == 1:
                        print(str(len(result)) + " résultat.")
                    elif (len(result)) > 1:
                        print(str(len(result)) + " résultats.")
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'], item['nb_round']))
                    choix = TOURNAMENT_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

            elif tournament_to_display == "display_not_started_tournaments":
                result = TOURNAMENT_MODEL.search_not_started_tournaments()
                if result == "no_result":
                    choix = TOURNAMENT_VIEW.choice_menu("Aucun tournoi à afficher. Recommencer (O/n)? ")
                    if choix == "N":
                        break
                else:
                    if (len(result)) == 1:
                        print(str(len(result)) + " résultat.")
                    elif (len(result)) > 1:
                        print(str(len(result)) + " résultats.")
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'], item['nb_round']))
                    choix = TOURNAMENT_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

    @staticmethod
    def begin_new_tournament():
        """ request for needed information (which tournament and players to associate) to begin new tournament """
        players_available_list = []
        match = None
        while True:
            players_available = PLAYER_MODEL.search_all_players()
            if players_available == "no_result" or len(players_available) <= 1:
                TOURNAMENT_VIEW.choice_menu("Liste des joueurs vide. Merci d'en créer au moins huit.\n"
                                            "disponibles pour démarrer un tournoi [ENTRER] pour revenir au menu.")
                break
            """ create list of players (uuid) """
            for i in range(len(players_available)):
                item = players_available[i]
                players_available_list.append(item['player_uuid'])

            """ create list of available tournaments (tournament not already started) """
            not_started_tournament = TOURNAMENT_MODEL.search_not_started_tournaments()
            if not_started_tournament == "no_result":
                TOURNAMENT_VIEW.choice_menu("Aucun tournoi disponible. Vous devez en créer un nouveau."
                                            " [ENTRER] pour continuer.")
                break

            """ displayer list of available tournaments """
            print("Liste des tournois non démarrés:")
            for i in range(len(not_started_tournament)):
                item = not_started_tournament[i]
                print(str(i + 1) + " - " + str(TournamentModel(item['name'], item['town'], item['nb_round'])))

            """ choose tournament """
            result = TOURNAMENT_VIEW.select_menu(not_started_tournament)
            selected_tournament = not_started_tournament[int(result) - 1]
            selected_tournament_uuid = selected_tournament['tournament_uuid']

            tournament_nb_round = TOURNAMENT_MODEL.search_nb_round_for_tournament(selected_tournament_uuid)
            """ compare nb rounds and nb players available to check if some players will play with the same 
            players twice - formula is nb round should not be superior of nb players available - 1
            example : if there is 8 players, nb match = 7 so nb round max should be equal or inferior to 7 """
            if int(tournament_nb_round) > (int(len(players_available)) - 1):
                print("Ce tournoi comporte " + str(tournament_nb_round) + " round(s) donc pas assez de joueurs"
                                                                          " disponibles pour éviter que certains ne se"
                                                                          " rencontrent deux fois.")

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
                    player = PLAYER_MODEL.extract_player_fname_and_name(player_uuid)
                    print(str(i + 1) + " - " + player + ".")
                print(str(nb_players) + " sélectionné(s).")
                result = PLAYER_VIEW.select_available_players_menu(len(players_available_list), nb_players)
                if result == "end_players_selection":
                    break
                selected_player_uuid = (players_available_list[int(result) - 1])
                TOURNAMENT_MODEL.add_player_uuid_to_tournament(selected_tournament_uuid, selected_player_uuid)
                nb_players_available -= 1
                nb_players += 1
                players_available_list.remove(selected_player_uuid)
                if nb_players_available == 1 and nb_players_available_pair is False:
                    print("Il ne reste plus qu'une personne, impossible de former une paire.\n"
                          "Fin de la selection.")
                    break
                elif nb_players_available == 0 or nb_players_available_pair == "True":
                    print("Plus de personne à ajouter.")
                    break

            print('Tournoi "' + selected_tournament['name'] + '" prêt.')
            if (nb_players - 1) < int(tournament_nb_round):
                print("Pour information : vu le faible nombre de joueurs sélectionnés et le grand nombre de rounds,"
                      " certains joueurs se rencontreront deux fois.")
            elif (nb_players - 1) > int(tournament_nb_round):
                print("Pour information : vu le faible nombre de rounds du tournoi et la quantité de joueurs"
                      " sélectionnés, certains joueurs ne se rencontreront pas.")

            TOURNAMENT_VIEW.choice_menu("Appuyez sur une [ENTRER] pour continuer.")

            """ beginning of the tournament """
            date = str(datetime.now())
            TOURNAMENT_MODEL.store_tournament_start_date(selected_tournament_uuid, date)
            players_uuid_list = TOURNAMENT_MODEL.extract_players_uuid_of_tournament(selected_tournament_uuid)
            nb_round = TOURNAMENT_MODEL.search_nb_round_for_tournament(selected_tournament_uuid)
            current_round = 1
            nb_match = int(len(players_uuid_list) / 2)

            for j in range(int(nb_round)):
                """ loop for all rounds """
                players_list_by_score = PLAYER_MODEL.create_player_list(players_uuid_list)
                current_match = 1
                for i in range(0, nb_match * 2, 2):
                    """ loop for all matches for one round"""
                    player_one_uuid = players_list_by_score[i]
                    player_two_uuid = players_list_by_score[i + 1]
                    player_one = PLAYER_MODEL.extract_player_fname_and_name(player_one_uuid)
                    player_two = PLAYER_MODEL.extract_player_fname_and_name(player_two_uuid)
                    print("Tour : " + str(current_round) + "/" + nb_round + ", match " + str(current_match)
                          + "/" + str(nb_match) + " opposant " + player_one + " à " + player_two + ".")
                    scores = PLAYER_VIEW.record_score(player_one, player_two)
                    match = MatchModel(selected_tournament_uuid, current_round, current_match, player_one_uuid,
                                       player_two_uuid, scores[0], scores[1])
                    match.create_tuple_for_match()
                    current_match += 1
                current_round += 1
            match_id_list = match.store_match()
            TOURNAMENT_MODEL.store_match_id(selected_tournament_uuid, match_id_list)
            date = str(datetime.now())
            TOURNAMENT_MODEL.store_tournament_end_date(selected_tournament_uuid, date)
            TOURNAMENT_VIEW.choice_menu("Fin du tournoi. Appuyez sur [ENTRER] pour revenir au menu.")
            break
