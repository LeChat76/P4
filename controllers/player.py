import os
import sys
from views.player import PlayerView
from models.player import PlayerModel
from constantes import MENU_PLAYER_CREATION, MENU_PLAYERS_DISPLAY, MENU_PLAYERS_DELETE, MENU_PLAYERS_EXIT

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data", "tournaments")
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
    with open(os.path.join(DATA_FOLDER, "players.json"), 'w') as creating_players_file:
        pass


class PlayerController:
    """ Player controller """
    def __init__(self):
        self.player_model = PlayerModel()
        self.player_view = PlayerView()

    def menu_player(self):
        """ Player menu """
        while True:
            choix = self.player_view.player_menu()
            if choix == MENU_PLAYER_CREATION:
                self.add_player()
            if choix == MENU_PLAYERS_DISPLAY:
                self.display_player()
            elif choix == MENU_PLAYERS_DELETE:
                self.delete_player()
            elif choix == MENU_PLAYERS_EXIT:
                break

    def add_player(self):
        """ Method for recording new players """
        new_player = self.player_view.add_player()
        for player in new_player:
            player_to_add = PlayerModel(player[0], player[1], player[2], player[3])
            player_to_add.add_player()

    def delete_player(self):
        """ method to delete players """
        while True:
            all_player_list = self.player_model.search_all_players()
            if all_player_list == "no_result":
                self.player_view.choice("Aucun joueur, merci d'en créer. Appuyez sur [ENTRER] pour revenir au menu.")
                break
            elif all_player_list == "error":
                self.player_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                               " le et recommencez.")
                sys.exit()
            index_player_to_delete = self.player_view.delete_player(all_player_list)
            player_to_delete = all_player_list[index_player_to_delete]
            self.player_view.text_to_print("Utilisateur " + player_to_delete['fname'] + " "
                                           + player_to_delete['name'].capitalize() + " supprimé.")
            self.player_model.delete_player(player_to_delete['player_uuid'])
            choix = self.player_view.choice("Supprimer un autre joueur(O/n)?")
            if choix == "N":
                break

    def display_player(self):
        """ method to display players by selecting name or all players """
        while True:
            player_to_display = self.player_view.display_player()
            result = self.player_model.search_player(player_to_display)
            if result == "no_result" and not player_to_display == "display_all":
                choix = self.player_view.choice("Aucun résultat. Recommencer (O/n)? ")
                if choix == "N":
                    break
            elif result == "error":
                self.player_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                               " le et recommencez.")
                sys.exit()
            elif result == "no_result" and player_to_display == "display_all":
                result = self.player_model.search_all_players()
                if result == "no_result":
                    self.player_view.choice("Liste vide. Veuillez en créer. Appuyez sur [ENTRER] pour revenir"
                                            " au menu.")
                    break
                elif result == "error":
                    self.player_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                                   " le et recommencez.")
                    sys.exit()
                if (len(result)) == 1:
                    self.player_view.text_to_print(str(len(result)) + " résultat.")
                elif (len(result)) > 1:
                    self.player_view.text_to_print(str(len(result)) + " résultats.")
                for i in range(len(result)):
                    item = result[i]
                    self.player_view.text_to_print(PlayerModel(item['fname'].capitalize(), item['name'].capitalize(),
                                                               item['birthd'], item['clubid']))
                choix = self.player_view.choice("Faire une autre recherche (O/n)? ")
                if choix == "N":
                    break
            elif len(result) > 0:
                if len(result) == 1:
                    self.player_view.text_to_print(str(len(result)) + " résultat:")
                else:
                    self.player_view.text_to_print(str(len(result)) + " résultats:")
                for i in range(len(result)):
                    item = result[i]
                    self.player_view.text_to_print(PlayerModel(item['fname'].capitalize(), item['name'].capitalize(),
                                                               item['birthd'], item['clubid']))
                choix = self.player_view.choice("Faire une autre recherche (O/n)? ")
                if choix.upper() == "N":
                    break
