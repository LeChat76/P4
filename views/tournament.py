import os
TOURNAMENT_LIST = []
MENU_TOURNAMENT_CREATION = 1
MENU_TOURNAMENT_DISPLAY = 2
MENU_TOURNAMENT_START = 3
MENU_TOURNAMENT_RECOVERY = 4
MENU_TOURNAMENT_EXIT = 5


class TournamentView:
    """ Tournament class """

    def __init__(self):
        self.tournaments = None
        self.question = None

    def tournament_menu(self):
        """ Menu 1 """
        choix = None
        while choix != MENU_TOURNAMENT_CREATION and choix != MENU_TOURNAMENT_DISPLAY and choix != MENU_TOURNAMENT_START\
                and choix != MENU_TOURNAMENT_RECOVERY and choix != MENU_TOURNAMENT_EXIT:
            self.clear_screen()
            print("+-------------------------------+")
            print("|         MENU TOURNOI          |")
            print("+-------------------------------+")
            print("| 1 - création d'un tournoi     |")
            print("| 2 - affichage des tournois    |")
            print("| 3 - démarrer nouveau tournoi  |")
            print("| 4 - reprise d'un tournoi      |")
            print("| 5 - revenir au menu principal |")
            print("+-------------------------------+")
            choix = input("Quel est votre choix : ")
            if not choix.isnumeric():
                print("Merci de préciser un choix numérique.")
                choix = None
            else:
                choix = int(choix)
        return choix

    def add_tournament_menu(self):
        self.clear_screen()
        new_one_tournament = " "
        TOURNAMENT_LIST.clear()

        while new_one_tournament.upper() != "N":

            """ Requests for tournament name """
            tournament_name = None
            while not tournament_name:
                tournament_name = input("Nom du tournoi : ")

            """ Requests for tournament name """
            tournament_town = None
            while not tournament_town:
                tournament_town = input("Lieu du tournoi : ")
                if any(chr.isdigit() for chr in tournament_town) is True:
                    print("La ville ne peut contenir de chiffre. Merci de ressaisir.")
                    tournament_town = ""

            """ Requests for number of rounds """
            tournament_nb_round = None
            while not tournament_nb_round:
                while True:
                    tournament_nb_round = input("Nombre de tour : ")
                    if str(tournament_nb_round).isalpha():
                        print("Valeur uniquement numérique. Ressaisir le nombre de tour.")
                    else:
                        break

            """ Requests for description of the tournament """
            tournament_description = input("Description du tournoi ([ENTRER pour laisser vide) : ")
            if not tournament_description:
                tournament_description = "Juste une description de test"     # juste pour debugging, à supprimer

            TOURNAMENT_LIST.append([tournament_name, tournament_town, tournament_nb_round, tournament_description])

            new_one_tournament = input("Créer un autre tournoi (O/n)?")

        return TOURNAMENT_LIST

    @staticmethod
    def display_tournament():
        """ method to display tournament(s) """
        dis_tournament_menu = ""
        while dis_tournament_menu.upper() != "T" and dis_tournament_menu.upper() != "C" and\
                dis_tournament_menu.upper() != "N":
            while True:
                dis_tournament_menu = input("Afficher tournois (t)erminés, en (c)ours, (n)on commencé ou"
                                            " tous[ENTER] ? ")
                if not dis_tournament_menu:
                    return "display_all_tournaments"
                elif dis_tournament_menu == "t":
                    return "display_completed_tournaments"
                elif dis_tournament_menu == "n":
                    return "display_not_started_tournaments"
                elif dis_tournament_menu == "c":
                    return "display_current_tournaments"

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

    def select_menu(self, tournaments):
        """ method to select tournament """
        self.tournaments = tournaments
        choice = ""
        while not choice.isnumeric():
            choice = input("Choisir un tournoi (renseigner un chiffre) : ")
            if not choice.isnumeric():
                print("Merci de saisir un chiffre.")
            elif int(choice) > len(self.tournaments):
                print("Choix incorrect, merci de ressaisir.")
                choice = ""
            elif int(choice) <= 0:
                print("Choix incorrect, merci de ressaisir.")
                choice = ""
            elif choice.isnumeric():
                return choice

    @staticmethod
    def display_all_tournaments():
        """ method to display all tournaments and select one """
        pass

    @staticmethod
    def clear_screen():
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system('cls')
