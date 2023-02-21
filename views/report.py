from math import floor, ceil
import os

MENU_RESULT_TOURNAMENT_PLAYERS = 1
MENU_RESULT_TOURNAMENT_SCORES = 2
MENU_RESULT_PLAYER_NAME = 3
MENU_RESULT_PLAYER_FNAME = 4
MENU_RESULT_TOURNAMENT_LIST = 5
MENU_RESULT_TOURNAMENT_DETAIL = 6
MENU_RESULT_EXIT = 7
REPORT_TABLE_WIDTH = 60
REPORT_MATCH_WIDTH = 18
REPORT_SCORE_WIDTH = REPORT_TABLE_WIDTH - REPORT_MATCH_WIDTH
PLAYER_MAX_LENGTH = 17


class ReportView:
    """ Result class """
    """
    le rapport doit afficher:
        * liste de tous les joueurs par ordre alphabétique
        * liste de tous les tournois
        * nom et dates d’un tournoi donné
        * liste des joueurs du tournoi par ordre alphabétique
        * liste de tous les tours du tournoi et de tous les matchs du tour
    """

    def __init__(self):
        self.question = None
        self.tournament_name = None
        self.tournaments_scores = None

    def report_menu(self):
        """ Menu 3 """
        choix = None
        while choix != MENU_RESULT_TOURNAMENT_PLAYERS and choix !=\
                MENU_RESULT_PLAYER_NAME and choix !=\
                MENU_RESULT_EXIT and choix !=\
                MENU_RESULT_TOURNAMENT_SCORES and choix != \
                MENU_RESULT_PLAYER_FNAME and choix !=\
                MENU_RESULT_TOURNAMENT_LIST and choix != \
                MENU_RESULT_TOURNAMENT_DETAIL:
            self.clear_screen()
            print("+-------------------------------+")
            print("|       MENU RAPPORTS           |")
            print("+-------------------------------+")
            print("| 1 - score d'un tournoi/joueurs|")
            print("| 2 - score d'un tournoi/score  |")
            print("| 3 - liste des joueurs/nom     |")
            print("| 4 - list des joueurs/prénom   |")
            print("| 5 - liste des tournois        |")
            print("| 6 - détail d'un tournoi       |")
            print("| 7 - revenir au menu principal |")
            print("+-------------------------------+")
            choix = input("Quel est votre choix : ")
            if not choix.isnumeric():
                print("Merci de préciser un choix numérique.")
                choix = None
            else:
                choix = int(choix)
        return choix

    def display_scores_players(self, tournaments_scores, tournament_name):
        """
        method to display all scores for one tournament
        displayed with names details
        """
        self.clear_screen()
        """ extraction/creation of attributs """
        self.tournaments_scores = tournaments_scores
        self.tournament_name = tournament_name
        rounds_list = self.tournaments_scores[0]
        matchs_list = self.tournaments_scores[1]
        p1names_list = self.tournaments_scores[2]
        p2names_list = self.tournaments_scores[3]
        p1scores_list = self.tournaments_scores[4]
        p2scores_list = self.tournaments_scores[5]
        round_max = self.tournaments_scores[6]
        index = 0

        """ print report's table (title) """
        print("+" + "=" * REPORT_TABLE_WIDTH + "+")
        blank_width = (REPORT_TABLE_WIDTH - len("Tournoi " +
                                                self.tournament_name) - 1) / 2
        print("+" + " " * floor(blank_width) + " Tournoi " +
              self.tournament_name + " " * ceil(blank_width) + "+")
        print("+" + "=" * REPORT_TABLE_WIDTH + "+")
        for round_nb in range(1, int(round_max) + 1):
            """ print title round number """
            blank_width = (REPORT_TABLE_WIDTH - len("Round " +
                                                    str(round_nb)) - 2) / 2
            print("+" + " " * floor(blank_width) + " Round  " +
                  str(round_nb) + " " * ceil(blank_width) + "+")
            print("+" + "-" * REPORT_TABLE_WIDTH + "+")
            """ print scores table """
            for round in rounds_list:
                if int(round) == round_nb:
                    match = matchs_list[index]
                    p1name = p1names_list[index]
                    p2name = p2names_list[index]
                    p1score = p1scores_list[index]
                    p2score = p2scores_list[index]
                    if p1score > p2score:
                        winner = p1name
                    elif p1score < p2score:
                        winner = p2name
                    else:
                        winner = "match nul"
                    blank_width = (REPORT_TABLE_WIDTH - len("Match " +
                                                            str(match) +
                                                            " opposant " +
                                                            str(p1name) +
                                                            " à " +
                                                            str(p2name))) / 2
                    print("+" + " " * floor(blank_width) + "Match " +
                          str(match) + " opposant " + str(p1name) +
                          " à " + str(p2name) + " " * ceil(blank_width) + "+")
                    blank_width = (REPORT_TABLE_WIDTH - len("Vainqueur : " +
                                                            str(winner))) / 2
                    print("+" + " " * floor(blank_width) + "Vainqueur : " +
                          winner + " " * ceil(blank_width) +
                          "+")
                    index += 1
            print("+" + "-" * REPORT_TABLE_WIDTH + "+")
        input("Appuyez sur [ENTRER] pour retourner au menu.")

    def display_scores_scores(self, tournaments_scores, tournament_name):
        """
        method to display all scores for one tournament
        displayed with scores details
        """
        self.clear_screen()
        """ extraction/creation of attributs """
        self.tournaments_scores = tournaments_scores
        self.tournament_name = tournament_name
        rounds_list = self.tournaments_scores[0]
        matchs_list = self.tournaments_scores[1]
        p1names_list = self.tournaments_scores[2]
        p2names_list = self.tournaments_scores[3]
        p1scores_list = self.tournaments_scores[4]
        p2scores_list = self.tournaments_scores[5]
        round_max = self.tournaments_scores[6]
        index = 0

        """ print report's table (title) """
        print("+" + "=" * REPORT_TABLE_WIDTH + "+")
        blank_width = (REPORT_TABLE_WIDTH - len("Tournoi " +
                                                self.tournament_name) - 1) / 2
        print("+" + " " * floor(blank_width) + " Tournoi " +
              self.tournament_name + " " * ceil(blank_width) + "+")
        print("+" + "=" * REPORT_TABLE_WIDTH + "+")
        for round_nb in range(1, int(round_max) + 1):
            """ print title round number """
            blank_width = (REPORT_TABLE_WIDTH - len("Round " +
                                                    str(round_nb)) - 2) / 2
            print("+" + " " * floor(blank_width) + " Round  " +
                  str(round_nb) + " " * ceil(blank_width) + "+")
            print("+" + "-" * REPORT_TABLE_WIDTH + "+")
            """ print scores table """
            for round in rounds_list:
                if int(round) == round_nb:
                    match = matchs_list[index]
                    p1name = (p1names_list[index])[:PLAYER_MAX_LENGTH]
                    p2name = (p2names_list[index])[:PLAYER_MAX_LENGTH]
                    p1score = p1scores_list[index]
                    p2score = p2scores_list[index]
                    blank_match_width = REPORT_MATCH_WIDTH -\
                    len(str(" Match ")) -\
                    len(str(match))
                    blank_score_width = (REPORT_TABLE_WIDTH -
                                         REPORT_MATCH_WIDTH -
                                         len(str(p1score)) -
                                         len(str(p2score)) - len("|+"))/3
                    p1_blank = (PLAYER_MAX_LENGTH - len(p1name))
                    p2_blank = (PLAYER_MAX_LENGTH - len(p2name))
                    print("+" + " Match " + str(match) + " " *
                          int(blank_match_width) + " | " +
                          " " * floor(p1_blank) +
                          str(p1name) + " VS " + str(p2name) +
                          " " * ceil(p2_blank) + " +")
                    if isinstance(p1score, float):
                        score_float = "+"
                    else:
                        score_float = " +"
                    print("+ Scores            | " + " " *
                          floor(blank_score_width) + str(p1score) + " "
                          * floor(blank_score_width) + str(p2score) + " " *
                          floor(blank_score_width) + str(score_float))
                    index += 1
            print("+" + "-" * REPORT_TABLE_WIDTH + "+")
        input("Appuyez sur [ENTRER] pour retourner au menu.")

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

    @staticmethod
    def clear_screen():
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system('cls')
