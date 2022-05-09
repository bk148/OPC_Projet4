from operator import itemgetter
from rich.table import Table
from rich.tree import Tree
from tinydb import TinyDB

SORT_ORDER = 1
NAME = 'Nom'
FIRSTNAME = 'Prenom'
PLACE = 'Lieu'
TIME_CONTROL = 'Controle du temps'
SEX = 'Sexe'
BIRTH_DATE = 'Date de naissance'
RANK = 'Classement'
TOURNAMENT_DATE = 'Date du tournament'
DESCRIPTION = 'Description'
RANK_TITLE = 2
SORT_VICTORY = 3
GAMERS_TOURNAMENT = 'Joueurs du tournament'
GAMERS = 'Joueurs'
ROUND = 'Round'
WIN = 1
LOSE = 2
NUL = 3
WIN_MATCHED = 1
LOSED_MATCH = 0
NUL_MATCH = 2
NUL_MATCH_ = 0.5
GAMER_A = 0
GAMER_B = 1
GAMER_NAME = 3
TOURNAMENT_SCORE = 4
GAMER_RANK = 2
ROUND_ID_GAMER = 0
ROUND_GAMER_NAME = 1
ROUND_RANK_GAMER = 2
ROUND_SCORES_MATCH_GAMER = 3
ROUND_TOTAL_SCORE_GAMER = 4
ODD = 2
EVEN = 0
START = 0
START_ROUND = 1
ADD_ROUND = 1
COUNTER = 1
NO_WINNER = 'MATCH NUL'
MATCH = 'Match'


