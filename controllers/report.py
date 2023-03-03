from controllers.tournament import TournamentController
from views.report import ReportView
from views.tournament import TournamentView
from models.tournament import TournamentModel
from models.match import MatchModel
from models.player import PlayerModel
from constantes import MENU_REPORT_TOURNAMENT_PLAYERS, MENU_REPORT_TOURNAMENT_SCORES, MENU_REPORT_PLAYER_NAME,\
    MENU_REPORT_PLAYER_FNAME, MENU_RESULT_TOURNAMENT_LIST, MENU_RESULT_TOURNAMENT_DETAIL, MENU_REPORT_EXIT


class ReportController:
    """ reports class """
    def __init__(self):
        self.by_fname = None
        self.by_name = None
        self.tournament_controller = TournamentController()
        self.report_view = ReportView()
        self.tournament_view = TournamentView()
        self.tournament_model = TournamentModel()
        self.match_model = MatchModel()
        self.player_model = PlayerModel()

    def menu_report(self):
        """ Reports menu """
        while True:
            choix = self.report_view.report_menu()
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

    def report_tournament_details(self, ):
        """ method to display detail of a tournament """
        player_fname_name_list = []
        tournaments = self.tournament_model.search_all_tournaments()
        while True:
            if tournaments == "no_result":
                self.report_view.choice_menu("Aucun tournoi. Appuyez sur [ENTRER] pour revenir au menu et en créer.")
                break
            else:
                for i in range(len(tournaments)):
                    item = tournaments[i]
                    print(str(i + 1) + " - "
                          + str(TournamentModel(item['name'], item['town'], item['nb_round'])))

                # select a tournament
                choix = self.tournament_view.select_menu(tournaments)
                selected_tournament = tournaments[int(choix) - 1]
                tournament_uuid = selected_tournament['tournament_uuid']
                tournament_infos = self.tournament_model.extract_all_infos_tournaments(tournament_uuid)
                self.report_view.display_tournament_details(tournament_infos)
                # display ordered player list of a tournament
                if tournament_infos[7]:
                    for player_uuid in tournament_infos[7]:
                        player_fname_name_list.append(self.player_model.extract_player_fname_and_name(player_uuid))
                    player_fname_name_list.sort()
                    print("La liste des joueurs (triée par ordre alphabétique) est la suivante :")
                    for player in player_fname_name_list:
                        print("- " + player)
                self.report_view.choice_menu("Appuyez sur [ENTRER] pour revenir au menu.")
                break

    def report_tournament_list(self):
        """ method to display list of tournaments """
        self.tournament_controller.display_tournament()

    def report_players_name(self, by_name, by_fname):
        """ method to display all players in alphabetic order """
        self.by_name = by_name
        self.by_fname = by_fname
        while True:
            if self.player_model.search_all_players("", "") == "no_result":
                self.report_view.choice_menu("Aucun joueurs. Appuyez sur [ENTRER] pour revenir au menu et en créer.")
                break
            else:
                self.by_name = by_name
                self.by_fname = by_fname
                players_uuid_list = self.player_model.search_all_players(self.by_name, self.by_fname)
                players_list = self.player_model.extract_data_player(players_uuid_list)
                for player in players_list:
                    print(PlayerModel(player[0], player[1], player[2], player[3]))
                self.report_view.choice_menu("Appuyez sur [ENTRER] pour revenir au menu.")
                break

    def report_tournament(self, display_type=None):
        """ method to display tournament report """
        while True:
            if self.tournament_model.search_all_tournaments() == "no_result":
                self.report_view.choice_menu("Aucun tournoi. Appuyez sur [ENTRER] pour revenir au menu et en créer.")
                break
            else:
                # display ended tournaments
                ended_tournaments = self.tournament_model.search_completed_tournaments()
                print("Liste des tournois terminés:")
                for i in range(len(ended_tournaments)):
                    item = ended_tournaments[i]
                    print(str(i + 1) + " - " + str(TournamentModel(item['name'], item['town'], item['nb_round'])))

                # select a tournament
                choix = self.tournament_view.select_menu(ended_tournaments)
                selected_tournament = ended_tournaments[int(choix) - 1]
                selected_tournament_uuid = selected_tournament['tournament_uuid']

                # extraction of all matchs associated to selected tournament
                matchs_ids_list = self.tournament_model.extract_matchs_uuid_list_of_tournament(
                    selected_tournament_uuid)

                # extract all players and scores from matchs id list
                players_uuid_list, players_scores = self.match_model.extract_players_scores(matchs_ids_list)

                # reinit scores in players.json
                self.player_model.delete_score_player(players_uuid_list)

                # store scores in players.json for create ordered winners
                for player_uuid, player_score in zip(players_uuid_list, players_scores):
                    self.player_model.store_score(player_uuid, player_score)

                # create tuple contains players names + scores
                players_uuid_list = list(set(players_uuid_list))

                # create [(fname + name), score] list
                players = []
                scores = []
                for player_uuid in players_uuid_list:
                    player = self.player_model.extract_player_fname_and_name(player_uuid)
                    score = self.player_model.search_player_score(player_uuid)
                    players.append(player)
                    scores.append(score)
                scores, players = zip(*sorted(zip(scores, players), reverse=True))
                players_scores = [players, scores]

                # extraction of all rounds details
                rounds_list = self.tournament_model.extract_rounds_list(selected_tournament_uuid)

                # extraction of start and end dates of a tournament
                tournament_start_date =\
                    self.tournament_model.extract_all_infos_tournaments(selected_tournament_uuid)[2]
                tournament_end_date = self.tournament_model.extract_all_infos_tournaments(selected_tournament_uuid)[3]

                # extraction of all scores of matchs list associated to the selected tournament
                tournaments_scores = self.match_model.extract_scores(matchs_ids_list)
                tournament_name = self.tournament_model.extract_tournament_name(selected_tournament_uuid)
                if display_type == "players":
                    self.report_view.display_scores_players(tournaments_scores, rounds_list, tournament_start_date,
                                                            tournament_end_date, tournament_name, players_scores)
                elif display_type == "scores":
                    self.report_view.display_scores_scores(tournaments_scores, rounds_list, tournament_start_date,
                                                           tournament_end_date, tournament_name, players_scores)
                break
