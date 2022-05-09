import os
from rich.console import Console
from rich.prompt import Prompt
from rich.prompt import IntPrompt
from rich.panel import Panel

CONTINUE = '\nAppuyer sur entrer pour continuer'
CANCELED_UPDATE = '\nModification annulé'
GAMER_WINNED_MATCH = 'Quel gamer remporte le match ?'
GAMER_NAME = 'Nom de famille du gamer: '
GAMER_FIRST_NAME = 'Prenom du gamer: '
GAMER_SEX = '[0] = Masculin || [1] = Féminin: '
GAMER_BIRTH_DATE = 'Date de naissance JJ-MM-AAAA: '
GAMER_RANK = 'Classement du gamer: '
TOURNAMENT_NAME = 'Nom du Tournament: '
TOURNAMENT_PLACE = 'Lieu du Tournament: '
TOURNAMENT_DATE = 'Date du tournament JJ-MM-AAAA: '
TOURNAMENT_TIME_CONTROL = '[0] = Bullet || [1] = Blitz || [2] = Coup rapide :'
TOURNAMENT_DESCRIPTION = 'Description du Tournament: '
GAMERS_NUMBER_CHOICE = 'Choisir un nombre de joueurs maximum pour le tournament: '
GAMERS_NUMBER_ROUND_CHOICE = 'Choisir le nombre de round maximum pour le tournament: '
ADMIN_CHOICE_ID = 'Choisir un ID: '
ADMIN_VALIDATION = 'Voulez vous modifier les informations [blue]o[/blue] ou [red]n[/red]: '
TOURNAMENT_DATEE = 'Date du tournament'
GAMER_WINNER_MENU = '\n[1] Gamer 1 || [2] Gamer 2 || [3] Match Nul: '
ADD_GAMER_TOURNAMENT = '\nAjouter 8 ID de joueurs au tournament: '
WINNER = 'Le gagnant du tournament est: '

class View(Console):

    def __init__(self, view):
        Console.__init__(self)
        self.view = view
        self.entrer_str = Prompt
        self.entrer_int = IntPrompt

    @staticmethod
    def clean_screen():
        #os.system('cls')
        os.system('clear')

    def pause_screen(self) -> [None]:
        self.display_continue()
        input()

    def ask_global_menu(self) -> None:
        return self.view.global_menu()

    def ask_tournament_menu(self) -> None:
        return self.view.tournament_menu()

    def ask_menu_gamer(self) -> None:
        return self.view.gamer_menu()

    def ask_menu_report(self) -> None:
        return self.view.report_menu()

    def display_menu_gamers_list_report(self) -> None:
        return self.view.gamers_list_report_menu()

    def display_menu_report_tournament_gamers_list(self) -> None:
        return self.view.gamers_list_report_tournament_menu()

    def ask_choice_menu(self) -> [int]:
        return self.entrer_int.ask()

    def display_continue(self) -> None:
        self.print(Panel.fit(CONTINUE))

    def display_canceled_update(self) -> None:
        self.print(Panel.fit(CANCELED_UPDATE))

    def display_gamer_match_winner(self) -> None:
        self.print(Panel.fit(GAMER_WINNED_MATCH))

    def display_add_gamers_tournament(self) -> None:
        self.print(Panel.fit(ADD_GAMER_TOURNAMENT))

    def display_gamer_tournament(self, winner_gamer) -> None:
        self.clean_screen()
        self.print(Panel.fit(f'{WINNER}{winner_gamer}'))
        self.pause_screen()

    def display_gamer_table(self, table) -> None:
        self.clean_screen()
        self.print(table)
        self.pause_screen()

    def display_tournament_table(self, table) -> None:
        self.clean_screen()
        self.print(table)
        self.pause_screen()

    def display_round_table(self, table) -> None:
        self.clean_screen()
        self.print(table)
        self.pause_screen()

    def display_match_table(self, table) -> None:
        self.clean_screen()
        self.print(table)
        self.pause_screen()

    def display_gamers_tournament_table(self, table) -> None:
        self.clean_screen()
        self.print(table)
        self.pause_screen()

    def display_round_match_tournament_table(self, table) -> None:
        self.print(table)

    def display_round_tree(self, tree) -> None:
        self.clean_screen()
        self.print(tree)
        self.pause_screen()

    def display_match_tree(self, tree) -> None:
        self.clean_screen()
        self.print(tree)

    def ask_gamer_last_name(self) -> [str]:
        return self.entrer_str.ask(GAMER_NAME)

    def ask_gamer_first_name(self) -> [str]:
        return self.entrer_str.ask(GAMER_FIRST_NAME)

    def ask_gamer_sex(self) -> [int]:
        return self.entrer_int.ask(GAMER_SEX)

    def ask_gamer_birth_date(self) -> [str]:
        return self.entrer_str.ask(GAMER_BIRTH_DATE)

    def ask_gamer_rank(self) -> [int]:
        return self.entrer_int.ask(GAMER_RANK)

    def ask_tournament_name(self) -> [str]:
        return self.entrer_str.ask(TOURNAMENT_NAME)

    def ask_tournament_place(self) -> [str]:
        return self.entrer_str.ask(TOURNAMENT_PLACE)

    def ask_tournament_date(self) -> [str]:
        return self.entrer_str.ask(TOURNAMENT_DATE)

    def ask_time_control_tournament(self) -> [int]:
        return self.entrer_int.ask(TOURNAMENT_TIME_CONTROL)

    def ask_tournament_description(self) -> [str]:
        return self.entrer_str.ask(TOURNAMENT_DESCRIPTION)

    def ask_id(self) -> [int]:
        return self.entrer_int.ask(ADMIN_CHOICE_ID)

    def ask_validation(self) -> [int]:
        validation = self.entrer_str.ask(ADMIN_VALIDATION)
        if validation == "n":
            return False
        return True

    def ask_match_result(self) -> [int]:
        return self.entrer_int.ask(GAMER_WINNER_MENU)

    def ask_gamers_tournament_max(self) -> [int]:
        return self.entrer_str.ask(GAMERS_NUMBER_CHOICE)

    def ask_rounds_tournament_max(self) -> [int]:
        return self.entrer_int.ask(GAMERS_NUMBER_ROUND_CHOICE)


class MenuView(Console):
    def __init__(self):
        Console.__init__(self)

    def global_menu(self) -> None:
        self.print('[1] Tournois')
        self.print('[2] Joueurs')
        self.print('[3] Rapports')
        self.print('[4] Quitter')

    def tournament_menu(self) -> None:
        self.print('[1] Ajouter un tournament')
        self.print('[2] Modifier un tournament')
        self.print('[3] Lancer Tournament')
        self.print('[4] Retour')

    def gamer_menu(self) -> None:
        self.print('[1] Ajouter un gamer')
        self.print('[2] Modifier un gamer')
        self.print('[3] Retour')

    def report_menu(self) -> None:
        self.print('[1] Liste de tous les joueurs')
        self.print("[2] Liste de tous les joueurs d'un tournament")
        self.print('[3] Liste de tous les tournois')
        self.print("[4] Liste des rondes et des match d'un tournament")
        self.print("[5] Retour")

    def gamers_list_report_menu(self) -> None:
        self.print('[1] Liste de tous les joueurs par ordre alphabétique')
        self.print('[2] Liste de tous les joueurs par rank')
        self.print('[3] Retour')

    def gamers_list_report_tournament_menu(self) -> None:
        self.print('[1] Liste de tous les joueurs du tournament par ordre alphabétique')
        self.print('[2] Liste de tous les joueurs du tournament par rank')
        self.print('[3] Retour')
