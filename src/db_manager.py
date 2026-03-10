import psycopg2

from src.config import config


class DBManager:
    """Класс для взаимодействия с базой данных"""

    def __init__(self, db_name: str, path: str = "../database.ini"):
        self.__params = config(filename=path)
        self.create_database(db_name)
        self.conn = psycopg2.connect(database=db_name, **self.__params)
        self.create_tables()

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
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS employers (
                    employer_id INT PRIMARY KEY,
                    employer_name VARCHAR(30) NOT NULL
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS vacancies (
                    vacancy_id INT PRIMARY KEY,
                    vacancy_name VARCHAR(50) NOT NULL,
                    department VARCHAR(50) NOT NULL,
                    employer_name VARCHAR(50) NOT NULL,
                    employer_id INT NOT NULL REFERENCES employers(employer_id),
                    area VARCHAR(50) NOT NULL,
                    salary VARCHAR(50),
                    published_at DATE NOT NULL,
                    requirement TEXT,
                    responsibility TEXT,
                    schedule VARCHAR(50) NOT NULL,
                    working_hours VARCHAR(50) NOT NULL,
                    work_schedule_by_days VARCHAR(50) NOT NULL,
                    professional_roles VARCHAR(50) NOT NULL,
                    experience VARCHAR(50) NOT NULL,
                    employment VARCHAR(50) NOT NULL,
                    url VARCHAR(100) NOT NULL
                )
            """)

        self.conn.commit()

    def save_data_to_db(self, employers: dict[str, str], vacancies: dict[str, dict]) -> None:
        """Метод для сохранения данных в базу данных."""
        with self.conn.cursor() as cur:
            for key, value in employers.items():
                cur.execute(
                    """
                    INSERT INTO employers (employer_id, employer_name) VALUES (%s, %s)
                    ON CONFLICT (employer_id) DO NOTHING
                    """,
                    (value, key)
                )

            for key, value in vacancies.items():
                for vacancy in value["vacancies"]:
                    if not vacancy["salary"]:
                        salary = None
                    else:
                        salary = vacancy["salary"]
                        salary = str(salary["from"]) + "-" + str(salary["to"]) + " " + salary["currency"]
                    snippet = vacancy["snippet"]

                    cur.execute(
                        """
                        INSERT INTO vacancies (
                        vacancy_id, vacancy_name, department, employer_name, employer_id, area, salary, published_at,
                        requirement, responsibility, schedule, working_hours, work_schedule_by_days,
                        professional_roles, experience, employment, url
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (vacancy_id) DO NOTHING
                        """,
                        (
                            vacancy["id"],
                            vacancy["name"],
                            vacancy["department"]["name"],
                            key,
                            value["employer_id"],
                            vacancy["area"]["name"],
                            salary,
                            vacancy["published_at"],
                            snippet["requirement"],
                            snippet["responsibility"],
                            vacancy["schedule"]["name"],
                            vacancy["working_hours"][0]["name"],
                            vacancy["work_schedule_by_days"][0]["name"],
                            vacancy["professional_roles"][0]["name"],
                            vacancy["experience"]["name"],
                            vacancy["employment"]["name"],
                            vacancy["url"]
                        )
                    )

        self.conn.commit()

    def get_companies_and_vacancies_count(self) -> tuple[str, int]:
        """Метод для получения списка всех компаний и количества вакансий у каждой компании."""
        cur = self.conn.cursor()

        cur.execute("SELECT employer_name, COUNT(*) as count FROM vacancies GROUP BY employer_name")
        employer, vacancies_count = cur.fetchone()

        return employer, vacancies_count
