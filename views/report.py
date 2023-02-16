from math import *
import os

MENU_RESULT_TOURNAMENT = 1
MENU_RESULT_PLAYER = 2
MENU_RESULT_EXIT = 3
REPORT_TABLE_WIDTH = 60


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
        self.tournament_name = None
        self.tournaments_scores = None

    def report_menu(self):
        """ Menu 3 """
        choix = None
        while choix != MENU_RESULT_TOURNAMENT and choix != MENU_RESULT_PLAYER:
            self.clear_screen()
            print("+-------------------------------+")
            print("|       MENU RAPPORTS           |")
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

    def display_scores(self, tournaments_scores, tournament_name):
        """ method to display all scores for one tournament """
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
        match_max = self.tournaments_scores[7]
        match_nb = 1
        round_nb = 1
        index = 0

        """ print report's table (title) """
        print("+" + "-" * REPORT_TABLE_WIDTH + "+")
        blank_width = (REPORT_TABLE_WIDTH - len("Tournoi " + self.tournament_name) - 2) / 2
        print("+" + " " * floor(blank_width) + " Tournoi " + self.tournament_name + " " * floor(blank_width) + "+")
        print("+" + "-" * REPORT_TABLE_WIDTH + "+")
        for round_nb in range(1, int(round_max) + 1):
            """ print title round number """
            blank_width = (REPORT_TABLE_WIDTH - len("Round " + str(round_nb)) - 2) / 2
            print("+" + " " * floor(blank_width) + " Round  " + str(round_nb) + " " * ceil(blank_width) + "+")
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
                    blank_width = (REPORT_TABLE_WIDTH - len("Match " + str(match) + " opposant " + str(p1name) +
                                                            " à " + str(p2name))) / 2
                    print("+" + " " * floor(blank_width) + "Match " + str(match) + " opposant " + str(p1name) +
                          " à " + str(p2name) + " " * ceil(blank_width) + "+")
                    blank_width = (REPORT_TABLE_WIDTH - len("Vainqueur : " + str(winner))) / 2
                    print("+" + " " * floor(blank_width) + "Vainqueur : " + winner + " " * ceil(blank_width) +
                          "+")
                    index += 1
                    print("+                         ---- * ----                        +")
            print("+" + "-" * REPORT_TABLE_WIDTH + "+")
        input("Appuyez sur [ENTRER] pour retourner au menu.")

    @staticmethod
    def clear_screen():
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system('cls')
