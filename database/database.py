import sqlite3
from database.queries import Queries


class Database:
    def __init__(self, path):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as connection:
            connection.execute(Queries.CREATE_TABLE)
            connection.execute(Queries.DROP_FOOD_CATEGORIES_TABLE)
            connection.execute(Queries.CREATE_FOOD_CATEGORIES_TABLE)
            connection.execute(Queries.POPULATE_FOOD_CATEGORIES)
            connection.execute(Queries.DROP_MENU_TABLE)
            connection.execute(Queries.CREATE_MENU_TABLE)
            connection.execute(Queries.POPULATE_MENU)

            connection.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as connection:
            if params:
                connection.execute(query, params)
            else:
                connection.execute(query)

            connection.commit()

    def fetch(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as connection:
            if params:
                result = connection.execute(query, params)
            else:
                result = connection.execute(query)
            return result.fetchall()

