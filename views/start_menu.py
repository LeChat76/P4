import os
from constantes import *


class MainMenu:
    """ Main Menu Class """
    def main_menu(self):
        """ Root menu """
        choix = None
        while choix != MENU_TOURNAMENTS and choix != MENU_PLAYERS\
                and choix != MENU_REPORTS and choix != MENU_EXIT:
            self.clear_screen()
            print("+-------------------------------+")
            print("|            MENU               |")
            print("+-------------------------------+")
            print("| 1 - joueurs                   |")
            print("| 2 - tournois                  |")
            print("| 3 - rapports                  |")
            print("| 4 - quitter                   |")
            print("+-------------------------------+")
            choix = input("Quel est votre choix : ")
            if not choix.isnumeric():
                print("Merci de préciser un choix numérique.")
                choix = None
            else:
                choix = int(choix)

        return choix

    @staticmethod
    def clear_screen():
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system('cls')
