import datetime
from os import system

PLAYER_LIST = []


class Menu:
    """ Menu class """

    def main_menu(self):
        """ Root menu """
        choix = None
        while choix != 1 and choix != 2 and choix != 3 and choix != 4:
            system('cls')
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
        else:
            exit()

    def tournament_menu(self):
        """ Menu 1 """
        choix = None
        while choix != 1 and choix != 2 and choix != 3:
            system('cls')
            print("+-------------------------------+")
            print("| 1 - création d'un tournoi     |")
            print("| 2 - reprise d'un tournoi      |")
            print("| 3 - revenir au menu principal |")
            print("+-------------------------------+")
            choix = input("Quel est votre choix : ")
            if not choix.isnumeric():
                print("Merci de préciser un choix numérique.")
                choix = None
            else:
                choix = int(choix)
        if choix == 1:
            return "menu_1_1"
        elif choix == 2:
            return "menu_1_2"
        elif choix == 3:
            return "menu_1_3"

    def tournament_creation(self):
        """ Menu 1 - 1 """
        system('cls')
        tournament_name = None
        while not tournament_name:
            tournament_name = input("Nom du tournoi : ")
            if not tournament_name:                             # juste pour debugging, à supprimer
                tournament_name = "Chess master Rouen"          # juste pour debugging, à supprimer

    def player_menu(self):
        """ Menu 2 """
        choix = None
        while choix != 1 and choix != 2 and choix != 3:
            system('cls')
            print("+-------------------------------+")
            print("| 1 - création d'un joueur      |")
            print("| 2 - suppression d'un joueur   |")
            print("| 3 - revenir au menu principal |")
            print("+-------------------------------+")
            choix = input("Quel est votre choix : ")
            if not choix.isnumeric():
                print("Merci de préciser un choix numérique.")
                choix = None
            else:
                choix = int(choix)
        if choix == 1:
            return "menu_2_1"
        if choix == 2:
            return "menu_2_2"
        if choix == 3:
            return "menu_2_3"

    def add_player_menu(self):
        """ Requests for player first name """

        new_one_player = " "

        while new_one_player.upper() != "N":

            system('cls')
            player_fname = None
            while not player_fname:
                while True:
                    player_fname = input("Prénom du joueur : ")
                    if not player_fname:                        # juste pour debugging, à supprimer
                        player_fname = "cedric"                 # juste pour debugging, à supprimer
                    if not player_fname.isalpha():
                        print("Le prénom ne doit pas contenir de chiffre. Merci de ressaisir.")
                    else:
                        break

            """ Requests for player name """
            player_name = None
            while not player_name:
                while True:
                    player_name = input("Nom du joueur : ")
                    if not player_name:                         # juste pour debugging, à supprimer
                        player_name = "delauney"                # juste pour debugging, à supprimer
                    if not player_name.isalpha():
                        print("Le nom ne doit pas contenir de chiffre. Merci de ressaisir.")
                    else:
                        break

            """ Requests for player birthday """
            player_birthd = ""
            while not player_birthd:
                while True:
                    player_birthd = input("Date d'anniversaire (au format JJ/MM/AAAA) : ")
                    if player_birthd == "":  # juste pour debugging, à supprimer
                        player_birthd = "16/07/1975"  # juste pour debugging, à supprimer
                    try:
                        datetime.datetime.strptime(player_birthd, '%d/%m/%Y')
                    except ValueError:
                        print("Mauvais format de date. Merci de ressaisir.")
                    else:
                        break

            """ Requests for player clubid """
            player_clubid = None
            while not player_clubid:
                while True:
                    player_clubid = input("ID du club (au format AB12345) : ")
                    if player_clubid == "":                 # juste pour debugging, à supprimer
                        player_clubid = "ab12345"           # juste pour debugging, à supprimer
                    if len(player_clubid) != 7:
                        print("Le club ID doit comporter 7 caractères. Merci de ressaisir.")
                    elif not player_clubid[:2].isalpha():
                        print("Les 2 premiers caractères doivent être des lettres. Merci de ressaisir.")
                    elif not player_clubid[2:].isnumeric():
                        print("les 5 derniers caractères doivent être des chiffres. Merci de ressaisir.")
                    else:
                        player_clubid = str(player_clubid[:2].upper()) + str(player_clubid[2:])
                        break

            PLAYER_LIST.append([player_fname, player_name, player_birthd, player_clubid])

            new_one_player = input("Ajouter un autre joueur au tournoi (O/n)?")

        return PLAYER_LIST

    def delete_player_menu(self):
        """ Request for delete player """
        del_player_name = None
        while not del_player_name:
            while True:
                del_player_name = input("Merci de préciser le nom de la personne commençant par : ")
                if del_player_name == "":                     # juste pour debugging, à supprimer
                    del_player_name = "delauney"               # juste pour debugging, à supprimer
                if not del_player_name.isalpha():
                    print("Merci de préciser un nom sans chiffres. Merci de ressaisir.")
                else:
                    return del_player_name
