import os
import sys
from views.player import PlayerView
from models.player import PlayerModel
from constantes import MENU_PLAYER_CREATION, MENU_PLAYERS_DISPLAY, MENU_PLAYERS_DELETE, MENU_PLAYERS_EXIT

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data", "tournaments")
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
    with open(os.path.join(DATA_FOLDER, "players.json"), 'w') as players_file:
        pass
    players_file.close()
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data", "reports")
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
    with open(os.path.join(DATA_FOLDER, "report.html"), 'w') as report_file:
        pass
    report_file.close()


class PlayerController:
    """ Player controller """
    def __init__(self):
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

    @staticmethod
    def add_player():
        """ Method for recording new players """
        players_list = PlayerView.add_player()
        for player in players_list:
            player = PlayerModel(player_fname=player[0], player_name=player[1], player_birthd=player[2],
                                 player_clubid=player[3])
            player.save_player()

    @staticmethod
    def delete_player():
        """ method to delete players """
        while True:
            players_list = PlayerModel.search_all_players()
            if players_list == "no_result":
                PlayerView.choice("Aucun joueur, merci d'en créer. Appuyez sur [ENTRER] pour revenir au menu.")
                break
            elif players_list == "error":
                PlayerView.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                         " le et recommencez.")
                sys.exit()
            player_to_delete = PlayerView.delete_player(players_list)
            player_deleted = player_to_delete.delete_player()
            PlayerView.text_to_print("Utilisateur " + player_deleted + " supprimé.")
            choix = PlayerView.choice("Supprimer un autre joueur(O/n)?")
            if choix == "N":
                break

    @staticmethod
    def display_player():
        """ method to display players by selecting name or all players """
        while True:
            player_to_search = PlayerView.display_player()
            players_list = PlayerModel.search_player(player_to_search)

            # case when you specify a name with no result
            if players_list == "no_result" and not player_to_search == "display_all":
                choix = PlayerView.choice("Aucun résultat. Recommencer (O/n)? ")
                if choix == "N":
                    break

            # case of error structure file players.json
            elif players_list == "error":
                PlayerView.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                         " le et recommencez.")
                sys.exit()

            # case when you want to display all users [ENTER]
            elif players_list == "no_result" and player_to_search == "display_all":
                players_list = PlayerModel.search_all_players()
                if players_list == "no_result":
                    PlayerView.choice("Liste vide. Veuillez en créer. Appuyez sur [ENTRER] pour revenir"
                                      " au menu.")
                    break
                else:
                    PlayerView.text_to_print(str(len(players_list)) + " résultat(s).")
                    for player in players_list:
                        PlayerView.text_to_print(player)
                    choix = PlayerView.choice("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

            # case when you specify a name and there is some results
            elif len(players_list) > 0:
                PlayerView.text_to_print(str(len(players_list)) + " résultat(s):")
                for player in players_list:
                    PlayerView.text_to_print(player)
                choix = PlayerView.choice("Faire une autre recherche (O/n)? ")
                if choix.upper() == "N":
                    break
