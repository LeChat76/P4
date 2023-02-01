from tinydb import TinyDB, Query


class Player:
    """"
    Player class
    Has a first name, name, birthday and club ID
    """

    def __init__(self, fname, name, birthd, clubid):
        """ Init player
        """
        self.fname = fname
        self.name = name
        self.birthd = birthd
        self.clubid = clubid

    def __str__(self):
        return f"{self.fname} {self.name} né le {self.birthd} et appartient au club {self.clubid}"

    def record_new_player(self):
        """ method for add a player in the json file """
        db = TinyDB('data/tournaments/players.json')
        db.insert({'fname': self.fname, 'name': self.name, 'birthd': self.birthd, 'clubid': self.clubid})
