from views.start_menu import MainMenu
from constantes import MENU_PLAYERS, MENU_TOURNAMENTS, MENU_REPORTS, MENU_EXIT
import os
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data",
                           "tournaments")
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
    with open(os.path.join(DATA_FOLDER, "players.json"), 'w') as\
            creating_players_file:
        pass
    with open(os.path.join(DATA_FOLDER, "tournaments.json"), 'w') as\
            creating_tournaments_file:
        pass
from controllers.tournament import TournamentController
from controllers.player import PlayerController
from controllers.report import ReportController


class ChessTournament:
    def __init__(self):
        self.view_main_menu = MainMenu()
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()
        self.report_controller = ReportController()

    def tournament_start(self):
        """ start tournament method """
        while True:
            choix = self.view_main_menu.main_menu()
            if choix == MENU_PLAYERS:
                self.player_controller.menu_player()
            elif choix == MENU_TOURNAMENTS:
                self.tournament_controller.menu_tournament()
            elif choix == MENU_REPORTS:
                self.report_controller.menu_report()
            elif choix == MENU_EXIT:
                exit()
