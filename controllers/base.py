import os
from views.start_menu import MainMenu
from controllers.player import PlayerController
from controllers.tournament import TournamentController
MAIN_MENU = MainMenu()
PLAYER_CONTROLLER = PlayerController()
TOURNAMENT_CONTROLLER = TournamentController()
MENU_TOURNAMENT = 1
MENU_PLAYERS = 2
MENU_REPORTS = 3
MENU_EXIT = 4
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data", "tournaments")
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
    with open(os.path.join(DATA_FOLDER, "players.json")):
        pass
    with open(os.path.join(DATA_FOLDER, "tournaments.json")):
        pass


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
            if choix == MENU_TOURNAMENT:
                TOURNAMENT_CONTROLLER.menu_1()
            elif choix == MENU_PLAYERS:
                PLAYER_CONTROLLER.menu_2()
            # elif choix_menu == MENU_REPORTS:
            #    self.statistics_menu()
            elif choix == MENU_EXIT:
                exit()
