from src.db_manager import DBManager


def test_db_manager_create_database(capsys):
    db_manager = DBManager("test", "./database.ini")
    db_manager.create_database("test")
    db_manager.close_conn()

    captured = capsys.readouterr()
    assert captured.out == "База данных с таким именем уже существует.\n"

    DBManager.drop_database("test", "./database.ini")
