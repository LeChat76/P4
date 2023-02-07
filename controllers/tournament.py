from views.start_menu import MainMenu
from views.tournament import TournamentView
from models.tournament import TournamentModel
MAINMENU = MainMenu()
TOURNAMENT_VIEW = TournamentView()
TOURNAMENT_MODEL = TournamentModel()
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
            # elif choix == MENU_TOURNAMENT_START:
            #     self.start_tournament()
            # elif choix == MENU_TOURNAMENT_RECOVERY:
            #     self.back_to_tournament()
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
                    for i in range(len(result)):
                        item = result[i]
                        print(TournamentModel(item['name'], item['town'], item['start_date'], item['end_date']))
                    choix = TOURNAMENT_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break
