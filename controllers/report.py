from views.report import ReportView
from views.tournament import TournamentView
from models.tournament import TournamentModel
from models.match import MatchModel
MENU_REPORT_TOURNAMENT_PLAYERS = 1
MENU_REPORT_TOURNAMENT_SCORES = 2
MENU_REPORT_PLAYER = 3
MENU_REPORT_EXIT = 4
RESULT_DISPLAY = None


class ReportController:
    """ reports class """
    def menu_3(self):
        """ Reports menu """
        while True:
            choix = ReportView().report_menu()
            if choix == MENU_REPORT_TOURNAMENT_PLAYERS:
                self.report_tournament("players")
            elif choix == MENU_REPORT_TOURNAMENT_SCORES:
                self.report_tournament("scores")
            elif choix == MENU_REPORT_PLAYER:
                pass
            elif choix == MENU_REPORT_EXIT:
                break

    @staticmethod
    def report_tournament(display_type=None):
        """ method to display tournament report """

        """ display ended tournaments """
        ended_tournaments = TournamentModel().search_completed_tournaments()
        print("Liste des tournois terminés:")
        for i in range(len(ended_tournaments)):
            item = ended_tournaments[i]
            print(str(i + 1) + " - " + str(TournamentModel(item['name'], item['town'], item['nb_round'])))

        """ select a tournament """
        choix = TournamentView().select_menu(ended_tournaments)
        selected_tournament = ended_tournaments[int(choix) - 1]
        selected_tournament_uuid = selected_tournament['tournament_uuid']

        """ extraction of all matchs associated to selected tournament """
        matchs_ids_list = TournamentModel().extract_matchs_uuid_list_of_tournament(selected_tournament_uuid)

        """ extraction of all scores of matchs list associated to the selected tournament """
        tournaments_scores = MatchModel().extract_scores(matchs_ids_list)
        tournament_name = TournamentModel().extract_tournament_name(selected_tournament_uuid)
        if display_type == "players":
            ReportView().display_scores_players(tournaments_scores, tournament_name)
        elif display_type == "scores":
            ReportView().display_scores_scores(tournaments_scores, tournament_name)
