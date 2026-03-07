import requests, os

from dotenv import load_dotenv
from typing import Any


class HeadHunterAPIHandler:
    """Класс для обработки API-запросов к сайту HeadHunter"""

    def __init__(self):
        load_dotenv()
        self.__url = os.getenv("HEADHUNTER_API_URL")
        self.__headers = {
            "User-Agent": os.getenv("HEADHUNTER_HEADER"),
        }
        self.__employers_id = []

    def __repr__(self):
        return f"URL: {self.__url}, headers: {self.__headers["User-Agent"]}"

    def get_employers_id(self, employers: list[str]) -> int:
        """Метод для получения идентификаторов работодателей по их названиям."""
        pass

    def get_vacancies(self) -> list[dict[str, Any]]:
        """Метод для получения списка с вакансиями по работодателям."""
        pass
