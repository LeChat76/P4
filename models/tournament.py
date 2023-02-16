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
    def __init__(self, tournament_name="", tournament_town="", tournament_nb_round="", tournament_description=""):
        """ Init tournament """
        self.match_id_list = None
        self.player_uuid = None
        self.tournament_uuid = None
        self.tournament_name = tournament_name
        self.tournament_town = tournament_town
        self.tournament_nb_round = tournament_nb_round
        self.tournament_start_date = None
        self.tournament_end_date = None
        self.tournament_current_round = None
        self.tournament_list_matchs = None
        self.tournament_list_players = None
        self.tournament_description = tournament_description

    def __str__(self):
        return f"Tournoi {self.tournament_name} se déroulant à {self.tournament_town} et comportant" \
               f" {self.tournament_nb_round} round(s)."

    def add_tournament(self):
        """ method for add a tournament in the json file """
        TOURNAMENTS.insert({'tournament_uuid': str(uuid.uuid1()), 'name': self.tournament_name,
                            'town': self.tournament_town, 'start_date': self.tournament_start_date,
                            'end_date': self.tournament_end_date, 'nb_round': self.tournament_nb_round,
                            'current_round': self.tournament_current_round, 'list_round': self.tournament_list_matchs,
                            'list_players': self.tournament_list_players, 'description': self.tournament_description})

    @staticmethod
    def search_all_tournaments():
        """ method to select all tournaments and record in a list """
        try:
            result = TOURNAMENTS.search(TOURNAMENT.name.matches('[aZ]*'))
        except ValueError:
            print("Problème de structure sur fichier tournaments.json.\nVérifiez le et recommencez.")
            exit()
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
            print("Problème de structure sur fichier tournaments.json.\nVérifiez le et recommencez.")
            exit()
        if len(result) == 0:
            return "no_result"
        for i in range(len(result)):
            item = result[i]
            if item['nb_round'] == item['current_round']:
                list_completed_tournament.append(item)
        return list_completed_tournament

    @staticmethod
    def search_current_tournaments():
        """ method to select tournaments where nb_round != current_round """
        list_current_tournament = []
        try:
            result = TOURNAMENTS.search(TOURNAMENT.name.matches('[aZ]*'))
        except ValueError:
            print("Problème de structure sur fichier tournaments.json.\nVérifiez le et recommencez.")
            exit()
        if len(result) == 0:
            return "no_result"
        for i in range(len(result)):
            item = result[i]
            if item['nb_round'] != item['current_round'] and item['current_round'] is not None:
                list_current_tournament.append(item)
        return list_current_tournament

    @staticmethod
    def search_not_started_tournaments():
        """ method to select tournaments where nb_round # current round """
        list_current_tournament = []
        try:
            result = TOURNAMENTS.search(TOURNAMENT.name.matches('[aZ]*'))
        except ValueError:
            print("Problème de structure sur fichier tournaments.json.\nVérifiez le et recommencez.")
            exit()
        if len(result) == 0:
            return "no_result"
        else:
            for i in range(len(result)):
                item = result[i]
                if item['current_round'] is None:
                    list_current_tournament.append(item)
            return list_current_tournament

    def search_nb_round_for_tournament(self, tournament_uuid):
        """ method to search nb_round for a tournament """
        self.tournament_uuid = tournament_uuid
        try:
            result = TOURNAMENTS.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))
        except ValueError:
            print("Problème de structure sur fichier tournaments.json.\nVérifiez le et recommencez.")
            exit()
        result = result[0]['nb_round']
        return result

    def store_players_uuids(self, tournament_uuid, tournament_list_players):
        """ method to add player's uuids to tournament """
        self.tournament_uuid = tournament_uuid
        self.tournament_list_players = tournament_list_players
        TOURNAMENTS.update({'list_players': self.tournament_list_players}, TOURNAMENT.tournament_uuid ==
                           self.tournament_uuid)

    def extract_players_uuid_of_tournament(self, tournament_uuid):
        """ method to extract all player's uuid of a tournament """
        self.tournament_uuid = tournament_uuid
        tournament = TOURNAMENTS.search(TOURNAMENT.tournament_uuid.matches(self.tournament_uuid))
        players_uuid_list = (tournament[0]['list_players']).split(",")
        return players_uuid_list

    def store_tournament_start_date(self, tournament_uuid, tournament_start_date):
        """ method to store start date in tournament """
        self.tournament_start_date = tournament_start_date
        self.tournament_uuid = tournament_uuid
        TOURNAMENTS.update({'start_date': self.tournament_start_date}, TOURNAMENT.tournament_uuid ==
                           self.tournament_uuid)

    def store_tournament_end_date(self, tournament_uuid, tournament_end_date):
        """ method to store start date in tournament """
        self.tournament_start_date = tournament_end_date
        self.tournament_uuid = tournament_uuid
        TOURNAMENTS.update({'end_date': self.tournament_start_date}, TOURNAMENT.tournament_uuid ==
                           self.tournament_uuid)

    def store_match_id(self, tournament_uuid, match_id_list):
        """ method to store matchs id in tournament """
        self.tournament_uuid = tournament_uuid
        self.match_id_list = match_id_list
        TOURNAMENTS.update({'list_matchs': self.match_id_list}, TOURNAMENT.tournament_uuid == self.tournament_uuid)

    def store_current_round(self, tournament_uuid, tournament_current_round):
        self.tournament_uuid = tournament_uuid
        self.tournament_current_round = tournament_current_round
        TOURNAMENTS.update({'current_round': self.tournament_current_round}, TOURNAMENT.tournament_uuid ==
                           self.tournament_uuid)
