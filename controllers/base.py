from models.player import Player
from views.menus import Menu
MIN_PLAYER = 2
MENU = Menu()
PLAYER = Player()


class Tournament:
    """ Player controller """
    """
    premier tour : mélanger les joueurs aléatoirement
    ensuite, chaque paire de joueurs est géré de la façon suivante:
        * triez les joueurs par points
        * associez les joueurs par paire et par ordre de points (si joueurs avec même nb de points, choix aléatoire)
        * NE PAS GÉNÉRER DE PAIRE AYANT DEJA JOUE ENSEMBLE
        * choix de la couleur tiré au sort (le menu doit donc demander qui a noir et qui a blanc)
    """
    def start_tournament(self):
        """ start tournament method """

        choix_menu = MENU.main_menu()
        if choix_menu == "menu_1":
            self.menu_1()
        elif choix_menu == "menu_2":
            self.menu_2()
        # elif choix_menu == "menu_3":
        #    MENU.statistics_menu()
        elif choix_menu == "menu_4":
            exit()

    def menu_1(self):
        """ Tournament Menu """
        MENU.tournament_menu()
        if "menu_1_3":
            self.start_tournament()

    def menu_2(self):
        choix_menu = MENU.player_menu()
        if choix_menu == "menu_2_1":
            self.add_player()
        elif choix_menu == "menu_2_2":
            self.delete_player()
        elif choix_menu == "menu_2_3":
            MENU.main_menu()

    def add_player(self):
        """ Request for players """

        new_player = MENU.add_player_menu()

        for player in new_player:
            player_to_add = Player(player[0], player[1], player[2], player[3])
            player_to_add.record_new_player()

        self.menu_2()

    def delete_player(self):
        player_to_delete = MENU.delete_player_menu()
        PLAYER.delete_player(player_to_delete)
        if "no result":
            print("Aucun résultat.")
            self.menu_2()

    def create_ran_player_list(self):
        pass
