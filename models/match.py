import uuid


class Match:
    """ Match class """

    """
    Match = paire de joueurs
    gagnant = 1 point
    perdant = 0 point
    égalité = 0,5 points
    
    résultat d'UN match stocké sous forme de tuple contenant 2 listes avec 2 éléments : joueur et score
    LES matchs sont stockés sous formes de listes "dans l'instance du tour auquel ils appartiennent"
    """

    def __init__(self, tournament_uuid, which_round, player_one, player_two, player_one_score, player_two_score):
        self.tournament_uuid = tournament_uuid
        self.round = which_round
        self.player_one = player_one
        self.player_two = player_two
        self.player_one_score = player_one_score
        self.player_two_score = player_two_score

    def store_match(self, tournament_uuid):
        pass
