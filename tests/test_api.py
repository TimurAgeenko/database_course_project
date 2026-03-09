import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.api import HeadHunterAPIHandler


def test_headhunter_api_initialization():
    api_handler = HeadHunterAPIHandler()
    api_handler_repr = "URL: https://api.hh.ru/, headers: HeadHunter's Hunter/1.0 (ageenko.timur.10@gmail.com)"
    assert str(api_handler) == api_handler_repr


@patch("requests.get")
def test_headhunter_api_get_employers_id(mock_get):
    api_handler = HeadHunterAPIHandler()

    mock_get.return_value.json.return_value = {
        "items": [
            {"id": 1, "name": "emp1"},
            {"id": 2, "name": "emp2"},
            {"id": 3, "name": "emp3"}
        ]
    }

    employers_info = api_handler.get_employers_id(["Example"])

    assert employers_info == {"Example": {"emp1": 1, "emp2": 2, "emp3": 3}}

    load_dotenv()
    url = os.getenv("HEADHUNTER_API_URL") + "employers"
    headers = {"User-Agent": os.getenv("HEADHUNTER_HEADER")}

    params = {"text": "Example", "only_with_vacancies": True, "sort_by": "by_vacancies_open"}

    mock_get.assert_called_once_with(url, headers=headers, params=params)


@patch("requests.get")
def test_headhunter_api_get_vacancies(mock_get):
    api_handler = HeadHunterAPIHandler()

    vacancies = [
        {"id": 1, "name": "vac1"},
        {"id": 2, "name": "vac2"},
        {"id": 3, "name": "vac3"}
    ]
    mock_get.return_value.json.return_value = {"items": vacancies}

    vacancies_info = api_handler.get_vacancies({"Example": "1"})

    assert vacancies_info == {"Example": {"employer_id": "1", "vacancies": vacancies}}

    load_dotenv()
    url = os.getenv("HEADHUNTER_API_URL") + "vacancies"
    headers = {"User-Agent": os.getenv("HEADHUNTER_HEADER")}

    params = {"employer_id": "1"}

    mock_get.assert_called_once_with(url, headers=headers, params=params)
