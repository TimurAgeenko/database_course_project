import json
import os

from src.utils import save_data_to_file


def test_save_data_to_file():
    data = [
        {"employer_name": "employer_name1", "count": "count2"},
        {"employer_name": "employer_name1", "count": "count2"}
    ]

    save_data_to_file("vacancies_count", data, "./data/")

    with open("./data/vacancies_count.json", "r") as f:
        loaded_data = json.load(f)

    assert data == loaded_data

    os.remove("./data/vacancies_count.json")
    os.rmdir("./data")
