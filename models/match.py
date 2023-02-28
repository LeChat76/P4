from models.player import PlayerModel
from tinydb import TinyDB, Query
from constantes import MATCH_ID_LIST, MATCHS_LIST
import uuid
DB = TinyDB('data/tournaments/matchs.json')
MATCHS = DB.table('matchs')
MATCH = Query()


class MatchModel:
    """ Match class """

    def __init__(self, tournament_uuid="", round_nb="", match_nb="",
                 player_one_uuid="", player_two_uuid="",
                 player_one_score="", player_two_score=""):
        self.players_list = None
        self.matchs_list = None
        self.matchs_ids_list = []
        self.tournament_uuid = tournament_uuid
        self.round_nb = round_nb
        self.match_nb = match_nb
        self.player_one_uuid = player_one_uuid
        self.player_two_uuid = player_two_uuid
        self.player_one_score = player_one_score
        self.player_two_score = player_two_score

    def create_tuple_for_match(self):
        """ method to store match result for a round in a list of tuple
         (who contains list of players + scores) """
        p1 = (self.player_one_uuid, self.player_one_score)
        p2 = (self.player_two_uuid, self.player_two_score)
        match_id = "T_" + str(self.tournament_uuid) + "_R" +\
                   str(self.round_nb) + "_M" + str(self.match_nb)
        PlayerModel().store_score(self.player_one_uuid, self.player_one_score)
        PlayerModel().store_score(self.player_two_uuid, self.player_two_score)
        match = (match_id, p1, p2)
        MATCHS_LIST.append(match)

    @staticmethod
    def store_match():
        """ method to store a round with list of tuple in json file """
        MATCH_ID_LIST.clear()
        for match in MATCHS_LIST:
            match_id = match[0]
            p1 = match[1]
            p2 = match[2]
            p1_uuid, p1_score = p1[0], p1[1]
            p2_uuid, p2_score = p2[0], p2[1]
            MATCHS.insert({'match_uuid': str(uuid.uuid1()),
                           'match_id': match_id, 'player_one_uuid': p1_uuid,
                           'player_two_uuid': p2_uuid,
                           'player_one_score': p1_score,
                           'player_two_score': p2_score})
            MATCH_ID_LIST.append(match_id)
        MATCHS_LIST.clear()
        return MATCH_ID_LIST

    def extract_scores(self, matchs_ids_list):
        """ method to extract score from a match id """
        tournament_scores = None
        rounds = []
        matchs = []
        p1_name = []
        p2_name = []
        p1_scores = []
        p2_scores = []
        self.matchs_ids_list = matchs_ids_list
        for i in range(len(self.matchs_ids_list)):
            match_id = matchs_ids_list[i]
            result = MATCHS.search(MATCH.match_id.matches(match_id))
            rounds.append((match_id.split("_")[2])[1:])
            round_max = max(rounds)
            matchs.append((match_id.split("_")[3])[1:])
            match_max = max(matchs)
            p1_uuid = result[0]['player_one_uuid']
            p1_name.append(PlayerModel().
                           extract_player_fname_and_name(p1_uuid))
            p2_uuid = result[0]['player_two_uuid']
            p2_name.append(PlayerModel().
                           extract_player_fname_and_name(p2_uuid))
            p1_scores.append(result[0]['player_one_score'])
            p2_scores.append(result[0]['player_two_score'])
            tournament_scores = [rounds, matchs, p1_name, p2_name, p1_scores,
                                 p2_scores, round_max, match_max]
        return tournament_scores

    @staticmethod
    def create_matchs_players_list(matchs_list):
        """ method to create list of matchs already played for a tournament """
        previous_matchs_players_list = []
        if matchs_list:
            for match in matchs_list:
                result = MATCHS.search(MATCH.match_id.matches(match))
                p1_uuid = result[0]['player_one_uuid']
                p2_uuid = result[0]['player_two_uuid']
                previous_matchs_players_list.append([p1_uuid, p2_uuid])
        return previous_matchs_players_list

    def extract_previous_scores(self, players_list, matchs_list):
        """ method to extract all previous scores from stored matches """
        self.matchs_list = matchs_list
        self.players_list = players_list
        scores = []
        for i in range(len(players_list)):
            player_score = 0
            for match_id in matchs_list:
                result = MATCHS.search(MATCH.match_id.matches(match_id))
                p1_uuid = result[0]['player_one_uuid']
                p2_uuid = result[0]['player_two_uuid']
                p1_score = result[0]['player_one_score']
                p2_score = result[0]['player_two_score']
                if players_list[i] == p1_uuid:
                    player_score += p1_score
                elif players_list[i] == p2_uuid:
                    player_score += p2_score
            scores.append(player_score)
        return scores
