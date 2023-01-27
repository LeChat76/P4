import random
from views.menu import Menu


class Player:
    """ Player class """

    def __init__(self, fname, name, birthd):
        self.fname = fname
        self.name = name
        self.birthd = birthd
        self.player = None

    def __str__(self):
        return f"{self.fname} {self.name} né le {self.birthd}"
    """
    Nom de famille
    Prénom
    Date de naissance
    
    premier tour : mélanger les joueurs aléatoirement
    ensuite, chaque paire de joueurs est géré de la façon suivante:
        * triez les joueurs par points
        * associez les joueurs par paire et par ordre de points (si joueurs avec même nb de points, choix aléatoire)
        * NE PAS GENERER DE PAIRE AYANT DEJA JOUE ENSEMBLE
        * choix de la couleur tiré au sort (le menu doit donc demander qui a noir et qui a blanc)
    """

    def player_group_ran(self):
        pass
# player = Player("Cedric", "Delauney", "16 juillet 1975")
# print(player)
index = 1
while index % 2 != 0:
    menu = Menu()
    player[index] = menu.player_menu()
    print(player[index])
    index += 1

