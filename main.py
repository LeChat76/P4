import os


def main():
    """ launching starting here """
    from controllers.base import ChessTournament
    tournament = ChessTournament()
    try:
        tournament.tournament_start()
    except KeyboardInterrupt:
        print("\n\nFin du script par l'utilisateur.\n")


if __name__ == "__main__":
    DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data",
                               "tournaments")
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
        with open(os.path.join(DATA_FOLDER, "players.json"), 'w')\
                as players_file:
            players_file.write("")
        with open(os.path.join(DATA_FOLDER, "tournaments.json"), 'w')\
                as tournaments_file:
            tournaments_file.write("")
    main()
