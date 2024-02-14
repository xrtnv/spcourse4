from abc import ABC, abstractmethod


class GeneralAPI(ABC):
    """Абстрактный класс для API"""

    @abstractmethod
    def get_vacancies(self, name: str, salary: int, quantity: int) -> dict:
        """
        Получает вакансии из API.

        :param name: Название вакансии.
        :param salary: Зарплата.
        :param quantity: Количество вакансий.
        :return: Словарь с данными о вакансиях.
        """
        pass

    @abstractmethod
    def parse(self, data: dict) -> list:
        """
        Преобразует необработанные данные в структурированные объекты класса Vacancy.

        :param data: Необработанные данные из API.
        :return: Структурированные объекты класса Vacancy.
        """
        pass