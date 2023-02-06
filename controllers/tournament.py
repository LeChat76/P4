from views.start_menu import MainMenu
from views.tournament import TournamentView
TOURNAMENT_VIEW = TournamentView()
MAINMENU = MainMenu()


class TournamentController:

    def menu_1(self):
        """ Tournament Menu """
        while True:
            choix = TOURNAMENT_VIEW.tournament_menu()
            if choix == "menu_1_1":
                self.add_tournament()
            elif choix == "menu_1_2":
                self.back_to_tournamend()
            elif choix == "menu_1_3":
                return "main_menu"

    def add_tournament(self):
        TOURNAMENT_VIEW.add_tournament_menu()

