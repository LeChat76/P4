import os


def main():
    """ launching starting here """
    tournament = ChessTournament()
    try:
        tournament.tournament_start()
    except KeyboardInterrupt:
        print("\n\nFin du script par l'utilisateur.\n")


if __name__ == "__main__":
    DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data", "tournaments")
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
        with open(os.path.join(DATA_FOLDER, "players.json")):
            pass
        with open(os.path.join(DATA_FOLDER, "tournaments.json")):
            pass
    from controllers.base import ChessTournament
    main()
