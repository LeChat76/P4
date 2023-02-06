import os


class MainMenu:

    def main_menu(self):
        """ Root menu """
        choix = None
        while choix != 1 and choix != 2 and choix != 3 and choix != 4:
            self.clear_screen()
            print("+-------------------------------+")
            print("| 1 - tournois                  |")
            print("| 2 - joueurs                   |")
            print("| 3 - statistiques              |")
            print("| 4 - quitter                   |")
            print("+-------------------------------+")
            choix = input("Quel est votre choix : ")
            if not choix.isnumeric():
                print("Merci de préciser un choix numérique.")
                choix = None
            else:
                choix = int(choix)
        if choix == 1:
            return "menu_1"
        elif choix == 2:
            return "menu_2"
        elif choix == 3:
            return "menu_3"
        elif choix == 4:
            return "menu_4"

    def clear_screen(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system('cls')
