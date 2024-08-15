import sqlite3
from database.queries import Queries


class Database:
    def __init__(self, path):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as connection:
            connection.execute(Queries.CREATE_TABLE)

            connection.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as connection:
            connection.execute(query, params)

            connection.commit()
