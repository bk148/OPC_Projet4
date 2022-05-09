from rich.table import Table
from rich import box

NAME = 'Nom'
PLACE = 'Lieu'
TOURNAMENT_DATE = 'Date du tournament'
TIME_CONTROL = 'Controle du temps'
DESCRIPTION = 'Description'
TOURNAMENT_GAMERS = 'Joueurs du tournament'
COUNTER = 1
BOLD = 'bold'
TITLE_TOUNAMENT_TABLE = 'Tournament enregistré'
ID = 'ID'
FIRSTNAME = 'Prenom'
BIRTH_DATE = 'Date de naissance'
SEX = 'Sexe'
RANK = 'Classement'
MAX_GAMER = 'Gamer maximum'
ROUND_MAX = 'Round maximum'


class Tournament:
    TIME_CONTROL = ["Bullet", "Blitz", "Coup Rapide"]

    def __init__(self,
                 count_round_max=4,
                 count_gamer_max=8):
        self.name = ''
        self.place = ''
        self.date = ''
        self.time_control = 0
        self.description = ''
        self.max_rounds_count = count_round_max
        self.max_gamers_count = count_gamer_max
        self.gamers = []
        self.id = 0
        self.sort_gamers_by_rank = []
        self.dict_t = {}
        self.tabt = Table
        self.table_gamers = Table

    def dict_tournament(self) -> [dict]:
        self.name = self.name.upper()
        self.place = self.place.upper()
        self.description = self.description.capitalize()
        self.time_control = Tournament.TIME_CONTROL[self.time_control]
        self.dict_t = {NAME: self.name,
                       PLACE: self.place,
                       TOURNAMENT_DATE: self.date,
                       TIME_CONTROL: self.time_control,
                       DESCRIPTION: self.description,
                       TOURNAMENT_GAMERS: self.gamers,
                       MAX_GAMER: self.max_gamers_count,
                       ROUND_MAX: self.max_rounds_count}
        return self.dict_t

    def create_tournament_table(self) -> [Table]:
        self.tabt = Table(box=box.HORIZONTALS,
                          show_header=True,
                          header_style=BOLD,
                          title=TITLE_TOUNAMENT_TABLE)
        self.tabt.add_column(ID)
        self.tabt.add_column(NAME)
        self.tabt.add_column(PLACE)
        self.tabt.add_column(TIME_CONTROL)
        self.tabt.add_column(TOURNAMENT_DATE)
        self.tabt.add_column(DESCRIPTION)
        return self.tabt

    def get_tounament_table(self) -> [Table]:
        return self.tabt

    def get_tournament_id(self) -> [int]:
        return self.id

    def create_gamers_tournament_table(self) -> [Table]:
        self.table_gamers = Table(box=box.HORIZONTALS,
                                  show_header=True,
                                  header_style=BOLD,
                                  title=TOURNAMENT_GAMERS)
        self.table_gamers.add_column(ID)
        self.table_gamers.add_column(NAME)
        self.table_gamers.add_column(RANK)
        return self.table_gamers

    def get_gamers_tournament_table(self) -> [Table]:
        return self.table_gamers
