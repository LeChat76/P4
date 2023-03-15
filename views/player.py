import datetime
import os
from constantes import MENU_PLAYER_CREATION, MENU_PLAYERS_DISPLAY, MENU_PLAYERS_DELETE, MENU_PLAYERS_EXIT, PLAYER_LIST


class PlayerView:
    """ Menu class """

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

    def add_player(self, associate_to_tournament):
        """ Requests for player first name """
        new_one_player = " "
        PLAYER_LIST.clear()

        while new_one_player.upper() != "N":

            self.clear_screen()
            player_fname = None
            while not player_fname:
                while True:
                    player_fname = input("Prénom du joueur : ")
                    if not self.test_value(player_fname):
                        print("Caractère(s) interdit(s) détecté(s), ressaisir le prénom SVP.")
                    else:
                        break

            """ Requests for player name """
            player_name = None
            while not player_name:
                while True:
                    player_name = input("Nom du joueur : ")
                    if not self.test_value(player_name):
                        print("Caractère(s) interdit(s) détecté(s), ressaisir le nom SVP.")
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
                        print("Mauvais format de date, ressaisir la date d'anniversaire SVP.")
                    else:
                        break

            """ Requests for player clubid """
            player_clubid = None
            while not player_clubid:
                while True:
                    player_clubid = input("ID du club (au format AB12345) : ")
                    if len(player_clubid) != 7:
                        print("Le club ID doit comporter 7 caractères, ressaisir le club ID.")
                    elif not player_clubid[:2].isalpha():
                        print("Les 2 premiers caractères doivent être des lettres, ressaisir le club ID.")
                    elif not player_clubid[2:].isnumeric():
                        print("les 5 derniers caractères doivent être des chiffres, ressaisir le club ID.")
                    else:
                        player_clubid = str(player_clubid[:2].upper()) + str(player_clubid[2:])
                        break

            PLAYER_LIST.append([player_fname, player_name, player_birthd, player_clubid])

            new_one_player = input("Ajouter un autre joueur au tournoi (O/n)?")
            if new_one_player.upper() == "N" and associate_to_tournament and len(PLAYER_LIST)%2 != 0:
                print("Vous devez avoir un nombre pair de joueurs. Saisissez un dernier joueur SVP.")
                new_one_player = "Y"

        return PLAYER_LIST

    def delete_player(self, players_list):
        """ Request for select player to delete """
        index = 1
        for player in players_list:
            print(str(index) + " - " + str(player))
            index += 1
        while True:
            while True:
                choice = input("Saisir le numéro du joueur à supprimer : ")
                if not choice.isnumeric():
                    print("La saisie doit être uniquement un chiffre. Merci de ressaisir.")
                else:
                    return players_list[int(choice) - 1]

    def display_player(self):
        """ Request for display player """
        dis_player_menu = None
        while not dis_player_menu:
            while True:
                dis_player_name = input("Afficher les noms commençant par ([ENTER] = afficher tout) : ")
                if not dis_player_name:
                    return "display_all"
                elif not dis_player_name.isalpha():
                    print("Nom incorrect. Merci de ressaisir.")
                elif dis_player_name.isalpha() and len(dis_player_name) > 0:
                    return dis_player_name

    def choice(self, question):
        """ method for asking to restart request """
        choix = ""
        while choix.upper() != "O" or choix.upper() != "N":
            choix = input(question)
            if choix.upper() == "O" or choix == "":
                return "O"
            elif choix.upper() == "N":
                return "N"

    def select_available_players(self, nb_players_available, nb_players):
        """ method to select multiples players """
        while True:
            choice = input("Merci de sélectionner un joueur à ajouter [ENTRER pour terminer]: ")
            if choice.isalpha():
                print("Merci de préciser un chiffre uniquement.")
            elif not choice:
                if nb_players % 2 != 0 or nb_players == 0:
                    print("Vous avez sélectionné " + str(nb_players)
                          + " joueurs. Il faut un nombre pair de joueurs pour former des équipes.")
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
        try:
            float(score_is_float)
            return True
        except ValueError:
            return False

    def text_to_print(self, text):
        """ method to print text from controller """
        print(text)

    def clear_screen(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system('cls')

    def test_value(self, value):
        """ method to check if no forbidden characters are in a value"""
        specials_authorized_char = [" ", "-"]
        result = False
        if not value.isalpha():
            # methode ne fonctionne pas, si caractère autorisé + caractère interdit : ça passe donc pas bon
            for special_authorized_char in specials_authorized_char:
                if special_authorized_char in value:
                    result = True
                    continue
        elif value.isalpha():
            result = True
        return result
