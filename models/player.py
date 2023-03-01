from tinydb import TinyDB, Query
import uuid
import re
import random
import sys

DB = TinyDB('data/tournaments/players.json')
PLAYERS = DB.table('players')
PLAYER = Query()


class PlayerModel:
    """" Player class """

    def __init__(self, player_fname="", player_name="", player_birthd="", player_clubid="", score=0):
        """ Init player """
        self.players_scores = None
        self.players_uuid = None
        self.player = None
        self.players_list = []
        self.score = score
        self.player_uuid = None
        self.player_to_search = None
        self.player_fname = player_fname
        self.player_name = player_name
        self.player_birthd = player_birthd
        self.player_clubid = player_clubid
        self.enable = "Y"

    def __str__(self):
        return f"{self.player_fname} {self.player_name} né le {self.player_birthd}," \
               f" affilié au club {self.player_clubid}."

    def add_player(self):
        """ method for add a player in the json file """
        PLAYERS.insert({'player_uuid': str(uuid.uuid1()), 'fname': self.player_fname, 'name': self.player_name,
                        'birthd': self.player_birthd, 'clubid': self.player_clubid, 'score': self.score,
                        'enable': self.enable})

    def delete_player(self, player_uuid):
        """ method to delete a player """
        self.player_uuid = player_uuid
        PLAYERS.update({'enable': False}, PLAYER.player_uuid == self.player_uuid)

    def search_player(self, player_to_search):
        """ method to display player (search by name) """
        self.player_to_search = player_to_search
        try:
            result = PLAYERS.search(PLAYER.name.matches(self.player_to_search, flags=re.IGNORECASE)
                                    & (PLAYER.enable != "N"))
        except ValueError:
            print("Problème de structure sur fichier players.json.\nVérifiez le et recommencez.")
            sys.exit()
        if len(result) == 0:
            return "no_result"
        else:
            return result

    @staticmethod
    def search_all_players(by_name=False, by_fname=False):
        """ method to count players in players.json DB"""
        players_uuid_list = []
        players_fname_list = []
        players_name_list = []
        try:
            result = PLAYERS.search(PLAYER.enable != "N")
        except ValueError:
            print("Problème de structure sur fichier players.json.\nVérifiez le et recommencez.")
            sys.exit()
        if len(result) == 0:
            return "no_result"
        elif by_name:
            for player in result:
                players_name_list.append((player['name']).capitalize())
                players_uuid_list.append(player['player_uuid'])
            players_name_list, players_uuid_list = zip(*sorted(zip(players_name_list, players_uuid_list)))
            return players_uuid_list
        elif by_fname:
            for player in result:
                players_fname_list.append(player['fname'].capitalize())
                players_uuid_list.append(player['player_uuid'])
            players_fname_list, players_uuid_list = zip(*sorted(zip(players_fname_list, players_uuid_list)))
            return players_uuid_list
        else:
            return result

    def create_player_list(self, players_list):
        """method to create player's list sorted by score if all score egal 0, randomized players list """
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
            players_scores, sorted_players_list = zip(*sorted(zip(players_scores, sorted_players_list)))
        return list(sorted_players_list)

    @staticmethod
    def check_players_list(players_list, previous_matchs_list):
        """ method to compare matchs players VS previous matchs players """
        match = None
        p2_uuid = None
        checked_players_list = []
        already_played = False
        if previous_matchs_list:
            while players_list:
                p1_uuid = players_list.pop(0)
                for p2_uuid in players_list:
                    match = [p1_uuid, p2_uuid]
                    if match in previous_matchs_list or match[::-1] in previous_matchs_list:
                        already_played = True
                        continue
                    elif match not in previous_matchs_list or match[::-1] not in previous_matchs_list:
                        already_played = False
                        break
                checked_players_list.append(match)
                players_list.remove(p2_uuid)
            for player_uuid in checked_players_list:
                players_list += player_uuid
            return players_list, already_played
        else:
            return players_list, already_played

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
        """ method to extract players' fname and name with player's uuid """
        self.player_uuid = player_uuid
        result = PLAYERS.search(PLAYER.player_uuid.matches(player_uuid))
        player_first_name = result[0]['fname']
        player_name = result[0]['name']
        player = player_first_name.capitalize() + " " + player_name.capitalize()
        return player

    def extract_data_player(self, players_uuid):
        """ method to extract players' fname, name, birthd and clubid with player's uuid """
        players_list = []
        self.players_uuid = players_uuid
        for player_uuid in self.players_uuid:
            result = PLAYERS.search(PLAYER.player_uuid.matches(player_uuid))
            player_first_name = result[0]['fname']
            player_name = result[0]['name']
            player_birthd = result[0]['birthd']
            player_clubid = result[0]['clubid']
            player = [player_first_name.capitalize(), player_name.capitalize(), player_birthd, player_clubid]
            players_list.append(player)
        return players_list

    def store_score(self, player_uuid, score):
        """ method to store score  (add score to current score) in the json player's file, to use with only
        one player """
        self.player_uuid = player_uuid
        self.score = score
        player = PLAYERS.search(PLAYER.player_uuid.matches(self.player_uuid))
        current_score = player[0]['score']
        new_score = float(current_score) + float(score)
        PLAYERS.update({'score': new_score}, PLAYER.player_uuid == self.player_uuid)

    def store_score_from_previous_match(self, players_list, players_scores):
        """ method to store previous scores in players when resume previous tournament (replace score from previous,
        used for a list of players) """
        self.players_list = players_list
        self.players_scores = players_scores
        for i in range(len(players_list)):
            PLAYERS.update({'score': players_scores[i]}, PLAYER.player_uuid == self.players_list[i])
