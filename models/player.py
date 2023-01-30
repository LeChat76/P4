import random


class Player:
    """"
    Player class
    Has a first name, name and birthday
    """

    def __init__(self, fname, name, birthd, club_ID):
        """ Init player """
        self.fname = fname
        self.name = name
        self.birthd = birthd
        self.club_ID = club_ID

    def __str__(self):
        return f"{self.fname} {self.name} né le {self.birthd} et appartient au club {self.club_ID}"








