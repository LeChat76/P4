import datetime
import os
PLAYER_LIST = []
MENU_PLAYER_CREATION = 1
MENU_PLAYERS_DISPLAY = 2
MENU_PLAYERS_DELETE = 3
MENU_PLAYERS_EXIT = 4


class PlayerView:
    """ Menu class """
    def __init__(self):
        self.player_two = None
        self.player_one = None
        self.nb_players = None
        self.nb_players_available = None
        self.question = None

    def player_menu(self):
        """ Menu 2 """
        choix = None
        while choix != MENU_PLAYER_CREATION and choix != MENU_PLAYERS_DISPLAY and choix != MENU_PLAYERS_DELETE and\
                choix != MENU_PLAYERS_EXIT:
            self.clear_screen()
            print("+-------------------------------+")
            print("|          MENU JOUEUR          |")
            print("+-------------------------------+")
            print("| 1 - création d'un joueur      |")
            print("| 2 - affichage des joueurs     |")
            print("| 3 - suppression d'un joueur   |")
            print("| 4 - revenir au menu principal |")
            print("+-------------------------------+")
            choix = input("Quel est votre choix : ")
            if not choix.isnumeric():
                print("Merci de préciser un choix numérique.")
                choix = None
            else:
                choix = int(choix)
        return choix

    def add_player_menu(self):
        """ Requests for player first name """
        new_one_player = " "
        PLAYER_LIST.clear()

        while new_one_player.upper() != "N":

            self.clear_screen()
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
                    if player_birthd == "":                     # juste pour debugging, à supprimer
                        player_birthd = "16/07/1975"            # juste pour debugging, à supprimer
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

    @staticmethod
    def delete_player_menu():
        """ Request for delete player """
        del_player_name = None
        while not del_player_name:
            while True:
                del_player_name = input("Merci de préciser le nom de la personne contenant : ")
                if del_player_name == "":                      # juste pour debugging, à supprimer
                    del_player_name = "delauney"               # juste pour debugging, à supprimer
                if not del_player_name.isalpha():
                    print("Nom incorrect. Merci de ressaisir.")
                else:
                    return del_player_name

    @staticmethod
    def display_player_menu():
        """ Request for display player """
        dis_player_menu = None
        while not dis_player_menu:
            while True:
                dis_player_name = input("Afficher les noms contenant ([ENTER] = afficher tout) : ")
                if not dis_player_name:
                    return "display_all"
                elif not dis_player_name.isalpha():
                    print("Nom incorrect. Merci de ressaisir.")
                elif dis_player_name.isalpha() and len(dis_player_name) > 0:
                    return dis_player_name

    def choice_menu(self, question):
        """ method for asking to restart request """
        self.question = question
        choix = ""
        while choix.upper() != "O" or choix.upper() != "N":
            choix = input(self.question)
            if choix.upper() == "O" or choix == "":
                return "O"
            elif choix.upper() == "N":
                return "N"

    def select_available_players_menu(self, nb_players_available, nb_players):
        """ method to select multiples players """
        self.nb_players_available = nb_players_available
        self.nb_players = nb_players
        while True:
            choice = input("Merci de sélectionner un joueur à ajouter [ENTRER pour terminer]: ")
            self.clear_screen()
            if choice.isalpha():
                print("Merci de préciser un chiffre uniquement.")
            elif not choice:
                if self.nb_players % 2 != 0 or self.nb_players == 0:
                    print("Vous avez sélectionné " + str(nb_players) + " joueurs. Il faut un nombre pair de\n"
                          "joueurs pour former des équipes.")
                    continue
                else:
                    return "end_players_selection"
            elif int(choice) > int(nb_players_available):
                print("Choix incorrect. Merci de ressaisir.")
            elif int(choice) <= 0:
                print("Choix incorrect. Merci de ressaisir.")
            else:
                return choice

    def record_score(self, player_one, player_two):
        result1 = None
        result2 = None
        self.player_one = player_one
        self.player_two = player_two
        while result1 != 0 and result1 != 0.5 and result1 != 1:
            result1 = input("Score du joueur " + player_one + " : ")
            if not result1.isnumeric():
                print("Merci de saisir uniquement une valeur numérique.")
            elif result1.isnumeric():
                result1 = int(result1)
                if result1 != 0 and result1 != 0.5 and int(result1) != 1:
                    print("Le score ne peut être que : 0 pour le perdant\n"
                          "                            1 pour le gagnant\n"
                          "                            0.5 pour une égalité")
        if result1 == 0:
            print("Le score de " + player_two + " est donc 1.")
            result2 = 1
        elif result1 == 0.5:
            print("Le score de " + player_two + " est donc 0.5.")
            result2 = 0.5
        else:
            print("Le score de " + player_two + " est donc 0.")
            result = 0
        return result1, result2

    @staticmethod
    def clear_screen():
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system('cls')
