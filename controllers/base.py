from views.start_menu import MainMenu
from controllers.player import PlayerController
from controllers.tournament import TournamentController
MAIN_MENU = MainMenu()
PLAYER_CONTROLLER = PlayerController()
TOURNAMENT_CONTROLLER = TournamentController()


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

    def Tournament_Start(self):
        """ start tournament method """
        while True:
            choix = MAIN_MENU.main_menu()
            if choix == "menu_1":
                TOURNAMENT_CONTROLLER.menu_1()
            elif choix == "menu_2":
                PLAYER_CONTROLLER.menu_2()
            # elif choix_menu == "menu_3":
            #    self.statistics_menu()
            elif choix == "menu_4":
                exit()
