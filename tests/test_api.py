import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.api import HeadHunterAPIHandler


def test_headhunter_api_initialization():
    api_handler = HeadHunterAPIHandler()
    api_handler_repr = (
        "URL: https://api.hh.ru/employers, headers: HeadHunter's Hunter/1.0 (ageenko.timur.10@gmail.com)"
    )
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

    assert employers_info == {"requested_name": "Example", "founded_employers": {"emp1": 1, "emp2": 2, "emp3": 3}}

    load_dotenv()
    url = os.getenv("HEADHUNTER_API_URL")
    headers = {"User-Agent": os.getenv("HEADHUNTER_HEADER")}

    params = {"text": "Example", "only_with_vacancies": True, "sort_by": "by_vacancies_open"}

    mock_get.assert_called_once_with(url, headers=headers, params=params)
