from tinydb import TinyDB, Query
import re
import uuid
DB = TinyDB('data/tournaments/players.json')
PLAYERS = DB.table('players')
PLAYER = Query()


class PlayerModel:
    """" Player class """
    """ Has a first name, name, birthday and club ID """

    def __init__(self, player_fname="", player_name="", player_birthd="", player_clubid="", player_tournament_uuid=""):
        """ Init player """
        self.tournament_uuid = None
        self.player_uuid = None
        self.player_to_search = None
        self.player_to_delete = None
        self.player_fname = player_fname
        self.player_name = player_name
        self.player_birthd = player_birthd
        self.player_clubid = player_clubid
        self.player_tournament_uuid = player_tournament_uuid

    def __str__(self):
        return f"{self.player_fname} {self.player_name} né le {self.player_birthd}, " \
               f"affilié au club {self.player_clubid}"

    def add_player(self):
        """ method for add a player in the json file """
        PLAYERS.insert({'player_uuid': str(uuid.uuid1()), 'fname': self.player_fname, 'name': self.player_name,
                        'birthd': self.player_birthd, 'clubid': self.player_clubid,
                        'tournament_uuid': self.player_tournament_uuid})

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

    def search_player(self, player_to_search):
        """ method to display player """
        self.player_to_search = player_to_search
        result = PLAYERS.search(PLAYER.name.matches(self.player_to_search, flags=re.IGNORECASE))
        if len(result) == 0:
            return "no_result"
        else:
            return result

    @staticmethod
    def search_all_players():
        """ method to count players in player.json DB"""
        result = PLAYERS.search(PLAYER.name.matches('[aZ]*'))
        if len(result) == 0:
            return "no_result"
        else:
            return result

    @staticmethod
    def search_available_player():
        """ method to display player without tournament associated """
        list_players_available = []
        result = PLAYERS.search(PLAYER.name.matches('[aZ]*'))
        if len(result) == 0:
            return "no_result"
        for i in range(len(result)):
            item = result[i]
            if not item['tournament_uuid']:
                list_players_available.append(item)
        return list_players_available

    def update_player_tournament_uuid(self, player_uuid, tournament_uuid):
        """ method to update tournamentid for a player """
        self.player_uuid = player_uuid
        self.tournament_uuid = tournament_uuid
        PLAYERS.update({'tournament_uuid': self.tournament_uuid}, PLAYER.player_uuid == self.player_uuid)
