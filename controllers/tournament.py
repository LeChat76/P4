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

    def menu_1(self):
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
            tournament_to_add = TournamentModel(tournament[0], tournament[1], tournament[2], tournament[3],
                                                tournament[4], tournament[5])
            tournament_to_add.add_tournament()

    @staticmethod
    def display_tournament():
        """ method to display tournaments completed, current or all """
        while True:
            tournament_to_display = TOURNAMENT_VIEW.display_tournament()
            if tournament_to_display == "display_all_tournaments":
                result = TOURNAMENT_MODEL.display_all_tournaments()
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
                        print(TournamentModel(item['name'], item['town'], item['start_date'], item['end_date']))
                    choix = TOURNAMENT_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

            elif tournament_to_display == "display_completed_tournaments":
                result = TOURNAMENT_MODEL.display_completed_tournaments()
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
                        print(TournamentModel(item['name'], item['town'], item['start_date'], item['end_date']))
                    choix = TOURNAMENT_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

            elif tournament_to_display == "display_current_tournaments":
                result = TOURNAMENT_MODEL.display_current_tournaments()
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
                        print(TournamentModel(item['name'], item['town'], item['start_date'], item['end_date']))
                    choix = TOURNAMENT_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

            elif tournament_to_display == "display_not_started_tournaments":
                result = TOURNAMENT_MODEL.display_not_started_tournaments()
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
                        print(TournamentModel(item['name'], item['town'], item['start_date'], item['end_date']))
                    choix = TOURNAMENT_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

    @staticmethod
    def begin_new_tournament():
        """ method to begin new tournament """
        while True:
            players_available = PLAYER_MODEL.search_available_player()
            if players_available == "no_result" or len(players_available) == 0:
                wait = TOURNAMENT_VIEW.choice_menu("Aucun joueur disponible. Vous devez en avoir au moins deux"
                                                   " disponibles pour démarrer un tournoi [ENTRER] pour continuer.")
                break
            elif len(players_available) == 1:
                wait = TOURNAMENT_VIEW.choice_menu("Un seul joueur disponible. Vous devez en avoir au moins deux"
                                                   " disponibles pour démarrer un tournoi [ENTRER] pour continuer.")
                break
            else:
                not_started_tournament = TOURNAMENT_MODEL.search_not_started_tournaments()
                if not_started_tournament == "no_result":
                    wait = TOURNAMENT_VIEW.choice_menu("Aucun tournoi disponible. Vous devez en créer un nouveau."
                                                       " [ENTRER] pour continuer.")
                    break
                else:
                    print("Liste des tournois non démarrés:")
                    for i in range(len(not_started_tournament)):
                        item = not_started_tournament[i]
                        print(str(i + 1) + " - " + str(TournamentModel(item['name'], item['town'], item['start_date'],
                                                                       item['end_date'])))
                    result = TOURNAMENT_VIEW.select_menu(not_started_tournament)
                    selected_tournament = not_started_tournament[int(result) - 1]
            print(str(len(players_available)) + " joueurs disponibles:")
            for i in range(len(players_available)):
                item = players_available[i]
                print(str(i + 1) + " - " + item['fname'].capitalize() + " " + item['name'].upper() + ".")
            result = PLAYER_VIEW.multi_select_menu()

