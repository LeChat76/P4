from tinydb import TinyDB, Query
from tinydb.operations import add
import uuid
import os
import datetime
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data", "tournaments")
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
    with open(os.path.join(DATA_FOLDER, "tournaments.json"), 'w') as tournaments_file:
        pass
    tournaments_file.close()
DB = TinyDB('data/tournaments/tournaments.json')
TOURNAMENTS = DB.table('tournaments')
TOURNAMENT = Query()


class TournamentModel:
    """Tournament class """

    def __init__(self, tournament_name="", tournament_town="", tournament_nb_round="", tournament_description=""):
        """ Init tournament """
        self.rounds_list = None
        self.tournaments_scores = None
        self.players_scores = None
        self.current_round = None
        self.round_end_date = None
        self.round_start_date = None
        self.match_id_list = None
        self.tournament_uuid = None
        self.tournament_name = tournament_name
        self.tournament_town = tournament_town
        self.tournament_nb_round = tournament_nb_round
        self.tournament_start_date = None
        self.tournament_end_date = None
        self.tournament_current_round = None
        self.tournament_list_matchs = ""
        self.tournament_list_players = None
        self.tournament_description = tournament_description
        self.list_rounds = None

    def __str__(self):
        return f"Tournoi {self.tournament_name} se déroulant à {self.tournament_town} et comportant" \
               f" {self.tournament_nb_round} round(s)."

    def add_tournament(self):
        """ method for add a tournament in the json file """
        TOURNAMENTS.insert({'tournament_uuid': str(uuid.uuid1()), 'name': self.tournament_name,
                            'town': self.tournament_town, 'start_date': self.tournament_start_date,
                            'end_date': self.tournament_end_date, 'nb_round': int(self.tournament_nb_round),
                            'current_round': self.tournament_current_round, 'list_rounds': self.list_rounds,
                            'list_players': self.tournament_list_players, 'list_matchs': self.tournament_list_matchs,
                            'description': self.tournament_description})

    @staticmethod
    def search_all_tournaments():
        """ method to select all tournaments and record in a list """
        try:
            result = TOURNAMENTS.search(TOURNAMENT.name.matches('[aZ]*'))
        except ValueError:
            return "error"
        if len(result) == 0:
            return "no_result"
        return result

    @staticmethod
    def search_completed_tournaments():
        """ method to select tournaments where nb_round = current round """
        list_completed_tournament = []
        try:
            result = TOURNAMENTS.search(TOURNAMENT.name.matches('[aZ]*'))
        except ValueError:
            return "error"
        for i in range(len(result)):
            item = result[i]
            if item['nb_round'] == item['current_round']:
                list_completed_tournament.append(item)
        if not list_completed_tournament:
            return "no_result"
        return list_completed_tournament

    @staticmethod
    def search_current_tournaments():
        """ method to select tournaments where nb_round != current_round """
        list_current_tournament = []
        try:
            result = TOURNAMENTS.search(TOURNAMENT.name.matches('[aZ]*'))
        except ValueError:
            return "error"
        for i in range(len(result)):
            item = result[i]
            if str(item['nb_round']) != str(item['current_round']) and item['current_round'] is not None:
                list_current_tournament.append(item)
        if not list_current_tournament:
            return "no_result"
        else:
            return list_current_tournament

    @staticmethod
    def search_not_started_tournaments():
        """ method to select tournaments where nb_round # current round """
        list_not_started_tournament = []
        try:
            result = TOURNAMENTS.search(TOURNAMENT.name.matches('[aZ]*'))
        except ValueError:
            return "error"
        for i in range(len(result)):
            item = result[i]
            if item['current_round'] is None:
                list_not_started_tournament.append(item)
        if not list_not_started_tournament:
            return "no_result"
        else:
            return list_not_started_tournament

    def search_nb_round_for_tournament(self, tournament_uuid):
        """ method to search nb_round for a tournament """
        self.tournament_uuid = tournament_uuid
        try:
            result = TOURNAMENTS.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))
        except ValueError:
            return "error"
        result = result[0]['nb_round']
        return result

    def store_players_uuids(self, tournament_uuid, tournament_list_players):
        """ method to add player's uuids to tournament """
        self.tournament_uuid = tournament_uuid
        self.tournament_list_players = tournament_list_players
        TOURNAMENTS.update({'list_players': self.tournament_list_players},
                           TOURNAMENT.tournament_uuid == self.tournament_uuid)

    def extract_players_uuid_of_tournament(self):
        """ method to extract all player's uuid of a tournament """
        tournament = TOURNAMENTS.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))
        players_uuid_list = tournament[0]['list_players']
        return players_uuid_list

    @staticmethod
    def extract_matchs_uuid_list_of_tournament(tournament_uuid):
        """ method to extract all match's ids of a tournament """
        tournament = TOURNAMENTS.search(TOURNAMENT.tournament_uuid.matches(tournament_uuid))
        matchs_id_list = tournament[0]['list_matchs']
        return matchs_id_list

    def extract_tournament_name(self, tournament_uuid):
        """ method to extract tournament's name of a tournament with tournament uuid """
        self.tournament_uuid = tournament_uuid
        tournament = TOURNAMENTS.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))
        tournament_name = tournament[0]['name']
        return tournament_name

    def extract_all_infos_tournaments(self, tournament_uuid):
        """ method to extract all infos of a tournament with the uuid's tournament """
        self.tournament_uuid = tournament_uuid
        tournament = TOURNAMENTS.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))
        name = tournament[0]['name']
        town = tournament[0]['town']
        start_date = tournament[0]['start_date']
        end_date = tournament[0]['end_date']
        nb_round = tournament[0]['nb_round']
        current_round = tournament[0]['current_round']
        list_matchs = tournament[0]['list_matchs']
        list_players = tournament[0]['list_players']
        description = tournament[0]['description']
        return name, town, start_date, end_date, nb_round, current_round, list_matchs, list_players, description

    def store_tournament_start_date(self, tournament_uuid, tournament_start_date):
        """ method to store start date in tournament """
        self.tournament_start_date = tournament_start_date
        self.tournament_uuid = tournament_uuid
        TOURNAMENTS.update({'start_date': self.tournament_start_date},
                           TOURNAMENT.tournament_uuid == self.tournament_uuid)

    def store_tournament_end_date(self, tournament_uuid, tournament_end_date):
        """ method to store end date in tournament """
        self.tournament_start_date = tournament_end_date
        self.tournament_uuid = tournament_uuid
        TOURNAMENTS.update({'end_date': self.tournament_start_date}, TOURNAMENT.tournament_uuid
                           == self.tournament_uuid)

    def store_match_id(self, tournament_uuid, match_id_list):
        """ method to store matchs id in tournament """
        self.tournament_uuid = tournament_uuid
        self.match_id_list = match_id_list
        is_list_matchs = TOURNAMENTS.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))[0]['list_matchs']
        if is_list_matchs:
            TOURNAMENTS.update(add('list_matchs', self.match_id_list), Query().tournament_uuid == self.tournament_uuid)
        else:
            TOURNAMENTS.update({'list_matchs': self.match_id_list}, TOURNAMENT.tournament_uuid == self.tournament_uuid)

    def store_current_round(self, tournament_uuid, tournament_current_round):
        """ method to store current_round number in tournaments.json"""
        self.tournament_uuid = tournament_uuid
        self.tournament_current_round = int(tournament_current_round)
        TOURNAMENTS.update({'current_round': self.tournament_current_round},
                           TOURNAMENT.tournament_uuid == self.tournament_uuid)

    def store_round_date(self, tournament_uuid, current_round, round_start_date, round_end_date):
        """ method to store start and end dates for a round """
        self.round_start_date = round_start_date
        self.round_end_date = round_end_date
        self.tournament_uuid = tournament_uuid
        self.current_round = current_round
        all_rounds = TOURNAMENTS.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))[0]['list_rounds']
        round = ["Round" + str(self.current_round), str(self.round_start_date), str(self.round_end_date)]
        if all_rounds is None:
            all_rounds = [round]
        else:
            all_rounds.append(round)
        TOURNAMENTS.update({'list_rounds': all_rounds}, TOURNAMENT.tournament_uuid == self.tournament_uuid)

    def extract_rounds_list(self, tournament_uuid):
        """ method to extract all rounds details of a tournament"""
        self.tournament_uuid = tournament_uuid
        rounds_list = TOURNAMENTS.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))[0]['list_rounds']
        return rounds_list

    def export_tournament(self, tournaments_scores, rounds_list, tournament_start_date, tournament_end_date,
                          tournament_name, players_scores):
        self.tournaments_scores = tournaments_scores
        self.rounds_list = rounds_list
        self.tournament_start_date = tournament_start_date
        self.tournament_end_date = tournament_end_date
        self.tournament_name = tournament_name
        self.players_scores = players_scores
        rounds_list = self.tournaments_scores[0]
        matchs_list = self.tournaments_scores[1]
        p1names_list = self.tournaments_scores[2]
        p2names_list = self.tournaments_scores[3]
        p1scores_list = self.tournaments_scores[4]
        p2scores_list = self.tournaments_scores[5]
        round_max = self.tournaments_scores[6]
        index = 0
        """ method to export in html file a tournament """
        data_folder = os.path.join(os.path.dirname(__file__), "..", "data", "reports")
        file_name = "Tournoi " + self.tournament_name + " " + datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S')\
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
            report_file.write('    <th class="tg-33h5" colspan="3">Tournoi ' + self.tournament_name + ' du '
                              + self.tournament_start_date + ' au ' + self.tournament_end_date + '</th>')
            report_file.write('  </tr>')
            report_file.write('  <tr>')
            for round_nb in range(1, int(round_max) + 1):
                round_start = self.rounds_list[round_nb - 1][1]
                round_end = self.rounds_list[round_nb - 1][2]
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
