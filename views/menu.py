

class Menu:
    """ Menu class """

    def __init__(self):
        self.player_fname = None
        self.player_name = None
        self.player_birthd = None

    def player_menu(self):
        """
        Recording menu of players
        2 minimum
        8 maximum
        """

        self.player_fname = input("Prénom du jouer : ")
        self.player_name = input("Nom du joueur : ")
        self.player_birthd = input("Date de naissance : ")
