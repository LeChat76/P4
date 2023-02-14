import os
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data", "tournaments")
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
    with open(os.path.join(DATA_FOLDER, "players.json"), 'w') as creating_players_file:
        pass
    with open(os.path.join(DATA_FOLDER, "tournaments.json"), 'w') as creating_tournaments_file:
        pass
from views.start_menu import MainMenu
from controllers.player import PlayerController
from controllers.tournament import TournamentController
from controllers.result import ResultController
MAIN_MENU = MainMenu()
PLAYER_CONTROLLER = PlayerController()
TOURNAMENT_CONTROLLER = TournamentController()
RESULT_CONTROLLER = ResultController
MENU_PLAYERS = 1
MENU_TOURNAMENTS = 2
MENU_RESULTS = 3
MENU_EXIT = 4


class ChessTournament:
    """ Player controller """
    """
    premier tour : mélanger les joueurs aléatoirement
    ensuite, chaque paire de joueurs est géré de la façon suivante:
        * triez les joueurs par points
        * associez les joueurs par paire et par ordre de points (si joueurs avec même nb de points, choix aléatoire)
        * NE PAS GÉNÉRER DE PAIRE AYANT DEJA JOUE ENSEMBLE
        * choix de la couleur tiré au sort (le menu doit donc demander qui a noir et qui a blanc)
    """
    @staticmethod
    def tournament_start():
        """ start tournament method """
        while True:
            choix = MAIN_MENU.main_menu()
            if choix == MENU_PLAYERS:
                PLAYER_CONTROLLER.menu_1()
            elif choix == MENU_TOURNAMENTS:
                TOURNAMENT_CONTROLLER.menu_2()
            elif choix == MENU_RESULTS:
                RESULT_CONTROLLER.menu_3()
            elif choix == MENU_EXIT:
                exit()
