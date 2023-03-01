from controllers.base import ChessTournament


def main():
    """ launching starting here """
    tournament = ChessTournament()
    try:
        tournament.tournament_start()
    except KeyboardInterrupt:
        print("\n\nFin du script par l'utilisateur.\n")


if __name__ == "__main__":
    main()
