from controllers.base import Tournament
import os

def main():
    """ launching starting here """

    """
    pre-req for correct launch
    verify if data/tournaments exists
    """
    data_folder = os.path.join("data", "tournaments")
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    tournament = Tournament()
    try:
        tournament.start_tournament()
    except KeyboardInterrupt:
        print("\n\nFin du script par l'utilisateur.\n")


if __name__ == "__main__":
    main()
