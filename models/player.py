from tinydb import TinyDB, Query
DB = TinyDB('data/tournaments/players.json')
PLAYERS = DB.table('players')

class Player:
    """"
    Player class
    Has a first name, name, birthday and club ID
    """



    def __init__(self, fname="", name="", birthd="", clubid="", tournamentid=""):
        """ Init player """
        self.player_to_delete = None
        self.fname = fname
        self.name = name
        self.birthd = birthd
        self.clubid = clubid
        self.tournamentid = tournamentid

    def __str__(self):
        return f"{self.fname} {self.name} né le {self.birthd} et appartient au club {self.clubid}"

    def record_new_player(self):
        """ method for add a player in the json file """
        PLAYERS.insert({'fname': self.fname, 'name': self.name, 'birthd': self.birthd, 'clubid': self.clubid,
                       'tournamentid': self.tournamentid})

    def delete_player(self, player_to_delete):
        """ method to delete a player """
        self.player_to_delete = player_to_delete
        player = Query()
        resultat = PLAYERS.search((player.name == self.player_to_delete) & (player.tournamentid == ""))
        if len(resultat) == 0:
            return "no_result"
        else:
            PLAYERS.remove((player.name == self.player_to_delete) & (player.tournamentid == ""))
            return str(len(resultat))
