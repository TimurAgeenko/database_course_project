import psycopg2

from src.config import config


class DBManager:
    """Класс для взаимодействия с базой данных"""

    def __init__(self, db_name: str, path: str = "../database.ini"):
        self.__params = config(filename=path)
        self.create_database(db_name)
        self.__conn = psycopg2.connect(database=db_name, **self.__params)
        self.create_tables()

    def close_conn(self) -> None:
        """Метод для закрытия связи с базой данных."""
        self.__conn.close()

    def create_database(self, db_name: str) -> None:
        """Метод для создания базы данных."""
        conn = psycopg2.connect(database="postgres", **self.__params)
        conn.autocommit = True
        cur = conn.cursor()

        try:
            cur.execute(f"CREATE DATABASE {db_name}")
        except psycopg2.errors.DuplicateDatabase:
            print("База данных с таким именем уже существует.")

        cur.close()
        conn.close()

    @staticmethod
    def drop_database(db_name: str, db_params_path: str = "../database.ini") -> None:
        """Метод для удаления базы данных."""
        params = config(filename=db_params_path)
        conn = psycopg2.connect(database="postgres", **params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE IF EXISTS {db_name}")

        cur.close()
        conn.close()

    def create_tables(self) -> None:
        """Метод для создания таблиц."""
        with self.__conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS employers (
                    employer_id INT PRIMARY KEY,
                    employer_name VARCHAR(30) NOT NULL
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS vacancies (
                    vacancy_id INT PRIMARY KEY,
                    vacancy_name VARCHAR(30) NOT NULL,
                    department VARCHAR(30) NOT NULL,
                    employer_name VARCHAR(30) NOT NULL,
                    employer_id INT NOT NULL REFERENCES employers(employer_id),
                    area VARCHAR(30) NOT NULL,
                    salary VARCHAR(30),
                    published_at DATE NOT NULL,
                    requirement TEXT,
                    responsibility TEXT,
                    schedule VARCHAR(30) NOT NULL,
                    working_hours VARCHAR(30) NOT NULL,
                    work_schedule_by_days VARCHAR(30) NOT NULL,
                    professional_roles VARCHAR(30) NOT NULL,
                    experience VARCHAR(30) NOT NULL,
                    employment VARCHAR(30) NOT NULL,
                    url VARCHAR(50) NOT NULL
                )
            """)

        self.__conn.commit()
