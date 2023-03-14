from controllers.tournament import TournamentController
from views.report import ReportView
from views.tournament import TournamentView
from models.tournament import TournamentModel
from models.player import PlayerModel
import sys
from constantes import MENU_REPORT_TOURNAMENT_PLAYERS, MENU_REPORT_TOURNAMENT_SCORES, MENU_REPORT_PLAYER_NAME,\
    MENU_REPORT_PLAYER_FNAME, MENU_RESULT_TOURNAMENT_LIST, MENU_RESULT_TOURNAMENT_DETAIL, MENU_REPORT_EXIT,\
    MENU_REPORT_EXPORT_HTML


class ReportController:
    """ reports class """
    def __init__(self):
        self.tournament_controller = TournamentController()
        self.report_view = ReportView()
        self.tournament_view = TournamentView()

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
            elif choix == MENU_REPORT_EXPORT_HTML:
                self.report_tournament("html_file")
            elif choix == MENU_REPORT_EXIT:
                break

    def report_tournament_details(self):
        """ method to display detail of a tournament """
        player_fname_name_list = []
        tournaments = TournamentModel.search_all_tournaments()
        while True:
            if tournaments == "no_result":
                self.report_view.choice("Aucun tournoi. Appuyez sur [ENTRER] pour revenir au menu et en créer.")
                break
            elif tournaments == "error":
                self.report_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                               " le et recommencez.")
                sys.exit()
            else:
                index = 0
                for tournament in tournaments:
                    index += 1
                    self.report_view.text_to_print(str(index) + " - " + str(tournament))
                # select a tournament
                choix = self.tournament_view.select(tournaments)
                tournament = tournaments[int(choix) - 1]
                # tournament = tournament.extract_all_infos_tournaments()
                ReportView.display_tournament_details(tournament)

                # display ordered player list of a tournament
                player_fname_name_list = []
                if tournament.tournament_list_players:
                    for player_uuid in tournament.tournament_list_players:
                        player = PlayerModel.create_player_object(player_uuid)
                        player_fname_name_list.append(player.extract_player_fname_and_name())
                    player_fname_name_list.sort()
                    self.report_view.text_to_print(
                        "La liste des joueurs (triée par ordre alphabétique) est la suivante :")
                    for player in player_fname_name_list:
                        self.report_view.text_to_print("- " + player)
                choix = self.report_view.choice("Faire une autre recherche (O/n)? ")
                if choix.upper() == "N":
                    break

    def report_tournament_list(self):
        """ method to display list of tournaments """
        self.tournament_controller.display_tournament()

    def report_players_name(self, by_name, by_fname):
        """ method to display all players in alphabetic order """
        while True:
            if PlayerModel.search_all_players() == "no_result":
                self.report_view.choice("Aucun joueurs. Appuyez sur [ENTRER] pour revenir au menu et en créer.")
                break
            elif PlayerModel.search_all_players() == "error":
                self.report_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                               " le et recommencez.")
                sys.exit()
            else:
                players_list = PlayerModel.search_all_players(by_name, by_fname)
                for player in players_list:
                    self.report_view.text_to_print(player)
                self.report_view.choice("Appuyez sur [ENTRER] pour revenir au menu.")
                break

    def report_tournament(self, display_type=None):
        """ method to display tournament report """
        while True:
            if TournamentModel.search_all_tournaments() == "no_result":
                self.report_view.choice("Aucun tournoi. Appuyez sur [ENTRER] pour revenir au menu et en créer.")
                break
            elif TournamentModel.search_all_tournaments() == "error":
                self.report_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                               " le et recommencez.")
                sys.exit()
            else:
                # display ended tournaments
                ended_tournaments = TournamentModel.search_completed_tournaments()
                self.report_view.text_to_print("Liste des tournois terminés:")
                index = 0
                for tournament in ended_tournaments:
                    index += 1
                    self.report_view.text_to_print(str(index) + " - " + str(tournament))

                # select a tournament
                choix = self.tournament_view.select(ended_tournaments)
                tournament = ended_tournaments[int(choix) - 1]

                # extraction of all matchs associated to selected tournament
                # matchs_ids_list = tournament.extract_matchs_id_list()

                # extract all players and scores from matchs id list
                players_uuid_list, players_scores = tournament.extract_players_scores()

                # reinit scores in players.json
                PlayerModel.delete_score_player(players_uuid_list)

                # store scores in players.json for create ordered winners
                for player_uuid, player_score in zip(players_uuid_list, players_scores):
                    PlayerModel.store_score(player_uuid, player_score)

                # create tuple contains players fname & name + scores
                players_uuid_list = list(set(players_uuid_list))
                players_uuid = []
                players = []
                scores = []
                for player_uuid in players_uuid_list:
                    score = PlayerModel.search_player_score(player_uuid)
                    players_uuid.append(player_uuid)
                    scores.append(score)
                scores, players_uuid = zip(*sorted(zip(scores, players_uuid), reverse=True))
                for player_uuid in players_uuid:
                    player = PlayerModel.create_player_object(player_uuid)
                    player_fname_name = player.extract_player_fname_and_name()
                    players.append(player_fname_name)
                players_scores = [players, scores]

                # extraction of all rounds details
                rounds_list = tournament.tournament_list_rounds

                # extraction of start and end dates of a tournament
                tournament_start_date = tournament.tournament_start_date
                tournament_end_date = tournament.tournament_end_date

                # extraction of all scores of matchs list associated to the selected tournament
                tournaments_scores = TournamentModel.extract_scores(tournament)
                if display_type == "players":
                    self.report_view.display_scores_players(tournaments_scores, rounds_list, tournament_start_date,
                                                            tournament_end_date, tournament.tournament_name,
                                                            players_scores)
                elif display_type == "scores":
                    self.report_view.display_scores_scores(tournaments_scores, rounds_list, tournament_start_date,
                                                           tournament_end_date, tournament.tournament_name,
                                                           players_scores)
                elif display_type == "html_file":
                    result = TournamentModel.export_tournament(tournaments_scores, rounds_list, tournament_start_date,
                                                               tournament_end_date, tournament.tournament_name,
                                                               players_scores)
                    self.report_view.text_to_print(result)
                    self.report_view.choice("Appuyez sur [ENTRER] pour continuer.")
                break
