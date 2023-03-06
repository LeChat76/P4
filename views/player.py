import datetime
import os
from constantes import MENU_PLAYER_CREATION, MENU_PLAYERS_DISPLAY, MENU_PLAYERS_DELETE, MENU_PLAYERS_EXIT, PLAYER_LIST


class PlayerView:
    """ Menu class """
    def __init__(self):
        self.text = None
        self.score_is_float = None
        self.all_player_list = None
        self.player_one = None
        self.player_two = None
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
        self.clear_screen()
        return choix

    def add_player(self):
        """ Requests for player first name """
        new_one_player = " "
        PLAYER_LIST.clear()

        while new_one_player.upper() != "N":

            self.clear_screen()
            player_fname = None
            while not player_fname:
                while True:
                    player_fname = input("Prénom du joueur : ")
                    if not player_fname.isalpha():
                        print("Le prénom ne doit pas contenir de chiffre. Merci de ressaisir.")
                    else:
                        break

            """ Requests for player name """
            player_name = None
            while not player_name:
                while True:
                    player_name = input("Nom du joueur : ")
                    if not player_name.isalpha():
                        print("Le nom ne doit pas contenir de chiffre. Merci de ressaisir.")
                    else:
                        break

            """ Requests for player birthday """
            player_birthd = ""
            while not player_birthd:
                while True:
                    player_birthd = input("Date d'anniversaire (au format JJ/MM/AAAA) : ")
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

    def delete_player(self, all_player_list):
        """ Request for select player to delete """
        self.all_player_list = all_player_list
        player_to_delete = None
        for i in range(len(all_player_list)):
            item = all_player_list[i]
            print(str(i + 1) + " - " + item['fname'].capitalize() + " " + item['name'].upper() + ".")
        while not player_to_delete:
            while True:
                player_to_delete = input("Saisir le numéro du joueur à supprimer : ")
                if not player_to_delete.isnumeric():
                    print("La saisie doit être uniquement un chiffre. Merci de ressaisir.")
                else:
                    return int(player_to_delete) - 1

    @staticmethod
    def display_player():
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

    def choice(self, question):
        """ method for asking to restart request """
        self.question = question
        choix = ""
        while choix.upper() != "O" or choix.upper() != "N":
            choix = input(self.question)
            if choix.upper() == "O" or choix == "":
                return "O"
            elif choix.upper() == "N":
                return "N"

    def select_available_players(self, nb_players_available, nb_players):
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
                    print("Vous avez sélectionné " + str(nb_players) + " joueurs. Il faut un nombre pair de\njoueurs"
                                                                       " pour former des équipes.")
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
        """ method to request score for player's match """
        result1 = None
        self.player_one = player_one
        self.player_two = player_two
        while result1 != 0 and result1 != 0.5 and result1 != 1:
            result1 = input("Score du joueur " + player_one + " : ")
            if result1.isnumeric():
                result1 = int(result1)
                if result1 != 0 and result1 != 0.5 and result1 != 1:
                    print("Le score ne peut être que : 0 pour le perdant\n"
                          "                            1 pour le gagnant\n"
                          "                            0.5 pour une égalité")
            elif self.isfloat(result1):
                result1 = float(result1)
            elif not result1.isnumeric():
                print("Merci de saisir uniquement une valeur numérique.")
        if result1 == 0:
            print("Le score de " + player_two + " est donc 1.")
            result2 = 1
        elif result1 == 0.5:
            print("Le score de " + player_two + " est donc 0.5.")
            result2 = 0.5
        else:
            print("Le score de " + player_two + " est donc 0.")
            result2 = 0
        return result1, result2

    def isfloat(self, score_is_float):
        self.score_is_float = score_is_float
        try:
            float(self.score_is_float)
            return True
        except ValueError:
            return False

    def text_to_print(self, text):
        """ method to print text from controller """
        self.text = text
        print(text)

    @staticmethod
    def clear_screen():
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system('cls')
