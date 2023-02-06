from tinydb import TinyDB, Query
DB = TinyDB('data/tournaments/tournament.json')
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
        self.tournament_description = tournament_description

    def __str__(self):
        return f"Tournoi {self.tournament_name} se déroulant à {self.tournament_town} du {self.tournament_start_date}" \
               f" au {self.tournament_end_date}"

    def add_tournament(self):
        """ method for add a tournament in the json file """
        TOURNAMENTS.insert({'name': self.tournament_name, 'town': self.tournament_town,
                            'start_date': self.tournament_start_date, 'end_date': self.tournament_end_date,
                            'nb_round': self.tournament_nb_round, 'actual_round': self.tournament_actual_round,
                            'list_round': self.tournament_list_round, 'list_players': self.tournament_list_players,
                            'description': self.tournament_description})
