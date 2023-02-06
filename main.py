import os


def main():
    """ launching starting here """
    data_folder = os.path.join(os.path.dirname(__file__), "data", "tournaments")
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    from controllers.base import ChessTournament
    tournament = ChessTournament()
    try:
        tournament.Tournament_Start()
    except KeyboardInterrupt:
        print("\n\nFin du script par l'utilisateur.\n")


if __name__ == "__main__":
    """
    pre-req for correct launch
    verify if data/tournaments exists
    """
    main()
