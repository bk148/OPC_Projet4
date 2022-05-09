from Controleur import Controller
from view import View

NAME = 'Nom'
RANK = 'Classement'

TOURNAMENT = 1
GAMERS = 2
REPORTS = 3
QUIT = 4

# Constante menu tournament
ADD_TOURNAMENT = 1
UPDATE_TOURNAMENT = 2
RUN_TOURNAMENT = 3
RETURN_GLOBAL_MENU_1 = 4

# Constante menu gamer
ADD_GAMER = 1
UPDATE_GAMER = 2
RETURN_GLOBAL_MENU_2 = 3

# Constante menu rapports
DISPLAY_GAMERS = 1
DISPLAY_TOURNAMENT_GAMERS = 2
DISPLAY_TOURNAMENTS = 3
DISPLAY_ROUND_MATCH_TOURNAMENT = 4
RETURN_GLOBAL_MENU_3 = 5

# Constante menu rapports gamer
DISPLAY_ALPHA_GAMERS = 1
DISPLAY_GAMERS_RANK = 2
RETURN_RAPPORTS_MENU_1 = 3

# Constante menu rapports gamer tournament
DISPLAY_TOURNAMENT_GAMERS_ALPHA = 1
DISPLAY_GAMERS_TOURNAMENT_RANK = 2
RETURN_MENU_REPPORTS_2 = 3

# Définition de la classe


class ControllerMenu:
    def __init__(self, view: View, controller: Controller):
        self.view = view
        self.controller = controller

    def execute(self):
        self.get_main_menu()

    def get_main_menu(self):
        self.view.clean_screen()
        self.view.ask_global_menu()
        option = self.view.ask_choice_menu()

        if option == TOURNAMENT:
            self.view.clean_screen()
            self.view.ask_tournament_menu()
            self.get_tournament_menu()
        elif option == GAMERS:
            self.view.clean_screen()
            self.view.ask_menu_gamer()
            self.get_gamer_menu()
        elif option == REPORTS:
            self.view.clean_screen()
            self.view.ask_menu_report()
            self.get_reports_menu()
        elif option == QUIT:
            quit()

    def get_tournament_menu(self):
        option = self.view.ask_choice_menu()

        if option == ADD_TOURNAMENT:
            self.controller.get_tournament_information()
            self.controller.models.save_tournament()
        elif option == UPDATE_TOURNAMENT:
            self.controller.update_tournament()
        elif option == RUN_TOURNAMENT:
            self.controller.run_tournament()
        elif option == RETURN_GLOBAL_MENU_1:
            self.get_main_menu()

    def get_gamer_menu(self):
        option = self.view.ask_choice_menu()

        if option == ADD_GAMER:
            self.controller.get_gamer_information()
            self.controller.models.save_gamers()
        elif option == UPDATE_GAMER:
            self.controller.update_gamer()
        elif option == RETURN_GLOBAL_MENU_2:
            self.get_main_menu()

    def get_reports_menu(self):
        option = self.view.ask_choice_menu()

        if option == DISPLAY_GAMERS:
            self.view.clean_screen()
            self.view.display_menu_gamers_list_report()
            self.choix_menu_rapport_liste_joueurs()
        elif option == DISPLAY_TOURNAMENT_GAMERS:
            self.view.clean_screen()
            self.view.display_menu_report_tournament_gamers_list()
            self.choix_menu_rapport_liste_joueurs_tournoi()
        elif option == DISPLAY_TOURNAMENTS:
            self.view.display_tournament_table(
                self.controller.get_tournament_table(NAME))
        elif option == DISPLAY_ROUND_MATCH_TOURNAMENT:
            self.controller.recuperer_ronde_match_tournoi()
        elif option == RETURN_GLOBAL_MENU_3:
            self.get_main_menu()

    def choix_menu_rapport_liste_joueurs(self):
        option = self.view.ask_choice_menu()
        if option == DISPLAY_ALPHA_GAMERS:
            self.view.display_gamer_table(
                self.controller.get_gamer_table(NAME))
        elif option == DISPLAY_GAMERS_RANK:
            self.view.display_gamer_table(
                self.controller.get_gamer_table(RANK, reverse=True))
        elif option == RETURN_RAPPORTS_MENU_1:
            self.view.clean_screen()
            self.view.ask_menu_report()
            self.get_reports_menu()

    def choix_menu_rapport_liste_joueurs_tournoi(self):
        option = self.view.ask_choice_menu()
        if option == DISPLAY_TOURNAMENT_GAMERS_ALPHA:
            self.view.display_gamers_tournament_table(
                self.controller.get_gamers_tounament(NAME))
        elif option == DISPLAY_GAMERS_TOURNAMENT_RANK:
            self.view.display_gamers_tournament_table(
                self.controller.get_gamers_tounament(RANK, reverse=True))
        elif option == RETURN_MENU_REPPORTS_2:
            self.view.clean_screen()
            self.view.ask_menu_report()
            self.get_reports_menu()
