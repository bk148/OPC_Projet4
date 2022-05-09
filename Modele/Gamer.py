from rich.table import Table
from rich import box

LASTNAME = 'Nom'
FIRSTNAME = 'Prenom'
BIRTH_DTAE = 'Date de naissance'
SEXS = 'Sexe'
RANKS = 'Classement'
COUNTER = 1
BOLD = 'bold'
TITLE_GAMERS_TABLE = 'Joueurs enregistré'
ID = 'ID'


class Gamer:
    SEXS = ['Masculin', 'Feminin']

    def __init__(self):
        self.lastname = ''
        self.firstname = ''
        self.birth_date = ''
        self.sex = 0
        self.rank = 0
        self.dict_gamers = {}
        self.gamers_table = Table

    def create_gamer_table(self) -> [Table]:
        self.gamers_table = Table(box=box.HORIZONTALS,
                                  show_header=True,
                                  header_style=BOLD,
                                  title=TITLE_GAMERS_TABLE)
        self.gamers_table.add_column(ID)
        self.gamers_table.add_column(LASTNAME)
        self.gamers_table.add_column(FIRSTNAME)
        self.gamers_table.add_column(BIRTH_DTAE)
        self.gamers_table.add_column(SEXS)
        self.gamers_table.add_column(RANKS)
        return self.gamers_table

    def get_gamer_table(self) -> [Table]:
        return self.gamers_table

    def get_gamer_dict(self) -> [dict]:
        self.lastname = self.lastname.upper()
        self.firstname = self.firstname.capitalize()
        self.sex = Gamer.SEXS[self.sex]
        self.dict_gamers = {
            LASTNAME: self.lastname,
            FIRSTNAME: self.firstname,
            BIRTH_DTAE: self.birth_date,
            SEXS: self.sex,
            RANKS: self.rank}
        return self.dict_gamers
