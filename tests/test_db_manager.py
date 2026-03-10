from src.db_manager import DBManager


def test_db_manager_create_database(capsys):
    db_manager = DBManager("test", "./database.ini")
    db_manager.create_database("test")
    db_manager.conn.close()

    captured = capsys.readouterr()
    assert captured.out == "База данных с таким именем уже существует.\n"

    DBManager.drop_database("test", "./database.ini")


def test_db_manager_save_data_to_db(employers, vacancies):
    db_manager = DBManager("test", "./database.ini")
    db_manager.save_data_to_db(employers, vacancies)

    cur = db_manager.conn.cursor()

    cur.execute("SELECT employer_id, employer_name FROM employers")
    employer = cur.fetchall()
    assert employer == [(1740, "Яндекс")]

    cur.execute("SELECT vacancy_id, vacancy_name, salary_str FROM vacancies")
    vacancy = cur.fetchall()
    assert vacancy == [(130355798, "Специалист по договорной работе", "50000-70000 RUR")]

    cur.close()
    db_manager.conn.close()

    DBManager.drop_database("test", "./database.ini")


def test_db_manager_get_companies_and_vacancies_count(employers, vacancies):
    db_manager = DBManager("test", "./database.ini")
    db_manager.save_data_to_db(employers, vacancies)

    employer, vacancies_count = db_manager.get_companies_and_vacancies_count()

    assert employer == "Яндекс"
    assert vacancies_count == 1

    db_manager.conn.close()

    DBManager.drop_database("test", "./database.ini")


def test_db_manager_get_all_vacancies(employers, vacancies):
    db_manager = DBManager("test", "./database.ini")
    db_manager.save_data_to_db(employers, vacancies)

    vacancies = db_manager.get_all_vacancies()

    assert vacancies == [
        (
            "Яндекс",
            "Специалист по договорной работе",
            "50000-70000 RUR",
            "https://api.hh.ru/vacancies/130355798?host=hh.ru",
        )
    ]

    db_manager.conn.close()

    DBManager.drop_database("test", "./database.ini")


def test_db_manager_get_avg_salary(employers, vacancies):
    db_manager = DBManager("test", "./database.ini")
    db_manager.save_data_to_db(employers, vacancies)

    average_salary = db_manager.get_avg_salary()

    assert average_salary == 60000.0

    db_manager.conn.close()

    DBManager.drop_database("test", "./database.ini")


def test_db_manager_get_vacancies_with_higher_salary(employers, vacancies):
    db_manager = DBManager("test", "./database.ini")
    db_manager.save_data_to_db(employers, vacancies)

    vacancies = db_manager.get_vacancies_with_higher_salary()

    assert vacancies[0][0] == 130355798

    db_manager.conn.close()

    DBManager.drop_database("test", "./database.ini")
