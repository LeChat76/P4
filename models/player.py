from tinydb import TinyDB, Query
import re
import uuid
import random
DB = TinyDB('data/tournaments/players.json')
PLAYERS = DB.table('players')
PLAYER = Query()
POS_PLAYER_SCORE = 7
POS_PLAYER_UUID = 1


class PlayerModel:
    """" Player class """
    """ Has a first name, name, birthday and club ID """

    def __init__(self, player_fname="", player_name="", player_birthd="", player_clubid="", player_tournament_uuid="",
                 score=0):
        """ Init player """
        self.player = None
        self.players_list = None
        self.score = score
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
                        'tournament_uuid': self.player_tournament_uuid, 'score': self.score})

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
        """ method to display player without tournament uuid """
        list_players_available = []
        result = PLAYERS.search(PLAYER.name.matches('[aZ]*'))
        if len(result) == 0:
            return "no_result"
        for i in range(len(result)):
            item = result[i]
            if not item['tournament_uuid']:
                list_players_available.append(item)
        return list_players_available

    def add_player_tournament_uuid(self, player_uuid, tournament_uuid):
        """ method to add tournament uuid to a player """
        self.player_uuid = player_uuid
        self.tournament_uuid = tournament_uuid
        PLAYERS.update({'tournament_uuid': self.tournament_uuid}, PLAYER.player_uuid == self.player_uuid)

    def create_player_list_with_same_t_uuid(self, tournament_uuid):
        """ method to create player list with the same tournament uuid """
        self.tournament_uuid = tournament_uuid
        players_same_t_uuid = PLAYERS.search(PLAYER.tournament_uuid.matches(self.tournament_uuid))
        return players_same_t_uuid

    def create_player_list_by_score(self, players_list):
        """
        method to create player's list sorted by score
        if all score egal 0, randomized players list
        """
        self.players_list = players_list
        players_scores = []
        sorted_players_list = []
        score0 = True
        nb_players = len(players_list)
        for i in range(nb_players):
            player = self.players_list[i]
            player_uuid = self.search_player_uuid(player)
            player_score = self.search_player_score(player_uuid)
            if player_score > 0:
                score0 = False
            players_scores.append(player_score)
            sorted_players_list.append(player_uuid)
        if score0:
            random.shuffle(sorted_players_list)
        else:
            sorted_players_list, players_scores = zip(*sorted(zip(sorted_players_list, players_scores)))
        return sorted_players_list

    def search_player_score(self, player_uuid):
        """method to search player's score """
        self.player_uuid = player_uuid
        player = (PLAYERS.search(PLAYER.player_uuid.matches(self.player_uuid)))[0]
        player_score = player['score']
        return player_score

    def search_player_uuid(self, player):
        """method to search player's uuid """
        self.player = player
        player_uuid = self.player['player_uuid']
        return player_uuid
