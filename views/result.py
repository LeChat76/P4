import os
MENU_RESULT_TOURNAMENT = 1
MENU_RESULT_PLAYER = 2
MENU_RESULT_EXIT = 3


class ResultView:

    def result_menu(self):
        """ Menu 3 """
        choix = None
        while choix != MENU_RESULT_TOURNAMENT and choix != MENU_RESULT_PLAYER:
            self.clear_screen()
            print("+-------------------------------+")
            print("|       MENU RESULTATS          |")
            print("+-------------------------------+")
            print("| 1 - score d'un tournoi        |")
            print("| 2 - score d'un joueur         |")
            print("| 3 - revenir au menu principal |")
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