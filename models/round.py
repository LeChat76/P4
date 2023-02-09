import uuid
from tinydb import TinyDB, Query
DB = TinyDB('data/tournaments/rounds.json')
ROUNDS = DB.table('rounds')
ROUND = Query()


class Round:
    """Rouen class """

    """
    un round = plusieurs matchs de paire de joueurs
    
    cette instance doit gérer les résultats des matchs : "Les matchs doivent être stockés sous forme de liste dans
     l'instance du tour auquel ils appartiennent"
    
    chaque instance de round doit avoir un nom Round1 Round2 etc mais aussi la date et heure de debut + date et heure de
    fin qui se remplit automatiquement à chaque debut et fin de round
    """

    def __init__(self, tournament_uuid, round):
        self.tournament_uuid = tournament_uuid
        self.round = round
