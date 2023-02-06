from views.start_menu import MainMenu
from views.player import PlayerView
from models.player import PlayerModel
MIN_PLAYER = 2
PLAYER_VIEW = PlayerView()
PLAYER_MODEL = PlayerModel()
MAINMENU = MainMenu()


class PlayerController:

    def menu_2(self):
        """ Player menu """
        while True:
            choix = PLAYER_VIEW.player_menu()
            if choix == "menu_2_1":
                self.add_player()
            if choix == "menu_2_2":
                self.display_player()
            elif choix == "menu_2_3":
                self.delete_player()
            elif choix == "menu_2_4":
                break

    def add_player(self):
        """ Method for recording new players """
        new_player = PLAYER_VIEW.add_player_menu()
        for player in new_player:
            player_to_add = PlayerModel(player[0], player[1], player[2], player[3])
            player_to_add.add_player()

    def delete_player(self):
        """ method to delete players """
        while True:
            player_to_delete = PLAYER_VIEW.delete_player_menu()
            result = PLAYER_MODEL.delete_player(player_to_delete)
            if result == "no_result":
                choix = PLAYER_VIEW.choice_menu("Aucun résultat. Recommencer (O/n)? ")
                if choix == "N":
                    break
            else:
                #if len(result) == 1:
                #    print(str(result) + " résultat.")
                #elif len(result) > 1:
                #    print(str(result) + " résultats.")
                for i in range(len(result)):
                    item = result[i]
                    print("Utilisateur " + item['name'] + " supprimé.")
                print(str(len(result)) + ' Personne(s) commençant par "' + player_to_delete + '" supprimé(s).')
                choix = PLAYER_VIEW.choice_menu("Supprimer un autre joueur (O/n)? ")
                if choix == "N":
                    break

    def display_player(self):
        while True:
            player_to_display = PLAYER_VIEW.display_player_menu()
            result = PLAYER_MODEL.display_player(player_to_display)
            if result == "no_result" and not player_to_display == "display_all":
                choix = PLAYER_VIEW.choice_menu("Aucun résultat. Recommencer (O/n)? ")
                if choix == "N":
                    break
            elif result == "no_result" and player_to_display == "display_all":
                result = PLAYER_MODEL.display_all_players()
                if result == "no_result":
                    choix = PLAYER_VIEW.choice_menu("Aucun résultat. Recommencer (O/n)? ")
                    if choix == "O":
                        continue
                    if choix == "N":
                        break
                if(len(result)) == 1:
                    print(str(len(result)) + " résultat.")
                elif(len(result)) > 1:
                    print(str(len(result)) + " résultats.")
                for i in range(len(result)):
                    item = result[i]
                    print(PlayerModel(item['fname'], item['name'], item['birthd'], item['clubid']))
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
                    print(PlayerModel(item['fname'], item['name'], item['birthd'], item['clubid']))
                choix = PLAYER_VIEW.choice_menu("Faire une autre recherche (O/n)? ")
                if choix.upper() == "N":
                    break

    def create_ran_player_list(self):
        pass
