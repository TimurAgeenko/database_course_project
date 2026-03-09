import psycopg2

from database_config.config import config


class DBManager:
    """Класс для взаимодействия с базой данных"""

    def __init__(self, db_name: str):
        self.__params = config()
        self.create_database(db_name)
        self.__conn = psycopg2.connect(database=db_name, **self.__params)

    def create_database(self, db_name: str):
        conn = psycopg2.connect(database="postgres", **self.__params)

        with conn.cursor() as cur:
            cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
            cur.execute(f"CREATE DATABASE {db_name}")

        conn.commit()
        conn.close()

    def close_conn(self):
        self.__conn.close()
