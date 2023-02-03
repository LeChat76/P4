from tinydb import TinyDB, Query
import re
DB = TinyDB('data/tournaments/players.json')
PLAYERS = DB.table('players')
PLAYER = Query()


class Player:
    """" Player class """
    """ Has a first name, name, birthday and club ID """

    def __init__(self, fname="", name="", birthd="", clubid="", tournamentid=""):
        """ Init player """
        self.player_to_display = None
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
        result = PLAYERS.search(PLAYER.name.matches(self.player_to_delete, flags=re.IGNORECASE))
        if len(result) == 0:
            return "no_result"
        else:
            for i in range(len(result)):
                item = result[i]
                PLAYERS.remove(PLAYER.name == item["name"])
            return str(len(result))

    def display_player(self, player_to_display):
        """ method to display player """
        self.player_to_display = player_to_display
        result = PLAYERS.search(PLAYER.name.matches(self.player_to_display, flags=re.IGNORECASE))
        if len(result) == 0:
            return "no_result"
        else:
            return result
