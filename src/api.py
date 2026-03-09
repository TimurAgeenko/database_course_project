import os
from typing import Any

import requests
from dotenv import load_dotenv


class HeadHunterAPIHandler:
    """Класс для обработки API-запросов к сайту HeadHunter"""

    def __init__(self):
        load_dotenv()
        self.__url = os.getenv("HEADHUNTER_API_URL")
        self.__headers = {"User-Agent": os.getenv("HEADHUNTER_HEADER")}
        self.__employers_id = []

    def __repr__(self):
        return f"URL: {self.__url}, headers: {self.__headers["User-Agent"]}"

    def get_employers_id(self, employers: list[str]) -> dict[str, Any]:
        """Метод для получения идентификаторов работодателей по их названиям."""
        result = {}

        for employer in employers:
            employers_dict = {}

            url = self.__url + "employers"
            params = {
                "text": employer,
                "only_with_vacancies": True,
                "sort_by": "by_vacancies_open"
            }

            response = requests.get(url, headers=self.__headers, params=params)
            response_json = response.json()

            for item in response_json["items"]:
                employers_dict[item["name"]] = item["id"]

            result[employer] = employers_dict

        return result

    def get_vacancies(self, employers: dict[str, str]) -> dict[str, Any]:
        """Метод для получения списка с вакансиями по работодателям."""
        result = {}

        for key, value in employers.items():
            url = self.__url + "vacancies"
            params = {"employer_id": value}

            response = requests.get(url, headers=self.__headers, params=params)
            response_json = response.json()

            result[key] = {"employer_id": value, "vacancies": response_json["items"]}

        return result
