from controllers.base import Tournament


def main():
    tournament = Tournament()
    try:
        tournament.start_tournament()
    except KeyboardInterrupt:
        print("\n\nFin du script par l'utilisateur.\n")


if __name__ == "__main__":
    main()
