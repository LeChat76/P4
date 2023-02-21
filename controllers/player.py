from views.start_menu import MainMenu
from views.player import PlayerView
from models.player import PlayerModel
MIN_PLAYER = 2
PLAYER_VIEW = PlayerView()
PLAYER_MODEL = PlayerModel()
MAINMENU = MainMenu()
MENU_PLAYER_CREATION = 1
MENU_PLAYERS_DISPLAY = 2
MENU_PLAYERS_DELETE = 3
MENU_PLAYERS_EXIT = 4


class PlayerController:

    def menu_1(self):
        """ Player menu """
        while True:
            choix = PLAYER_VIEW.player_menu()
            if choix == MENU_PLAYER_CREATION:
                self.add_player()
            if choix == MENU_PLAYERS_DISPLAY:
                self.display_player()
            elif choix == MENU_PLAYERS_DELETE:
                self.delete_player()
            elif choix == MENU_PLAYERS_EXIT:
                break

    @staticmethod
    def add_player():
        """ Method for recording new players """
        new_player = PLAYER_VIEW.add_player_menu()
        for player in new_player:
            player_to_add = PlayerModel(player[0], player[1], player[2], player[3])
            player_to_add.add_player()

    @staticmethod
    def delete_player():
        """ method to delete players """
        while True:
            all_player_list = PLAYER_MODEL.search_all_players()
            if all_player_list == "no_result":
                PLAYER_VIEW.choice_menu("Aucun joueur, merci d'en créer. Appuyez sur [ENTRER] pour revenir"
                                                " au menu.")
                break
            index_player_to_delete = PLAYER_VIEW.delete_player_menu(all_player_list)
            player_to_delete = all_player_list[index_player_to_delete]
            print("Utilisateur " + player_to_delete['fname'] + " " + player_to_delete['name'].capitalize() +
                  " supprimé.")
            PLAYER_MODEL.delete_player(player_to_delete['player_uuid'])
            choix = PLAYER_VIEW.choice_menu("Supprimer un autre joueur (O/n)? ")
            if choix == "N":
                break

    @staticmethod
    def display_player():
        """ method to display players by selecting name or all players """
        while True:
            player_to_display = PLAYER_VIEW.display_player_menu()
            result = PLAYER_MODEL.search_player(player_to_display)
            if result == "no_result" and not player_to_display == "display_all":
                choix = PLAYER_VIEW.choice_menu("Aucun résultat. Recommencer (O/n)? ")
                if choix == "N":
                    break
            elif result == "no_result" and player_to_display == "display_all":
                result = PLAYER_MODEL.search_all_players()
                if result == "no_result":
                    PLAYER_VIEW.choice_menu("Liste vide. Veuillez en créer. Appuyez sur [ENTRER] pour revenir au menu.")
                    break
                if(len(result)) == 1:
                    print(str(len(result)) + " résultat.")
                elif(len(result)) > 1:
                    print(str(len(result)) + " résultats.")
                for i in range(len(result)):
                    item = result[i]
                    print(PlayerModel(item['fname'].capitalize(), item['name'].capitalize(), item['birthd'],
                                      item['clubid']))
                choix = PLAYER_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                if choix == "N":
                    break
            elif len(result) > 0:
                if len(result) == 1:
                    print(str(len(result)) + " résultat:")
                else:
                    print(str(len(result)) + " résultats:")
                for i in range(len(result)):
                    item = result[i]
                    print(PlayerModel(item['fname'].capitalize(), item['name'].capitalize(), item['birthd'],
                                      item['clubid']))
                choix = PLAYER_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                if choix.upper() == "N":
                    break
