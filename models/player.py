from tinydb import TinyDB, Query
import uuid
import re
import random

DB = TinyDB('data/tournaments/players.json')
PLAYERS = DB.table('players')
PLAYER = Query()
POS_PLAYER_SCORE = 7
POS_PLAYER_UUID = 1


class PlayerModel:
    """" Player class """
    """ Has a first name, name, birthday and club ID """

    def __init__(self, player_fname="", player_name="", player_birthd="", player_clubid="", score=0):
        """ Init player """
        self.player = None
        self.players_list = None
        self.score = score
        self.player_uuid = None
        self.player_to_search = None
        self.player_uuid_to_delete = None
        self.player_fname = player_fname
        self.player_name = player_name
        self.player_birthd = player_birthd
        self.player_clubid = player_clubid

    def __str__(self):
        return f"{self.player_fname} {self.player_name} né le {self.player_birthd}, " \
               f"affilié au club {self.player_clubid}."

    def add_player(self):
        """ method for add a player in the json file """
        PLAYERS.insert({'player_uuid': str(uuid.uuid1()), 'fname': self.player_fname, 'name': self.player_name,
                        'birthd': self.player_birthd, 'clubid': self.player_clubid, 'score': self.score})

    def delete_player(self, player_uuid_to_delete):
        """ method to delete a player """
        self.player_uuid_to_delete = player_uuid_to_delete
        PLAYERS.remove(PLAYER.player_uuid == self.player_uuid_to_delete)

    def search_player(self, player_to_search):
        """ method to display player (search by name) """
        self.player_to_search = player_to_search
        try:
            result = PLAYERS.search(PLAYER.name.matches(self.player_to_search, flags=re.IGNORECASE))
        except ValueError:
            print("Problème de structure sur fichier players.json.\nVérifiez le et recommencez.")
            exit()
        if len(result) == 0:
            return "no_result"
        else:
            return result

    @staticmethod
    def search_all_players():
        """ method to count players in player.json DB"""
        try:
            result = PLAYERS.search(PLAYER.name.matches('[aZ]*'))
        except ValueError:
            print("Problème de structure sur fichier players.json.\nVérifiez le et recommencez.")
            exit()
        if len(result) == 0:
            return "no_result"
        else:
            return result

    def create_player_list(self, players_list, ):
        """
        players_list = players_uuid
        method to create player's list sorted by score
        if all score egal 0, randomized players list
        """
        self.players_list = players_list
        players_scores = []
        sorted_players_list = []
        score0 = True
        nb_players = len(players_list)
        for i in range(nb_players):
            player_uuid = players_list[i]
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

    def extract_player_fname_and_name(self, player_uuid):
        """ method to extract players' name """
        self.player_uuid = player_uuid
        result = PLAYERS.search(PLAYER.player_uuid.matches(player_uuid))
        player_first_name = result[0]['fname']
        player_name = result[0]['name']
        player = player_first_name.capitalize() + " " + player_name.capitalize()
        return player

    def store_score(self, player_uuid, score):
        """ method to store score  (add score to current score) in the json player's file """
        self.player_uuid = player_uuid
        self.score = score
        player = PLAYERS.search(PLAYER.player_uuid.matches(self.player_uuid))
        current_score = player[0]['score']
        new_score = float(current_score) + float(score)
        PLAYERS.update({'score': new_score}, PLAYER.player_uuid == self.player_uuid)




