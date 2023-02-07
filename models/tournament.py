from tinydb import TinyDB, Query
import uuid
DB = TinyDB('data/tournaments/tournaments.json')
TOURNAMENTS = DB.table('tournaments')
TOURNAMENT = Query()


class TournamentModel:
    """Tournament class """

    """
    gestion du fichier JSON
    stockés dans dossier data/tournaments
    
    chaque tournois doit contenir:
        * nom
        * lieu
        * date de début et de fin
        * nombre de tours – réglez la valeur par défaut sur 4
        * numéro correspondant au tour actuel
        * une liste des tours
        * une liste des joueurs enregistrés
        * description pour les remarques générales du directeur du tournoi
    """
    def __init__(self, tournament_name="", tournament_town="", tournament_start_date="", tournament_end_date="",
                 tournament_nb_round="", tournament_description=""):
        """ Init tournament """
        self.tournament_name = tournament_name
        self.tournament_town = tournament_town
        self.tournament_start_date = tournament_start_date
        self.tournament_end_date = tournament_end_date
        self.tournament_nb_round = tournament_nb_round
        self.tournament_current_round = None
        self.tournament_list_round = None
        self.tournament_list_players = None
        self.tournament_description = tournament_description

    def __str__(self):
        return f"Tournoi {self.tournament_name} se déroulant à {self.tournament_town} du {self.tournament_start_date}" \
               f" au {self.tournament_end_date}"

    def add_tournament(self):
        """ method for add a tournament in the json file """
        TOURNAMENTS.insert({'tournament_uuid': str(uuid.uuid1()), 'name': self.tournament_name,
                            'town': self.tournament_town, 'start_date': self.tournament_start_date,
                            'end_date': self.tournament_end_date, 'nb_round': self.tournament_nb_round,
                            'actual_round': self.tournament_current_round, 'list_round': self.tournament_list_round,
                            'list_players': self.tournament_list_players, 'description': self.tournament_description})

    @staticmethod
    def display_all_tournaments():
        """ method to select all tournaments and record in a list """
        result = TOURNAMENTS.search(TOURNAMENT.name.matches('[aZ]*'))
        if len(result) == 0:
            return "no result"
        return result

    @staticmethod
    def display_completed_tournaments():
        """ method to select tournaments where nb_round = actual round """
        list_completed_tournament = []
        result = TOURNAMENTS.search(TOURNAMENT.name.matches('[aZ]*'))
        if len(result) == 0:
            return "no_result"
        for i in range(len(result)):
            item = result[i]
            if item['nb_round'] == item['actual_round']:
                list_completed_tournament.append(item)
        return list_completed_tournament

    @staticmethod
    def display_current_tournaments():
        """ method to select tournaments where nb_round # actual round """
        list_current_tournament = []
        result = TOURNAMENTS.search(TOURNAMENT.name.matches('[aZ]*'))
        if len(result) == 0:
            return "no_result"
        for i in range(len(result)):
            item = result[i]
            if item['nb_round'] != item['actual_round'] and item['actual_round'] is not None:
                list_current_tournament.append(item)
        return list_current_tournament

    @staticmethod
    def display_not_started_tournaments():
        """ method to select tournaments where nb_round # actual round """
        list_current_tournament = []
        result = TOURNAMENTS.search(TOURNAMENT.name.matches('[aZ]*'))
        if len(result) == 0:
            return "no_result"
        for i in range(len(result)):
            item = result[i]
            if not item['actual_round']:
                list_current_tournament.append(item)
        return list_current_tournament
