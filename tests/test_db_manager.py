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
    assert employer == [(1740, 'Яндекс')]

    cur.execute("SELECT vacancy_id, vacancy_name, salary FROM vacancies")
    vacancy = cur.fetchall()
    assert vacancy == [(130355798, 'Специалист по договорной работе', '50000-70000 RUR')]

    cur.close()
    db_manager.conn.close()

    DBManager.drop_database("test", "./database.ini")
