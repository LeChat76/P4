from tinydb import TinyDB, Query
import uuid
DB = TinyDB('data/tournaments/matchs.json')
MATCHS = DB.table('matchs')
MATCH = Query()
MATCHS_LIST = []


class MatchModel:
    """ Match class """

    """
    Match = paire de joueurs
    gagnant = 1 point
    perdant = 0 point
    égalité = 0,5 points
    
    résultat d'UN match stocké sous forme de tuple contenant 2 listes avec 2 éléments : joueur et score
    LES matchs sont stockés sous formes de listes "dans l'instance du tour auquel ils appartiennent"
    """

    def __init__(self, tournament_uuid="", round_nb="", match_nb="", player_one_uuid="", player_two_uuid="",
                 player_one_score="", player_two_score=""):
        self.tournament_uuid = tournament_uuid
        self.round_nb = round_nb
        self.match_nb = match_nb
        self.player_one_uuid = player_one_uuid
        self.player_two_uuid = player_two_uuid
        self.player_one_score = player_one_score
        self.player_two_score = player_two_score

    def create_tuple_for_match(self):
        """ method to store match result for a round in a list of tuple (who contains list of players + scores) """
        p1 = (self.player_one_uuid, self.player_one_score)
        p2 = (self.player_two_uuid, self.player_two_score)
        match_id = "T_" + str(self.tournament_uuid) + "_R" + str(self.round_nb) + "_M" + str(self.match_nb)
        match = (match_id, p1, p2)
        MATCHS_LIST.append(match)

    @staticmethod
    def store_match():
        """ method to store a round with list of tuple in json file """
        for match in MATCHS_LIST:
            match_id = match[0]
            p1 = match[1]
            p2 = match[2]
            p1_uuid, p1_score = p1[0], p1[1]
            p2_uuid, p2_score = p2[0], p2[1]
            MATCHS.insert({'match_uuid': str(uuid.uuid1()), 'match_id': match_id, 'player_one_uuid': p1_uuid,
                           'player_two_uuid': p2_uuid, 'player_one_score': p1_score,
                           'player_two_score': p2_score})
        # del MATCHS_LIST
