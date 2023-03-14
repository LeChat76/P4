import sys
import os
from views.start_menu import MainMenu
from constantes import MENU_PLAYERS, MENU_TOURNAMENTS, MENU_REPORTS, MENU_EXIT
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
                sys.exit()
