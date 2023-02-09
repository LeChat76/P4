from views.start_menu import MainMenu
from views.tournament import TournamentView
from views.player import PlayerView
from models.tournament import TournamentModel
from models.player import PlayerModel
MAINMENU = MainMenu()
TOURNAMENT_VIEW = TournamentView()
TOURNAMENT_MODEL = TournamentModel()
PLAYER_VIEW = PlayerView()
PLAYER_MODEL = PlayerModel()
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
                    choix = TOURNAMENT_VIEW.choice_menu("Aucun tournoi à afficher. Recommencer (O/n)? ")
                    if choix == "N":
                        break
                else:
                    if (len(result)) == 1:
                        print(str(len(result)) + " résultat.")
                    elif (len(result)) > 1:
                        print(str(len(result)) + " résultats.")
                    i = 0
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'], item['start_date'], item['end_date']))
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
                    i = 0
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'], item['start_date'], item['end_date']))
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
                    i = 0
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'], item['start_date'], item['end_date']))
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
                    i = 0
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'], item['start_date'], item['end_date']))
                    choix = TOURNAMENT_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

    @staticmethod
    def begin_new_tournament():
        """ request for needed information (which tournament and players to associate) to begin new tournament """
        while True:
            players_available = PLAYER_MODEL.search_available_player()
            if players_available == "no_result" or len(players_available) <= 1:
                TOURNAMENT_VIEW.choice_menu("Aucun joueur disponible. Vous devez en avoir au moins deux\n"
                                            "disponibles pour démarrer un tournoi [ENTRER] pour revenir au menu.")
                break
            not_started_tournament = TOURNAMENT_MODEL.search_not_started_tournaments()
            if not_started_tournament == "no_result":
                TOURNAMENT_VIEW.choice_menu("Aucun tournoi disponible. Vous devez en créer un nouveau."
                                            " [ENTRER] pour continuer.")
                break
            print("Liste des tournois non démarrés:")
            i = 0
            for i in range(len(not_started_tournament)):
                item = not_started_tournament[i]
                print(str(i + 1) + " - " + str(TournamentModel(item['name'], item['town'], item['start_date'],
                                                               item['end_date'])))
            result = TOURNAMENT_VIEW.select_menu(not_started_tournament)
            selected_tournament = not_started_tournament[int(result) - 1]
            selected_tournament_uuid = selected_tournament['tournament_uuid']

            """ Selection of players to add to the selected tournament """
            nb_players = 0
            nb_players_available = len(players_available)
            if nb_players_available % 2 != 0:
                nb_players_available_pair = False
            else:
                nb_players_available_pair = True
            while True:
                print(str(nb_players_available) + " joueurs disponibles:")
                for i in range(nb_players_available):
                    item = players_available[i]
                    print(str(i + 1) + " - " + item['fname'].capitalize() + " " + item['name'].upper() + ".")
                print(str(nb_players) + " joueur(s) sélectionné(s).")
                result = PLAYER_VIEW.select_available_players_menu(len(players_available), nb_players)
                if result == "end_players_selection":
                    break
                selected_player_uuid = (players_available[int(result) - 1])['player_uuid']
                PLAYER_MODEL.add_player_tournament_uuid(selected_player_uuid, selected_tournament_uuid)
                nb_players_available -= 1
                nb_players += 1
                players_available = PLAYER_MODEL.search_available_player()
                if nb_players_available == 1 and nb_players_available_pair is False:
                    print("Il ne reste plus qu'une personne, impossible de former une paire.\n"
                          "Fin de la selection.")
                    break
                elif nb_players_available == 0 or nb_players_available_pair == "True":
                    print("Plus de personne à ajouter.")
                    break
            print('Tournoi "' + selected_tournament['name'] + '" prêt.')

            """ beginning of the tournament """
            players_list = PLAYER_MODEL.create_player_list_with_same_t_uuid(selected_tournament_uuid)
            players_list_uuid = []
            i = 0
            for i in range(len(players_list)):
                player = players_list[i]
                player[i] = player['player_uuid']
                players_list_uuid.append(player['player_uuid'])

            """ creation of lists of matches and rounds """
            nb_match = nb_players - 1
            nb_round = TOURNAMENT_MODEL.search_nb_round_for_tournament(selected_tournament_uuid)
            players_list_by_score = PLAYER_MODEL.create_player_list_by_score(players_list)
            i = 0
            for i in range(nb_players):
                players_list_sorted = players_list_by_score[i]
                print(players_list_sorted)
            print("Fin pour le moment.")
            break
