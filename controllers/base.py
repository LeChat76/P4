from models.player import Player_model
from views.menus import Menu_view
MIN_PLAYER = 2
MENU_VIEW = Menu_view()
PLAYER_MODEL = Player_model()

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
        choix_menu = None
        choix_menu = MENU_VIEW.main_menu()
        if choix_menu == "menu_1":
            self.menu_1()
        elif choix_menu == "menu_2":
            self.menu_2()
        # elif choix_menu == "menu_3":
        #    self.statistics_menu()
        elif choix_menu == "menu_4":
            exit()

    def menu_1(self):
        """ Tournament Menu """
        MENU.tournament_menu()
        if "menu_1_3":
            self.start_tournament()

    def menu_2(self):
        choix_menu = MENU_VIEW.player_menu()
        if choix_menu == "menu_2_1":
            self.add_player()
        if choix_menu == "menu_2_2":
            self.display_player()
        elif choix_menu == "menu_2_3":
            self.delete_player()
        elif choix_menu == "menu_2_4":
            self.start_tournament()

    def add_player(self):
        """ Request for players """
        new_player = MENU_VIEW.add_player_menu()
        for player in new_player:
            player_to_add = Player_model(player[0], player[1], player[2], player[3])
            player_to_add.record_new_player()

        self.menu_2()

    def delete_player(self):
        player_to_delete = MENU_VIEW.delete_player_menu()
        result = PLAYER_MODEL.delete_player(player_to_delete)
        if result == "no_result":
            choix = MENU_VIEW.choice_menu("Aucun résultat. Recommencer (O/n)? ")
            if choix == "O":
                self.delete_player()
            elif choix == "N":
                self.menu_2()
        else:
            if int(result) == 1:
                print(str(result) + " résultat.")
            elif int(result) > 1:
                print(str(result) + " résultats.")
            print('Personne(s) commençant par "' + player_to_delete + '" supprimé(s).')
            choix = MENU_VIEW.choice_menu("Supprimer un autre joueur (O/n)? ")
            if choix == "O":
                self.delete_player()
            elif choix == "N":
                self.menu_2()

    def display_player(self):
        player_to_display = MENU_VIEW.display_player_menu()
        result = PLAYER_MODEL.display_player(player_to_display)
        if result == "no_result" and not player_to_display == "display_all":
            choix = MENU_VIEW.choice_menu("Aucun résultat. Recommencer (O/n)? ")
            if choix == "O":
                self.display_player()
            elif choix == "N":
                self.menu_2()
        elif result == "no_result" and player_to_display == "display_all":
            result = PLAYER_MODEL.display_all_players()
            if result == "no_result":
                choix = MENU_VIEW.choice_menu("Aucun résultat. Recommencer (O/n)? ")
                if choix == "O":
                    self.display_player()
                elif choix == "N":
                    self.menu_2()
            elif(len(result)) == 1:
                print(str(len(result)) + " résultat.")
            elif(len(result)) > 1:
                print(str(len(result)) + " résultats.")
            for i in range(len(result)):
                item = result[i]
                print(Player_model(item['fname'], item['name'], item['birthd'], item['clubid']))
            choix = MENU_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
            if choix.upper() == "O":
                self.display_player()
            elif choix.upper() == "N":
                self.menu_2()
        elif len(result) > 0:
            if result == 1:
                print(str(len(result)) + " résultat:")
            else:
                print(str(len(result)) + " résultats:")
            for i in range(len(result)):
                item = result[i]
                print(Player_model(item['fname'], item['name'], item['birthd'], item['clubid']))
            choix = MENU_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
            if choix.upper() == "O":
                self.display_player()
            elif choix.upper() == "N":
                self.menu_2()


    def create_ran_player_list(self):
        pass
