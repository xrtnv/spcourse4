from abc import ABC

import requests

from src.abstract_classes.general_api import GeneralAPI
from src.vacancy import Vacancy


class HeadHunterAPI(GeneralAPI, ABC):
    """
    Реализация класса GeneralAPI для взаимодействия с API вакансий HeadHunter.
    """

    def __init__(self) -> None:
        """
        Инициализирует экземпляр API HeadHunter.
        Инициализирует базовый URL для API HeadHunter.
        """
        self._base_url = 'https://api.hh.ru/'

    def get_vacancies(self, name: str, salary: int = None, quantity: int = None) -> dict:
        """
        Получает вакансии из API HeadHunter.

        :param name: Название вакансии.
        :param salary: Желаемая зарплата для вакансии.
        :param quantity: Количество вакансий для получения.
        :return: Словарь, содержащий данные о вакансиях.
        """

        url = f'{self._base_url}vacancies'
        headers = {
            'User-Agent': 'MyApp/SPCourse4 forsphws@gmail.com'
        }
        params = {
            'text': f'name:{name}',
            'salary': salary,
            'per_page': quantity,
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        elif response.status_code == 400:
            print('bad request')
        elif response.status_code == 403:
            print('access forbidden')
        elif response.status_code == 404:
            print('not found')
        else:
            print('unknown error')

    def parse(self, data: dict) -> list[Vacancy]:
        """
        Парсит необработанные данные о вакансиях из API HeadHunter.

        :param data: Необработанные данные из API.
        :return: Список разобранных и структурированных объектов вакансий.
        """

        vacancies = []

        for el in data['items']:
            salary_data = el['salary']
            salary_from = salary_data.get('from') if salary_data else None
            salary_to = salary_data.get('to') if salary_data else None

            vac = Vacancy(title=el['name'],
                          vacancy_url=el['alternate_url'],
                          salary_from=salary_from,
                          salary_to=salary_to,
                          employer=el['employer']['name'],
                          city=el['area']['name'],
                          requirements=el['snippet']['requirement']
                          )

            vacancies.append(vac)
        return vacancies