class Controller:

    def __init__(self, view, models):
        self.view = view
        self.models = models

    def get_gamer_information(self):
        self.view.clean_screen()
        self.models.gamer.lastname = self.view.ask_gamer_last_name()
        self.models.gamer.firstname = self.view.ask_gamer_first_name()
        self.models.gamer.birth_date = self.view.ask_gamer_birth_date()
        self.models.gamer.sex = self.view.ask_gamer_sex()
        self.models.gamer.rank = self.view.ask_gamer_rank()

    def get_tournament_information(self):
        self.view.clean_screen()
        self.models.tournament.name = self.view.ask_tournament_name()
        self.models.tournament.place = self.view.ask_tournament_place()
        self.models.tournament.date = self.view.ask_tournament_date()
        self.models.tournament.time_control = self.view.ask_time_control_tournament()
        self.models.tournament.description = self.view.ask_tournament_description()

    def update_gamer(self):
        self.view.clean_screen()
        self.view.display_gamer_table(self.get_gamer_table(NAME))
        gamer_id = self.view.ask_id()
        validation = self.view.ask_validation()
        if validation:
            self.get_gamer_information()
            self.models.save_updated_gamer(gamer_id)
        if not validation:
            self.view.display_canceled_update()
            self.view.pause_screen()

    def update_tournament(self):
        self.view.clean_screen()
        self.view.display_tournament_table(self.get_tournament_table(NAME))
        tournament_id = self.view.ask_id()
        validation = self.view.ask_validation()
        if validation:
            self.get_tournament_information()
            self.models.save_tournament_update(tournament_id)
        if not validation:
            self.view.display_canceled_update()
            self.view.pause_screen()

    def get_gamers_tounament(self, trie, reverse=False) -> [Table]:
        self.view.clean_screen()
        self.view.display_tournament_table(self.get_tournament_table(NAME))
        tournament_id = self.view.ask_id()
        self.models.tournament.create_gamers_tournament_table()
        for tournament in self.models.db_tournament_table:
            if tournament_id == tournament.doc_id:
                for gamer in self.sort_table(self.models.db_gamer_table, trie, reverse):
                    for gamer_tournament in tournament[GAMERS_TOURNAMENT]:
                        if gamer.doc_id == gamer_tournament:
                            self.models.tournament.get_gamers_tournament_table().add_row(
                                str(gamer_tournament),
                                str(gamer[NAME]),
                                str(gamer[RANK]))
        return self.models.tournament.get_gamers_tournament_table()

    def recuperer_ronde_match_tournoi(self):
        score = -1
        self.view.display_tournament_table(self.get_tournament_table(NAME))
        tournament_id = self.view.ask_id()
        tournament = self.models.db_tournament_table.get(doc_id=tournament_id)
        for round_id in range(START_ROUND, self.models.tournament.max_rounds_count + ADD_ROUND):
            match_id = START
            score += COUNTER
            self.models.match.create_round_match_tournament_table(f'{ROUND}{round_id}')
            for match in tournament[f'{ROUND}{round_id}']:
                for resultat in range(score, len(match[GAMER_A][ROUND_SCORES_MATCH_GAMER])):
                    match_id += COUNTER
                    score_match = match[GAMER_A][ROUND_SCORES_MATCH_GAMER][score]
                    if score_match == LOSED_MATCH:
                        self.models.match.get_round_match_tournament_table().add_row(
                            str(f'{match_id}'),
                            match[GAMER_A][ROUND_GAMER_NAME],
                            match[GAMER_B][ROUND_GAMER_NAME],
                            match[GAMER_B][ROUND_GAMER_NAME])
                    elif score_match == WIN_MATCHED:
                        self.models.match.get_round_match_tournament_table().add_row(
                            str(f'{match_id}'),
                            match[GAMER_A][ROUND_GAMER_NAME],
                            match[GAMER_B][ROUND_GAMER_NAME],
                            match[GAMER_A][ROUND_GAMER_NAME])
                    elif score_match == NUL_MATCH_:
                        self.models.match.get_round_match_tournament_table().add_row(
                            str(f'{match_id}'),
                            match[GAMER_A][ROUND_GAMER_NAME],
                            match[GAMER_B][ROUND_GAMER_NAME],
                            NO_WINNER)
            self.view.display_round_match_tournament_table(
                self.models.match.get_round_match_tournament_table())
        self.view.pause_screen()

    @staticmethod
    def sort_table(table, trie, reverse=False) -> [TinyDB.table]:
        sorted_table = (sorted(table, key=itemgetter(trie), reverse=reverse))
        return sorted_table

    def get_gamer_table(self, trie, reverse=False) -> [Table]:
        self.models.gamer.create_gamer_table()
        for gamer in self.sort_table(self.models.db_gamer_table, trie, reverse):
            self.models.gamer.get_gamer_table().add_row(
                str(gamer.doc_id),
                gamer[NAME],
                gamer[FIRSTNAME],
                gamer[BIRTH_DATE],
                gamer[SEX],
                str(gamer[RANK]))
        return self.models.gamer.get_gamer_table()

    def get_tournament_table(self, trie) -> [Table]:
        self.models.tournament.create_tournament_table()
        for tournament in self.sort_table(self.models.db_tournament_table, trie):
            self.models.tournament.get_tounament_table().add_row(
                str(tournament.doc_id),
                tournament[NAME],
                tournament[PLACE],
                tournament[TIME_CONTROL],
                tournament[TOURNAMENT_DATE],
                tournament[DESCRIPTION])
        return self.models.tournament.get_tounament_table()

    def get_round_table(self) -> [Table]:
        self.models.round.create_round_table()
        for gamer in self.models.round.rounds:
            self.models.round.get_round_table().add_row(
                str(gamer[ROUND_ID_GAMER]),
                str(gamer[ROUND_GAMER_NAME]),
                str(gamer[ROUND_RANK_GAMER]),
                str(gamer[ROUND_SCORES_MATCH_GAMER]),
                str(gamer[ROUND_TOTAL_SCORE_GAMER])
            )
        return self.models.round.get_round_table()

    def get_round_tree(self) -> [Tree]:
        self.models.round.create_round_tree()
        for match_id in range(len(self.models.round.rounds)):
            self.models.match.create_match_tree(self.models.round.rounds_tree, match_id)
            self.models.match.get_match_tree().add(
                f'{self.models.round.rounds[match_id][GAMER_A][ROUND_GAMER_NAME]}')
            self.models.match.get_match_tree().add(
                f'{self.models.round.rounds[match_id][GAMER_B][ROUND_GAMER_NAME]}')
        return self.models.round.use_round_tree()

    def get_match_tree(self):
        for match_id in range(len(self.models.round.rounds)):
            self.view.display_match_tree(
                self.models.match.create_tree_result_match(
                    self.models.round.rounds, match_id))
            self.view.display_gamer_match_winner()
            gamer_result = self.view.ask_match_result()

            if gamer_result == WIN:
                self.models.round.rounds[match_id][GAMER_A][GAMER_NAME].append(
                    self.models.match.match_result[WIN_MATCHED])
                self.models.round.rounds[match_id][GAMER_B][GAMER_NAME].append(
                    self.models.match.match_result[LOSED_MATCH])

            elif gamer_result == LOSE:
                self.models.round.rounds[match_id][GAMER_A][GAMER_NAME].append(
                    self.models.match.match_result[LOSED_MATCH])
                self.models.round.rounds[match_id][GAMER_B][GAMER_NAME].append(
                    self.models.match.match_result[WIN_MATCHED])

            elif gamer_result == NUL:
                self.models.round.rounds[match_id][GAMER_A][GAMER_NAME].append(
                    self.models.match.match_result[NUL_MATCH])
                self.models.round.rounds[match_id][GAMER_B][GAMER_NAME].append(
                    self.models.match.match_result[NUL_MATCH])

    def sort_gamers_tournament_win(self) -> [list]:
        gamer_tournament_sort = []
        for match in self.models.round.rounds:
            for gamer in match:
                gamer_tournament_sort.append(
                    [gamer[ROUND_ID_GAMER],
                     gamer[ROUND_GAMER_NAME],
                     gamer[ROUND_RANK_GAMER],
                     gamer[ROUND_SCORES_MATCH_GAMER],
                     sum(gamer[ROUND_SCORES_MATCH_GAMER])])
        self.models.round.rounds.clear()
        self.models.round.rounds = sorted(gamer_tournament_sort, key=itemgetter(
            TOURNAMENT_SCORE, GAMER_RANK), reverse=True)
        return self.models.round.rounds

    def sort_gamers_tournament_rank(self) -> [list]:
        gamer_tournament_sort = []
        for gamer_id in self.models.tournament.gamers:
            for gamer in self.models.db_gamer_table:
                if gamer_id == gamer.doc_id:
                    gamer_tournament_sort.append([
                        gamer_id,
                        gamer[NAME],
                        gamer[RANK],
                        []
                    ])
        self.models.tournament.sort_gamers_by_rank = sorted(
            gamer_tournament_sort, key=itemgetter(RANK_TITLE), reverse=True)
        return self.models.tournament.sort_gamers_by_rank

    def get_first_round(self) -> [list]:
        gamer_index = (self.models.tournament.max_gamers_count / ODD)
        self.models.round.gamers_a = self.models.tournament.sort_gamers_by_rank[:int(gamer_index)]
        self.models.round.gamers_b = self.models.tournament.sort_gamers_by_rank[int(gamer_index):]
        for gamer_a, gamer_b in zip(self.models.round.gamers_a, self.models.round.gamers_b):
            self.models.round.rounds.append([gamer_a, gamer_b])
        return self.models.round.rounds

    def create_round(self) -> [list]:
        self.models.round.gamers_a.clear()
        self.models.round.gamers_b.clear()
        for index, gamer in enumerate(self.models.round.rounds):
            if index % ODD != EVEN:
                self.models.round.gamers_a.append(gamer)
            else:
                self.models.round.gamers_b.append(gamer)
        self.models.round.rounds.clear()
        for joueur_a, joueur_b in zip(self.models.round.gamers_a, self.models.round.gamers_b):
            self.models.round.rounds.append([joueur_a, joueur_b])
        return self.models.round.rounds

    def add_gamers_tournament(self) -> [list]:
        self.view.clean_screen()
        self.view.display_tournament_table(self.get_tournament_table(NAME))
        self.models.tournament.id = self.view.ask_id()
        self.view.ask_gamers_tournament_max()
        self.models.save_tournament_max_gamer(self.models.tournament.id)
        self.view.ask_rounds_tournament_max()
        self.models.save_tournament_max_round(self.models.tournament.id)
        self.view.clean_screen()
        self.view.display_gamer_table(self.get_gamer_table(RANK, reverse=True))
        self.view.display_add_gamers_tournament()
        for competiteur in range(START, self.models.tournament.max_gamers_count):
            gamer_id = self.view.ask_id()
            self.models.tournament.gamers.append(gamer_id)
        return self.models.tournament.gamers

    def run_tournament(self):
        self.add_gamers_tournament()
        self.models.save_tournament_gamers(self.models.tournament.id)
        self.sort_gamers_tournament_rank()
        self.get_first_round()
        self.view.display_round_tree(self.get_round_tree())
        self.get_match_tree()
        self.models.save_tournament_round(self.models.tournament.id)
        self.sort_gamers_tournament_win()
        self.view.display_round_table(self.get_round_table())
        for nouvelle_ronde in range(START_ROUND, self.models.tournament.max_rounds_count):
            self.create_round()
            self.view.display_round_tree(self.get_round_tree())
            self.get_match_tree()
            self.models.save_tournament_round(self.models.tournament.id)
            self.sort_gamers_tournament_win()
            self.view.display_round_table(self.get_round_table())
        self.view.display_gamer_tournament(self.models.round.get_winner_tournament())
