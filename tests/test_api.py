from src.api import HeadHunterAPIHandler


def test_headhunter_api_initialization():
    api_handler = HeadHunterAPIHandler()
    api_handler_repr = "URL: https://api.hh.ru/, headers: HeadHunter's Hunter/1.0 (ageenko.timur.10@gmail.com)"
    assert str(api_handler) == api_handler_repr
