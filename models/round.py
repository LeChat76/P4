import uuid
from tinydb import TinyDB, Query
DB = TinyDB('data/tournaments/rounds.json')
ROUNDS = DB.table('rounds')
ROUND = Query()


class RoundModel:
    """Rouen class """

    """
    un round = plusieurs matchs de paire de joueurs
    
    cette instance doit gérer les résultats des matchs : "Les matchs doivent être stockés sous forme de liste dans
     l'instance du tour auquel ils appartiennent"
    
    chaque instance de round doit avoir un nom Round1 Round2 etc mais aussi la date et heure de debut + date et heure de
    fin qui se remplit automatiquement à chaque debut et fin de round
    """

    def __init__(self, tournament_uuid, round, start_date, end_date):
        self.tournament_uuid = tournament_uuid
        self.round = round
        self.start_date = start_date
        self.end_date = end_date

    def store_round_start_date(self):
        """ method to store start date for a round """
        round_uuid = str(uuid.uuid1())
        ROUNDS.insert({'round_uuid': round_uuid, 'tournament_uuid': self.tournament_uuid, 'round': self.round,
                      'start_date': self.start_date, 'end_date': self.end_date})
        return round_uuid

    def store_round_end_date(self, round_uuid):
        """ method to store end date for a round """
        self.round_uuid = round_uuid
        ROUNDS.update({'end_date': self.end_date}, ROUND.round_uuid == self.round_uuid)
