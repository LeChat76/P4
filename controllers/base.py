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
from views.start_menu import MainMenu
from controllers.player import PlayerController
from controllers.tournament import TournamentController
from controllers.report import ReportController
MAIN_MENU = MainMenu()
MENU_PLAYERS = 1
MENU_TOURNAMENTS = 2
MENU_REPORTS = 3
MENU_EXIT = 4


class ChessTournament:
    """ Player controller """

    @staticmethod
    def tournament_start():
        """ start tournament method """
        while True:
            choix = MAIN_MENU.main_menu()
            if choix == MENU_PLAYERS:
                PlayerController().menu_1()
            elif choix == MENU_TOURNAMENTS:
                TournamentController().menu_2()
            elif choix == MENU_REPORTS:
                ReportController().menu_3()
            elif choix == MENU_EXIT:
                exit()
