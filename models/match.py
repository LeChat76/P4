from tinydb import TinyDB, Query
import uuid
DB = TinyDB('data/tournaments/matchs.json')
MATCHS = DB.table('matchs')
MATCH = Query()


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

    def __init__(self, tournament_uuid="", match_nb="", round_nb="", player_one_uuid="", player_two_uuid="",
                 player_one_score="", player_two_score=""):
        self.tournament_uuid = tournament_uuid
        self.match_nb = match_nb
        self.round_nb = round_nb
        self.player_one_uuid = player_one_uuid
        self.player_two_uuid = player_two_uuid
        self.player_one_score = player_one_score
        self.player_two_score = player_two_score

    def store_match(self):
        match_id = "T_" + str(self.tournament_uuid) + "_R" + str(self.round_nb) + "_M" + str(self.match_nb)
        MATCHS.insert({'match_uuid': str(uuid.uuid1()), 'match_id': match_id, 'player_one_uuid': self.player_one_uuid,
                       'player_two_uuid': self.player_two_uuid, 'player_one_score': self.player_one_score,
                       'player_two_score': self.player_two_score})
