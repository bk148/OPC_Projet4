from tinydb import TinyDB
from tinydb import table
from tinydb import Query
LASTNAME = 'Nom'
PLACE = 'Lieu'
TOURNAMENT_DATE = 'Date du tournament'
TIME_CONTROL = 'Controle du temps'
DESCRIPTION = 'Description'
TOURNAMENT_GAMERS = 'Joueurs du tournament'
FIRST_NAME = 'Prenom'
BIRTH_DATE = 'Date de naissance'
SEX = 'Sexe'
RANK = 'Classement'
MAX_GAMER = 'Gamer maximum'
ROUND_MAX = 'Round maximum'
GAMERS = 'Joueurs'
TOURNAMENT = 'Tournament'
LAST_NAME_BDD = 'db_tournament.json'


class Models:

    def __init__(self, tournament, gamer, round, match):
        self.tournament = tournament
        self.gamer = gamer
        self.round = round
        self.match = match
        self.db_master = TinyDB(LAST_NAME_BDD)
        self.db_tournament_table = self.db_master.table(TOURNAMENT)
        self.db_gamer_table = self.db_master.table(GAMERS)
        self.query = Query()

    def save_tournament(self) -> [TinyDB.table]:
        self.db_tournament_table.insert_multiple([self.tournament.dict_tournament()])
        return self.db_tournament_table

    def save_gamers(self) -> [TinyDB.table]:
        self.db_gamer_table.insert_multiple([self.gamer.get_gamer_dict()])
        return self.db_gamer_table

    def save_tournament_round(self, tournament_id):
        self.db_tournament_table.upsert(table.Document({self.round.round_id:
                                                    self.round.rounds}, doc_id=tournament_id))

    def save_tournament_gamers(self, tournament_id):
        self.db_tournament_table.upsert(table.Document({TOURNAMENT_GAMERS:
                                                    self.tournament.gamers}, doc_id=tournament_id))

    def save_tournament_max_gamer(self, tournament_id):
        self.db_tournament_table.upsert(table.Document({MAX_GAMER:
                                                    self.tournament.max_gamers_count}, doc_id=tournament_id))

    def save_tournament_max_round(self, tournament_id):
        self.db_tournament_table.upsert(table.Document({ROUND_MAX:
                                                    self.tournament.max_rounds_count}, doc_id=tournament_id))

    def save_tournament_update(self, tournament_id):
        self.db_tournament_table.update(self.tournament.dict_tournament(), doc_ids=[tournament_id])

    def save_updated_gamer(self, gamer_id):
        self.db_gamer_table.update(self.gamer.get_gamer_dict(), doc_ids=[gamer_id])
