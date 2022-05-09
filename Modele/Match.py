from rich.tree import Tree
from rich.table import Table
from rich import box

WINNED_MATCH = 1
LOSED_MATCH = 0
NUL_MATCH = 0.5
MATCH = 'Match'
COUNTER = 1
GAMER_A = 0
GAMER_B = 1
MATCH_PLAYER_NAME = 1
BOLD = 'Bold'
NAME_GAMER_A = 'Gamer A'
NAME_GAMER_B = 'Gamer B'
WINNER = 'Vainqueur'


class Match:

    def __init__(self):
        self.match_result = [LOSED_MATCH, WINNED_MATCH, NUL_MATCH]
        self.match_tree = Tree
        self.tree_result_match = Tree
        self.tree_round_match_tournament = Table

    def create_match_tree(self, round, id_match) -> [Tree]:
        self.match_tree = round.add(f'{MATCH}{id_match + COUNTER}')
        return self.match_tree

    def get_match_tree(self) -> [Tree]:
        return self.match_tree

    def create_tree_result_match(self, round, id_match) -> [Tree]:
        self.tree_result_match = Tree(f'\n{MATCH}{id_match + 1}')
        self.tree_result_match.add(f'{round[id_match][GAMER_A][MATCH_PLAYER_NAME]}')
        self.tree_result_match.add(f'{round[id_match][GAMER_B][MATCH_PLAYER_NAME]}')
        return self.tree_result_match

    def get_match_tree_result(self) -> [Tree]:
        return self.tree_result_match

    def create_round_match_tournament_table(self, round_id) -> [Table]:
        self.tree_round_match_tournament = Table(box=box.HORIZONTALS, show_header=True, header_style=BOLD,
                                                 title=round_id)
        self.tree_round_match_tournament.add_column(MATCH)
        self.tree_round_match_tournament.add_column(NAME_GAMER_A)
        self.tree_round_match_tournament.add_column(NAME_GAMER_B)
        self.tree_round_match_tournament.add_column(WINNER)
        return self.tree_round_match_tournament

    def get_round_match_tournament_table(self) -> [Table]:
        return self.tree_round_match_tournament
