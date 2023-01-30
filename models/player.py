

class Player:
    """"
    Player class
    Has a first name, name, birthday and club ID
    """

    def __init__(self, fname, name, birthd, club_id):
        """ Init player
        """
        self.fname = fname
        self.name = name
        self.birthd = birthd
        self.club_id = club_id

    def __str__(self):
        return f"{self.fname} {self.name} né le {self.birthd} et appartient au club {self.club_id}"
