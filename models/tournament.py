from tinydb import TinyDB, Query
from tinydb.operations import add
import uuid
import os
import datetime
import unidecode
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data", "tournaments")
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
    with open(os.path.join(DATA_FOLDER, "tournaments.json"), 'w') as tournaments_file:
        pass
    tournaments_file.close()
DB = TinyDB('data/tournaments/tournaments.json')
TOURNAMENTS_DB = DB.table('tournaments')
TOURNAMENT = Query()


class TournamentModel:
    """Tournament class """
    tournament_start_date = None
    tournament_end_date = None
    tournament_current_round = None
    tournament_list_rounds = None
    tournament_list_players = None
    tournament_list_matchs = ""

    def __init__(self, tournament_uuid="", tournament_name="", tournament_town="", tournament_nb_round="",
                 tournament_description=""):
        """ Init tournament """
        self.tournament_uuid = tournament_uuid
        self.tournament_name = tournament_name
        self.tournament_town = tournament_town
        self.tournament_nb_round = tournament_nb_round
        self.tournament_description = tournament_description

    def __str__(self):
        return f"Tournoi {self.tournament_name} se déroulant à {self.tournament_town} et comportant" \
               f" {self.tournament_nb_round} round(s)."

    def save_tournament(self):
        """ method to save tournament in json file """
        tournament_uuid = str(uuid.uuid1())
        tournament_name = self.tournament_name
        tournament_town = self.tournament_town
        tournament_start_date = self.tournament_start_date
        tournament_end_date = self.tournament_end_date
        tournament_nb_round = self.tournament_nb_round
        tournament_current_round = self.tournament_current_round
        tournament_list_rounds = self.tournament_list_rounds
        tournament_list_players = self.tournament_list_players
        tournament_list_matchs = self.tournament_list_matchs
        tournament_description = self.tournament_description
        TOURNAMENTS_DB.insert({'tournament_uuid': tournament_uuid, 'name': unidecode.unidecode(tournament_name),
                               'town': unidecode.unidecode(tournament_town), 'start_date': tournament_start_date,
                               'end_date': tournament_end_date, 'nb_round': int(tournament_nb_round),
                               'current_round': tournament_current_round, 'list_rounds': tournament_list_rounds,
                               'list_players': tournament_list_players, 'list_matchs': tournament_list_matchs,
                               'description': unidecode.unidecode(tournament_description)})

    @staticmethod
    def search_all_tournaments():
        """ method to select all tournaments and record in a list """
        try:
            result_doc = TOURNAMENTS_DB.search(TOURNAMENT.name.matches('[aZ]*'))
        except ValueError:
            return "error"
        if len(result_doc) == 0:
            return "no_result"
        tournaments = []
        for doc in result_doc:
            tournament = TournamentModel()
            tournament.tournament_uuid = doc['tournament_uuid']
            tournament.tournament_name = doc['name']
            tournament.tournament_town = doc['town']
            tournament.tournament_start_date = doc['start_date']
            tournament.tournament_end_date = doc['end_date']
            tournament.tournament_nb_round = doc['nb_round']
            tournament.tournament_current_round = doc['current_round']
            tournament.tournament_list_rounds = doc['list_rounds']
            tournament.tournament_list_players = doc['list_players']
            tournament.tournament_list_matchs = doc['list_matchs']
            tournament.tournament_description = doc['description']
            tournaments.append(tournament)
        return tournaments

    @staticmethod
    def search_completed_tournaments():
        """ method to select tournaments where nb_round = current round """
        try:
            result_doc = TOURNAMENTS_DB.search(TOURNAMENT.name.matches('[aZ]*'))
        except ValueError:
            return "error"
        completed_tournaments = []
        for doc in result_doc:
            tournament = TournamentModel()
            tournament.tournament_nb_round = doc['nb_round']
            tournament.tournament_current_round = doc['current_round']
            if tournament.tournament_nb_round == tournament.tournament_current_round:
                tournament.tournament_uuid = doc['tournament_uuid']
                tournament.tournament_name = doc['name']
                tournament.tournament_town = doc['town']
                tournament.tournament_start_date = doc['start_date']
                tournament.tournament_end_date = doc['end_date']
                tournament.tournament_nb_round = doc['nb_round']
                tournament.tournament_current_round = doc['current_round']
                tournament.tournament_list_rounds = doc['list_rounds']
                tournament.tournament_list_players = doc['list_players']
                tournament.tournament_list_matchs = doc['list_matchs']
                tournament.tournament_description = doc['description']
                completed_tournaments.append(tournament)
        if not completed_tournaments:
            return "no_result"
        return completed_tournaments

    @staticmethod
    def search_current_tournaments():
        """ method to select tournaments where nb_round != current_round """
        try:
            result_doc = TOURNAMENTS_DB.search(TOURNAMENT.name.matches('[aZ]*'))
        except ValueError:
            return "error"
        current_tournaments = []
        for doc in result_doc:
            tournament = TournamentModel()
            tournament.tournament_nb_round = doc['nb_round']
            tournament.tournament_current_round = doc['current_round']
            if tournament.tournament_nb_round != tournament.tournament_current_round and\
                    tournament.tournament_current_round is not None:
                tournament.tournament_uuid = doc['tournament_uuid']
                tournament.tournament_name = doc['name']
                tournament.tournament_town = doc['town']
                tournament.tournament_start_date = doc['start_date']
                tournament.tournament_end_date = doc['end_date']
                tournament.tournament_list_rounds = doc['list_rounds']
                tournament.tournament_list_players = doc['list_players']
                tournament.tournament_list_matchs = doc['list_matchs']
                tournament.tournament_description = doc['description']
                current_tournaments.append(tournament)
        if not current_tournaments:
            return "no_result"
        else:
            return current_tournaments

    @staticmethod
    def search_not_started_tournaments():
        """ method to select tournaments where nb_round # current round """
        try:
            result_doc = TOURNAMENTS_DB.search(TOURNAMENT.name.matches('[aZ]*'))
        except ValueError:
            return "error"
        not_started_tournaments = []
        for doc in result_doc:
            tournament = TournamentModel()
            tournament.tournament_nb_round = doc['nb_round']
            tournament.tournament_current_round = doc['current_round']
            if not tournament.tournament_current_round:
                tournament.tournament_name = doc['name']
                tournament.tournament_town = doc['town']
                tournament.tournament_current_round = doc['nb_round']
                tournament.tournament_uuid = doc['tournament_uuid']
                not_started_tournaments.append(tournament)
        if not not_started_tournaments:
            return "no_result"
        else:
            return not_started_tournaments

    def search_nb_round_for_tournament(self):
        """ method to search nb_round for a tournament object """
        return self.tournament_nb_round

    def store_players(self, players_uuids):
        """ method to add player's uuid to tournaments.json """
        players_uuid_list = []
        for player_uuid in players_uuids:
            players_uuid_list.append(player_uuid)
        TOURNAMENTS_DB.update({'list_players': players_uuid_list}, TOURNAMENT.tournament_uuid
                              == self.tournament_uuid)

    def extract_players_uuid_of_tournament(self):
        """ method to extract all player's uuid of a tournament """
        tournament = TOURNAMENTS_DB.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))
        players_uuid_list = tournament[0]['list_players']
        return players_uuid_list

    def extract_matchs_uuid_list_of_tournament(self):
        """ method to extract all match's ids of a tournament """
        result_doc = TOURNAMENTS_DB.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))
        matchs_id_list = result_doc[0]['list_matchs']
        return matchs_id_list

    # def extract_tournament_name(self, tournament):
    #     """ method to extract tournament's name of a tournament with tournament uuid """
    #     self.tournament_uuid = tournament.tournament_uuid
    #     tournament = TOURNAMENTS_DB.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))
    #     tournament_name = tournament[0]['name']
    #     return tournament_name

    def extract_all_infos_tournaments(self):
        """ method to extract all infos of a tournament with the uuid's tournament """
        return self.tournament_name, self.tournament_town, self.tournament_start_date,\
            self.tournament_end_date, self.tournament_nb_round, self.tournament_current_round,\
            self.tournament_list_matchs, self.tournament_list_players, self.tournament_description

    def store_tournament_start_date(self, tournament_start_date):
        """ method to store start date in tournament """
        TOURNAMENTS_DB.update({'start_date': tournament_start_date},
                              TOURNAMENT.tournament_uuid == self.tournament_uuid)

    def store_tournament_end_date(self, tournament_end_date):
        """ method to store end date in tournament """
        TOURNAMENTS_DB.update({'end_date': tournament_end_date}, TOURNAMENT.tournament_uuid == self.tournament_uuid)

    def store_match_id(self, match_id_list):
        """ method to store matchs id in tournament """
        is_list_matchs = TOURNAMENTS_DB.search(
            TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))[0]['list_matchs']
        if is_list_matchs:
            TOURNAMENTS_DB.update(add('list_matchs', match_id_list), Query().tournament_uuid == self.tournament_uuid)
        else:
            TOURNAMENTS_DB.update({'list_matchs': match_id_list}, TOURNAMENT.tournament_uuid == self.tournament_uuid)

    def store_current_round(self, tournament_current_round):
        """ method to store current_round number in tournaments.json"""
        TOURNAMENTS_DB.update({'current_round': int(tournament_current_round)},
                              TOURNAMENT.tournament_uuid == self.tournament_uuid)

    def store_round_date(self, current_round, round_start_date, round_end_date):
        """ method to store start and end dates for a round """
        all_rounds = TOURNAMENTS_DB.search(
            TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))[0]['list_rounds']
        round = ["Round" + str(current_round), str(round_start_date), str(round_end_date)]
        if all_rounds is None:
            all_rounds = [round]
        else:
            all_rounds.append(round)
        TOURNAMENTS_DB.update({'list_rounds': all_rounds}, TOURNAMENT.tournament_uuid == self.tournament_uuid)

    def extract_start_date_tournament(self):
        """ method to extract start date of a tournament object """
        return self.tournament_start_date

    def extract_end_date_tournament(self):
        """ method to extract start date of a tournament object """
        return self.tournament_end_date

    # def extract_rounds_list(self, tournament):
    #     """ method to extract all rounds details of a tournament"""
    #     self.tournament_uuid = tournament.tournament_uuid
    #     tournament = TOURNAMENTS_DB.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))
    #     rounds_list = tournament[0]['list_rounds']
    #     return rounds_list

    @staticmethod
    def export_tournament(tournaments_scores, detailed_rounds_list, tournament_start_date, tournament_end_date,
                          tournament_name, players_scores):
        rounds_list = tournaments_scores[0]
        matchs_list = tournaments_scores[1]
        p1names_list = tournaments_scores[2]
        p2names_list = tournaments_scores[3]
        p1scores_list = tournaments_scores[4]
        p2scores_list = tournaments_scores[5]
        round_max = tournaments_scores[6]
        index = 0
        """ method to export in html file a tournament """
        data_folder = os.path.join(os.path.dirname(__file__), "..", "data", "reports")
        file_name = "Tournoi " + tournament_name + " " + datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S')\
                    + ".html"
        with open(os.path.join(data_folder, file_name), 'w') as report_file:
            report_file.write('<style type="text/css">')
            report_file.write('.tg  {border-collapse:collapse;border-spacing:0}')
            report_file.write('.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial,'
                              ' sans-serif;')
            report_file.write('  overflow:hidden;padding:10px 5px;word-break:normal;}')
            report_file.write('.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial,'
                              ' sans-serif;')
            report_file.write('  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}')
            report_file.write('.tg .tg-33h5{background-color:#3166ff;border-color:#000000;color:#ffffff;'
                              'text-align:center;font-size:20px;vertical-align:top}')
            report_file.write('.tg .tg-2uuq{background-color:#ffcb2f;border-color:#000000;text-align:center;'
                              'font-size:16px;vertical-align:top}')
            report_file.write('.tg .tg-73oq{border-color:#000000;text-align:left;font-size:14px;vertical-align:top}')
            report_file.write('</style>')
            report_file.write('<table class="tg">')
            report_file.write("  <tr>")
            report_file.write('    <th class="tg-33h5" colspan="3">Tournoi ' + str(tournament_name) + ' du '
                              + str(tournament_start_date) + ' au ' + str(tournament_end_date) + '</th>')
            report_file.write('  </tr>')
            report_file.write('  <tr>')
            for round_nb in range(1, int(round_max)+1):
                round_start = detailed_rounds_list[round_nb - 1][1]
                round_end = detailed_rounds_list[round_nb - 1][2]
                report_file.write('    <td class="tg-2uuq" colspan="3">Round ' + str(round_nb) + ' du '
                                  + str(round_start) + ' au ' + str(round_end) + '</td>')
                report_file.write('  </tr>')
                report_file.write('  <tr>')
                for round in rounds_list:
                    if int(round) == round_nb:
                        match = matchs_list[index]
                        p1name = (p1names_list[index])
                        p2name = (p2names_list[index])
                        p1score = p1scores_list[index]
                        p2score = p2scores_list[index]
                        report_file.write('<td class="tg-73oq" colspan="1">Match ' + str(match) + '</td>')
                        report_file.write('<td class="tg-73oq" colspan="1">' + str(p1name) + ' : '
                                          + str(p1score) + '</td>')
                        report_file.write('<td class="tg-73oq" colspan="1">' + str(p2name) + ' : '
                                          + str(p2score) + '</td>')
                        report_file.write('  </tr>')
                        report_file.write('  <tr>')
                        index += 1
            report_file.write('    <td class="tg-2uuq" colspan="3">Résultats (triés par scores)</td>')
            report_file.write('  </tr>')
            report_file.write('  <tr>')
            result = '    <td class="tg-73oq" colspan="3">'
            for i in range(len(players_scores[0])):
                result = result + str(players_scores[0][i] + ' - score : ' + str(players_scores[1][i]) + '<br>')
            report_file.write(result)
        report_file.close()
        return 'Le fichier "' + file_name + '" à été exporté\ndans le dossier '\
            + data_folder.replace("models\\..\\", "") + '\\.'
