import datetime
from views.menu import Menu
from models.player import Player

class Controller:
    """ Main controller """

    """
    premier tour : mélanger les joueurs aléatoirement
    ensuite, chaque paire de joueurs est géré de la façon suivante:
        * triez les joueurs par points
        * associez les joueurs par paire et par ordre de points (si joueurs avec même nb de points, choix aléatoire)
        * NE PAS GENERER DE PAIRE AYANT DEJA JOUE ENSEMBLE
        * choix de la couleur tiré au sort (le menu doit donc demander qui a noir et qui a blanc)
    """

    def __init__(self):
        pass

    def start_tournament(self):
        """ Request for players """
        player_fname = None
        player_name = None
        player_birthd = None
        player_clubID = None
        menu = Menu()

        while not player_fname:
            player_fname = menu.prompt_player_fname()

        while not player_name:
            player_name = menu.prompt_player_name()

        while not player_birthd:
            while True:
                player_birthd = menu.prompt_player_birthd()
                try:
                    datetime.datetime.strptime(player_birthd, '%d/%m/%Y')
                except ValueError:
                    print("Mauvais format de date. Merci de ressaisir.")
                else:
                    break

        while not player_clubID:
            while True:
                player_clubID = menu.prompt_player_clubID()
                if len(player_clubID) != 7:
                    print("Mauvais format de club ID. Merci de ressaisir.")
                else:
                    break

        player = Player(player_fname.capitalize(), player_name.capitalize(), player_birthd, player_clubID.upper())
        print(player)

