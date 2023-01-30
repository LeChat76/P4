import datetime
from views.menu import Menu
from models.player import Player


class Controller:
    """ Main controller """

    """
    premier tour : mélanger les joueurs aléatoirement
    ensuite, chaque paire de joueurs est géré de la façon suivante:
        * triez les joueurs par points
        * associez les joueurs par paire et par ordre de points (si joueurs avec même nb de points, choix aléatoire)
        * NE PAS GENERER DE PAIRE AYANT DEJA JOUE ENSEMBLE
        * choix de la couleur tiré au sort (le menu doit donc demander qui a noir et qui a blanc)
    """

    def create_player_list(self):
        """ Request for players """
        player_fname = None
        player_name = None
        player_birthd = None
        player_clubid = None
        new_player = True

        menu = Menu()

        while new_player:
            player_fname = None
            while not player_fname:
                player_fname = menu.prompt_player_fname()
                if player_fname == "":                 # juste pour debugging, à supprimer
                    player_fname = "cedric"             # juste pour debugging, à supprimer

            player_name = None
            while not player_name:
                player_name = menu.prompt_player_name()
                if player_name == "":                  # juste pour debugging, à supprimer
                    player_name = "delauney"            # juste pour debugging, à supprimer

            player_birthd = None
            while not player_birthd:
                while True:
                    player_birthd = menu.prompt_player_birthd()
                    if player_birthd == "":            # juste pour debugging, à supprimer
                        player_birthd = "16/07/1975"    # juste pour debugging, à supprimer
                    try:
                        datetime.datetime.strptime(player_birthd, '%d/%m/%Y')
                    except ValueError:
                        print("Mauvais format de date. Merci de ressaisir.")
                    else:
                        break

            player_clubid = None
            while not player_clubid:
                while True:
                    player_clubid = menu.prompt_player_clubid()
                    if player_clubid == "":            # juste pour debugging, à supprimer
                        player_clubid = "ab12345"       # juste pour debugging, à supprimer
                    if len(player_clubid) != 7:
                        print("Le club ID doit comporter 7 caractères. Merci de ressaisir.")
                    elif not player_clubid[:2].isalpha():
                        print("Les 2 premiers caractères doivent être des lettres. Merci de ressaisir.")
                    elif not player_clubid[2:].isnumeric():
                        print("les 5 derniers caractères doivent être des chiffres. Merci de ressaisir.")
                    else:
                        break

            new_player = menu.prompt_add_player()
            if new_player == "":
                new_player = True
            elif new_player.upper() == "O":
                new_player = True
            elif new_player.upper() == "N":
                new_player = False

            player = Player(player_fname.capitalize(), player_name.capitalize(), player_birthd, player_clubid.upper())
            print(player)

    def create_ran_player_list(self):
        pass
