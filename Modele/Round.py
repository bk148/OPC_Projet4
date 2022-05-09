from rich import box
from rich.tree import Tree
from rich.table import Table

ID = 'ID'
NAME = 'Nom'
RANK = 'Classement'
SCORES_ROUNDS = 'Scores rondes'
SCORE_TOURNAMENT = 'Score du tournament'
ROUND = 'Round'
MATCH = 'Match'
BOLD = 'bold'


class Round:

    def __init__(self):
        self.gamers_a = []
        self.joueurs_b = []
        self.rounds = []
        self.counter_id = 0
        self.round_id = ''
        self.rounds_tree = Tree
        self.rounds_tree_match = Tree
        self.table_round_result = Table
        self.table_rounds = Table
        self.table_match = Table

    def create_round_table(self) -> [Table]:
        self.table_round_result = Table(box=box.HORIZONTALS, show_header=True, header_style=BOLD,
                                        title=self.round_id)
        self.table_round_result.add_column(ID)
        self.table_round_result.add_column(NAME)
        self.table_round_result.add_column(RANK)
        self.table_round_result.add_column(SCORES_ROUNDS)
        self.table_round_result.add_column(SCORE_TOURNAMENT)
        return self.table_round_result

    def get_round_table(self) -> [Table]:
        return self.table_round_result

    def create_round_tree(self) -> [Tree]:
        self.counter_id += 1
        self.round_id = f'{ROUND}{self.counter_id}'
        self.rounds_tree = Tree(label=self.round_id)
        return self.rounds_tree

    def use_round_tree(self) -> [Tree]:
        return self.rounds_tree

    def get_winner_tournament(self):
        return self.rounds[0][1]
