from tinydb import TinyDB, Query
import re
DB = TinyDB('data/tournaments/players.json')
PLAYERS = DB.table('players')
PLAYER = Query()


class PlayerModel:
    """" Player class """
    """ Has a first name, name, birthday and club ID """

    def __init__(self, player_fname="", player_name="", player_birthd="", player_clubid="", player_tournamentid=""):
        """ Init player """
        self.player_to_display = None
        self.player_to_delete = None
        self.player_fname = player_fname
        self.player_name = player_name
        self.player_birthd = player_birthd
        self.player_clubid = player_clubid
        self.player_tournamentid = player_tournamentid

    def __str__(self):
        return f"{self.player_fname} {self.player_name} né le {self.player_birthd}, " \
               f"affilié au club {self.player_clubid}"

    def add_player(self):
        """ method for add a player in the json file """
        PLAYERS.insert({'fname': self.player_fname, 'name': self.player_name, 'birthd': self.player_birthd,
                        'clubid': self.player_clubid, 'tournamentid': self.player_tournamentid})

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
            return result

    def display_player(self, player_to_display):
        """ method to display player """
        self.player_to_display = player_to_display
        result = PLAYERS.search(PLAYER.name.matches(self.player_to_display, flags=re.IGNORECASE))
        if len(result) == 0:
            return "no_result"
        else:
            return result

    def display_all_players(self):
        """ method to count players in player.json DB"""
        result = PLAYERS.search(PLAYER.name.matches('[aZ]*'))
        if len(result) == 0:
            return "no_result"
        else:
            return result
