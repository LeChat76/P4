from views.result import ResultView

RESULT_VIEW = ResultView()
MENU_RESULT_TOURNAMENT = 1
MENU_RESULT_PLAYER = 2
MENU_RESULT_EXIT = 3


class ResultController:

    @staticmethod
    def menu_3():
        """ Results menu """
        while True:
            choix = RESULT_VIEW.result_menu()
            if choix == MENU_RESULT_TOURNAMENT:
                pass
            elif choix == MENU_RESULT_PLAYER:
                pass
            elif choix == MENU_RESULT_EXIT:
                break
