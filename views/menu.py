

class Menu:
    """ Menu class """

    def prompt_player_fname(self):
        """ Request player first name """
        player_fname = input("Prénom du joueur : ")
        return player_fname

    def prompt_player_name(self):
        """ Request player name """
        player_name = input("Nom du joueur : ")
        return player_name

    def prompt_player_birthd(self):
        """ Request player birthday """
        player_birthd = input("Date d'anniversaire (au format JJ/MM/AAAA) : ")
        return player_birthd

    def prompt_player_clubid(self):
        """ Request player club ID """
        player_clubid = input("ID du club (au format AB12345) : ")
        return player_clubid

    def prompt_add_player(self):
        """ Request for recording à new player """
        new_player = input("Ajouter un autre joueur au tournoi (O/n)?")
        return new_player
