from controllers.tournament import TournamentController
from views.report import ReportView
from views.tournament import TournamentView
from models.tournament import TournamentModel
from models.match import MatchModel
from models.player import PlayerModel
MENU_REPORT_TOURNAMENT_PLAYERS = 1
MENU_REPORT_TOURNAMENT_SCORES = 2
MENU_REPORT_PLAYER_NAME = 3
MENU_REPORT_PLAYER_FNAME = 4
MENU_RESULT_TOURNAMENT_LIST = 5
MENU_RESULT_TOURNAMENT_DETAIL = 6
MENU_REPORT_EXIT = 7
RESULT_DISPLAY = None


class ReportController:
    """ reports class """

    def __init__(self):
        self.by_fname = None
        self.by_name = None

    def menu_3(self):
        """ Reports menu """
        while True:
            choix = ReportView().report_menu()
            if choix == MENU_REPORT_TOURNAMENT_PLAYERS:
                self.report_tournament("players")
            elif choix == MENU_REPORT_TOURNAMENT_SCORES:
                self.report_tournament("scores")
            elif choix == MENU_REPORT_PLAYER_NAME:
                self.report_players_name(by_name=True, by_fname=False)
            elif choix == MENU_REPORT_PLAYER_FNAME:
                self.report_players_name(by_name=False, by_fname=True)
            elif choix == MENU_RESULT_TOURNAMENT_LIST:
                self.report_tournament_list()
            elif choix == MENU_RESULT_TOURNAMENT_DETAIL:
                self.report_tournament_details()
            elif choix == MENU_REPORT_EXIT:
                break

    @staticmethod
    def report_tournament_details():
        """ method to display detail of a tournament """
        tournaments = TournamentModel.search_all_tournaments()
        while True:
            if tournaments == "no_result":
                ReportView().choice_menu("Aucun tournoi. Appuyez sur [ENTRER]"
                                         " pour revenir au menu et en créer.")
                break
            else:
                for i in range(len(tournaments)):
                    item = tournaments[i]
                    print(str(i + 1) + " - "
                          + str(TournamentModel(item['name'], item['town'],
                                                item['nb_round'])))

                """ select a tournament """
                choix = TournamentView().select_menu(tournaments)
                selected_tournament = tournaments[int(choix) - 1]
                tournament_uuid = selected_tournament['tournament_uuid']
                result =\
                    TournamentModel().extract_all_infos_tournaments(
                        tournament_uuid)
                print(f"Tournoi {result[0]} se déroulant à {result[1]} et"
                      f" comportant"
                      f" {result[4]} round(s).")
                print(f"Description : {result[8]}.")
                if result[2] and result[3]:
                    print(f"Ce tournoi a démarré le {result[2]} et s'est"
                          f" terminé le {result[3]}.")
                elif result[2] and not result[3]:
                    print(f"Ce tournoi a démarré le {result[2]} mais n'est"
                          f" pas terminé, {result[5]} round(s) sur"
                          f" {result[4]} ont étés joués.")
                elif not result[2]:
                    print(f"Ce tournoi n'a pas encore démarré.")
                if result[2]:
                    print(f"Il y'a eu " + str(len(result[6]))
                          + " matchs joué(s).")
                if result[7]:
                    print("La liste des joueurs est la suivante :")
                    for player_uuid in result[7]:
                        print("- "
                              + PlayerModel()
                              .extract_player_fname_and_name(player_uuid))
                ReportView().choice_menu("Appuyez sur [ENTRER] pour revenir"
                                         " au menu.")

    @staticmethod
    def report_tournament_list():
        """ method to display list of tournaments """
        TournamentController().display_tournament()

    def report_players_name(self, by_name, by_fname):
        """ method to display all players in alphabetic order """
        while True:
            if PlayerModel().search_all_players("", "") == "no_result":
                ReportView().choice_menu(
                         "Aucun joueurs. Appuyez sur [ENTRER] pour revenir"
                         " au menu et en créer.")
                break
            else:
                self.by_name = by_name
                self.by_fname = by_fname
                players_uuid_list = PlayerModel().\
                    search_all_players(self.by_name, self.by_fname)
                players_list = PlayerModel().extract_data_player(
                    players_uuid_list)
                for player in players_list:
                    print(PlayerModel(player[0], player[1], player[2],
                                      player[3]))
                ReportView().choice_menu("Appuyez sur [ENTRER] pour revenir"
                                         " au menu.")
                break

    @staticmethod
    def report_tournament(display_type=None):
        """ method to display tournament report """
        while True:
            if TournamentModel.search_all_tournaments() == "no_result":
                ReportView().choice_menu(
                         "Aucun tournoi. Appuyez sur [ENTRER] pour revenir"
                         " au menu et en créer.")
                break
            else:
                """ display ended tournaments """
                ended_tournaments = TournamentModel().\
                    search_completed_tournaments()
                print("Liste des tournois terminés:")
                for i in range(len(ended_tournaments)):
                    item = ended_tournaments[i]
                    print(str(i + 1) + " - " + str(
                        TournamentModel(item['name'], item['town'],
                                        item['nb_round'])))

                """ select a tournament """
                choix = TournamentView().select_menu(ended_tournaments)
                selected_tournament = ended_tournaments[int(choix) - 1]
                selected_tournament_uuid = \
                    selected_tournament['tournament_uuid']

                """ extraction of all matchs associated to selected
                 tournament """
                matchs_ids_list = TournamentModel()\
                    .extract_matchs_uuid_list_of_tournament(
                    selected_tournament_uuid)

                """ extraction of all scores of matchs list associated to the
                 selected tournament """
                tournaments_scores = MatchModel().extract_scores(
                    matchs_ids_list)
                tournament_name =\
                    TournamentModel().extract_tournament_name(
                        selected_tournament_uuid)
                if display_type == "players":
                    ReportView().display_scores_players(tournaments_scores,
                                                        tournament_name)
                elif display_type == "scores":
                    ReportView().display_scores_scores(tournaments_scores,
                                                       tournament_name)
