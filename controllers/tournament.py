from views.start_menu import MainMenu
from views.tournament import TournamentView
from models.tournament import TournamentModel
MAINMENU = MainMenu()
TOURNAMENT_VIEW = TournamentView()
TOURNAMENT_MODEL = TournamentModel()


class TournamentController:

    def menu_1(self):
        """ Tournament Menu """
        while True:
            choix = TOURNAMENT_VIEW.tournament_menu()
            if choix == "menu_1_1":
                self.add_tournament()
            elif choix == "menu_1_2":
                self.display_tournament()
            # elif choix == "menu_1_3":
            #     self.start_tournamend()
            # elif choix == "menu_1_4":
            #     self.back_to_tournamend()
            elif choix == "menu_1_5":
                break

    def add_tournament(self):
        """ methdo to record new tournaments """
        new_tournament = TOURNAMENT_VIEW.add_tournament_menu()
        for tournament in new_tournament:
            tournament_to_add = TournamentModel(tournament[0], tournament[1], tournament[2], tournament[3],
                                                tournament[4], tournament[5])
            tournament_to_add.add_tournament()

    def display_tournament(self):
        pass

