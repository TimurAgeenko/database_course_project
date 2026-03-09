import pytest


@pytest.fixture
def employers():
    return {"Яндекс": "1740"}


@pytest.fixture
def vacancies():
    data = {"Яндекс": {
        "employer_id": "1740",
        "vacancies": [{
            'id': '130355798',
            'premium': False,
            'name': 'Специалист по договорной работе',
            'department': {
                'id': 'yandex-1740-poirekl',
                'name': 'Команда Поисковых сервисов и\xa0ИИ'
            },
            'has_test': False,
            'response_letter_required': False,
            'area': {
                'id': '26',
                'name': 'Воронеж',
                'url': 'https://api.hh.ru/areas/26'
            },
            'salary': {
                'from': 50000,
                'to': 70000,
                'currency': 'RUR',
                'gross': True
            },
            'salary_range': {
                'from': 50000,
                'to': 70000,
                'currency': 'RUR',
                'gross': True,
                'mode': {
                    'id': 'MONTH',
                    'name': 'За\xa0месяц'
                },
                'frequency': {
                    'id': 'TWICE_PER_MONTH',
                    'name': 'Два раза в\xa0месяц'
                }
            },
            'type': {
                'id': 'open',
                'name': 'Открытая'
            },
            'address': None,
            'response_url': None,
            'sort_point_distance': None,
            'published_at': '2026-03-04T10:19:36+0300',
            'created_at': '2026-03-04T10:19:36+0300',
            'archived': False,
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=130355798',
            'branding': {
                'type': 'MAKEUP',
                'tariff': None
            },
            'show_logo_in_search': True,
            'show_contacts': False,
            'insider_interview': None,
            'url': 'https://api.hh.ru/vacancies/130355798?host=hh.ru',
            'alternate_url': 'https://hh.ru/vacancy/130355798',
            'relations': [],
            'employer': {
                'id': '1740',
                'name': 'Яндекс',
                'url': 'https://api.hh.ru/employers/1740',
                'alternate_url': 'https://hh.ru/employer/1740',
                'logo_urls': {
                    'original': 'https://img.hhcdn.ru/employer-logo-original/1490876.png',
                    '90': 'https://img.hhcdn.ru/employer-logo/12253867.png',
                    '240': 'https://img.hhcdn.ru/employer-logo/12253868.png'
                },
                'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1740',
                'country_id': 1,
                'accredited_it_employer': False,
                'trusted': True
            },
            'snippet': {
                'requirement': '''Работали с документами. Грамотно пишете и говорите. Ответственны,
                               внимательны и аккуратны. Уверенно владеете ПК. Работали с Excel.''',
                'responsibility': '''Работа с договорами, закрывающими документами, актами, сверками.
                                  Операции с классифайдами.'''
            },
            'contacts': None,
            'schedule': {
                'id': 'remote',
                'name': 'Удаленная работа'
            },
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': [],
            'accept_temporary': False,
            'fly_in_fly_out_duration': [],
            'work_format': [
                {
                    'id': 'REMOTE',
                    'name': 'Удалённо'
                }
            ],
            'working_hours': [
                {
                    'id': 'HOURS_8',
                    'name': '8\xa0часов'
                }
            ],
            'work_schedule_by_days': [
                {
                    'id': 'FIVE_ON_TWO_OFF',
                    'name': '5/2'
                }
            ],
            'accept_labor_contract': True,
            'civil_law_contracts': [],
            'night_shifts': False,
            'professional_roles': [
                {
                    'id': '40',
                    'name': 'Другое'
                }
            ],
            'accept_incomplete_resumes': True,
            'experience': {
                'id': 'between1And3',
                'name': 'От 1 года до 3 лет'
            },
            'employment': {
                'id': 'full',
                'name': 'Полная занятость'
            },
            'employment_form': {
                'id': 'FULL',
                'name': 'Полная'
            },
            'internship': False,
            'adv_response_url': None,
            'is_adv_vacancy': False,
            'adv_context': None

        }]
    }
    }

    return data
