from tinydb import TinyDB, Query
import uuid
import re
import random
import unidecode
import os

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data", "tournaments")
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
    with open(os.path.join(DATA_FOLDER, "players.json"), 'w') as players_file:
        pass
    players_file.close()

DB = TinyDB('data/tournaments/players.json')
PLAYERS_DB = DB.table('players')
PLAYER = Query()


class PlayerModel:
    """" Player class """
    enable = "Y"
    score = 0

    def __init__(self, player_uuid="", player_fname="", player_name="", player_birthd="", player_clubid=""):
        """ Init player """
        self.player_uuid = player_uuid
        self.player_fname = player_fname
        self.player_name = player_name
        self.player_birthd = player_birthd
        self.player_clubid = player_clubid

    def __str__(self):
        return f"{self.player_fname} {self.player_name} né le {self.player_birthd}," \
               f" affilié au club {self.player_clubid}."

    def save_player(self):
        """ method to store player in DB """
        player_fname = unidecode.unidecode(self.player_fname.capitalize())
        player_name = unidecode.unidecode(self.player_name.capitalize())
        player_birthd = self.player_birthd
        player_clubid = self.player_clubid
        PLAYERS_DB.insert({'player_uuid': str(uuid.uuid1()), 'fname': player_fname,
                           'name': player_name, 'birthd': player_birthd, 'clubid': player_clubid, 'score': 0,
                           'enable': "Y"})

    def delete_player(self):
        """ method to delete a player (delete = modify 'enable' value with 'N' """
        player_uuid = self.player_uuid
        player_fname = self.player_fname
        player_name = self.player_name
        PLAYERS_DB.update({'enable': "N"}, PLAYER.player_uuid == player_uuid)
        return player_fname + " " + player_name

    @staticmethod
    def search_player(player_to_search):
        """ method to display player (search by name) """
        try:
            result_doc = PLAYERS_DB.search(PLAYER.name.matches(player_to_search, flags=re.IGNORECASE)
                                           & (PLAYER.enable != "N"))
            players_list = []
            for doc in result_doc:
                player = PlayerModel()
                player.player_uuid = doc['player_uuid']
                player.player_name = doc['name']
                player.player_fname = doc['fname']
                player.player_birthd = doc['birthd']
                player.player_clubid = doc['clubid']
                players_list.append(player)
        except ValueError:
            return "error"
        if len(result_doc) == 0:
            return "no_result"
        else:
            return players_list

    @staticmethod
    def search_all_players(by_name=False, by_fname=False):
        """ method to count players in players.json DB"""
        try:
            result_doc = PLAYERS_DB.search(PLAYER.enable != "N")
            players_list = []
            for doc in result_doc:
                player = PlayerModel()
                player.player_uuid = doc['player_uuid']
                player.player_name = doc['name']
                player.player_fname = doc['fname']
                player.player_birthd = doc['birthd']
                player.player_clubid = doc['clubid']
                players_list.append(player)
        except ValueError:
            return "error"

        if len(players_list) == 0:
            return "no_result"
        elif by_name:
            players_list.sort(key=lambda x: x.player_name)
            return players_list
        elif by_fname:
            players_list.sort(key=lambda x: x.player_fname)
            return players_list
        else:
            return players_list

    @staticmethod
    def sort_player_list(players_list):
        """ method to create player's list sorted by score if all score egal 0, randomized players list """
        score0 = True
        for player in players_list:
            if player.score > 0:
                score0 = False
        if not score0:
            players_list.sort(key=lambda x: x.score)
        else:
            random.shuffle(players_list)
        return players_list

    @staticmethod
    def check_players_list(players_list, previous_matchs_list):
        """ method to compare matchs players VS previous matchs players """
        already_played = False
        if previous_matchs_list:
            checked_players_list = []
            while players_list:
                player1 = players_list[0]
                p1_uuid = player1.player_uuid
                players_list.pop(0)
                for player2 in players_list:
                    p2_uuid = player2.player_uuid
                    match = [p1_uuid, p2_uuid]
                    match_players = [player1, player2]
                    if match in previous_matchs_list or match[::-1] in previous_matchs_list:
                        already_played = True
                        continue
                    elif match not in previous_matchs_list or match[::-1] not in previous_matchs_list:
                        already_played = False
                        break
                checked_players_list.append(match_players)
                players_list.remove(player2)
            for player in checked_players_list:
                players_list += player
            return players_list, already_played
        else:
            return players_list, already_played

    @staticmethod
    def search_player_score(player_uuid):
        """method to search player's score """
        result_doc = (PLAYERS_DB.search(PLAYER.player_uuid.matches(player_uuid)))[0]
        player = PlayerModel()
        player.score = result_doc['score']
        return player.score

    def extract_player_fname_and_name(self):
        """ method to extract players' fname and name from player object """
        player_uuid = self.player_uuid
        result_doc = PLAYERS_DB.search(PLAYER.player_uuid.matches(player_uuid))
        self.player_fname = result_doc[0]['fname']
        self.player_name = result_doc[0]['name']
        player = self.player_fname + " " + self.player_name
        return player

    @staticmethod
    def store_score(player_uuid, score):
        """
        method to store score  (add score to current score) in the json player's file, to use with only
        one player
        """
        player = PLAYERS_DB.search(PLAYER.player_uuid.matches(player_uuid))
        current_score = player[0]['score']
        new_score = float(current_score) + float(score)
        PLAYERS_DB.update({'score': new_score}, PLAYER.player_uuid == player_uuid)

    @staticmethod
    def store_score_from_previous_match(players_list, players_scores):
        """
        method to store previous scores in players when resume previous tournament (replace score from previous,
        used for a list of players)
        """
        for i in range(len(players_list)):
            PLAYERS_DB.update({'score': players_scores[i]}, PLAYER.player_uuid == players_list[i])

    @staticmethod
    def delete_score_player(players_list):
        """ method to delete scores in players.json for uuid list of players"""
        for player_uuid in players_list:
            for i in range(len(players_list)):
                PLAYERS_DB.update({'score': 0}, PLAYER.player_uuid == player_uuid)

    @staticmethod
    def delete_score_player_object(players_list):
        """ method to delete scores in players.json from objects list """
        for player in players_list:
            player_uuid = player.player_uuid
            PLAYERS_DB.update({'score': 0}, PLAYER.player_uuid == player_uuid)

    @staticmethod
    def extract_player_uuid_list(players_list):
        """ method to extract players uuids from list of objects """
        players_uuid_list = []
        for player in players_list:
            player_uuid = player.player_uuid
            players_uuid_list.append(player_uuid)
        return players_uuid_list

    def extract_player_uuid(self):
        """ method to extract players uuid for a single player object """
        return self.player_uuid

    @staticmethod
    def create_player_object(player_uuid):
        """ method to create a player object from uuid """
        result_doc = PLAYERS_DB.search(PLAYER.player_uuid == player_uuid)
        for doc in result_doc:
            player = PlayerModel()
            player.player_uuid = doc['player_uuid']
            player.player_name = doc['name']
            player.player_fname = doc['fname']
            player.player_birthd = doc['birthd']
            player.player_clubid = doc['clubid']
            player.score = doc['score']
            player.enable = doc['enable']
        return player

    @staticmethod
    def update_score_in_player_object(players_list):
        """ method to update score in players objects from players.json """
        players_list = players_list
        for player in players_list:
            player_uuid = player.player_uuid
            result_doc = PLAYERS_DB.search(PLAYER.player_uuid.matches(player_uuid))
            score = result_doc[0]['score']
            player.score = score
