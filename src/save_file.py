import json
import os
from typing import Union
from src.vacancy import Vacancy


class JSONSaver:
    """
    Реализация класса General Storage для сохранения и загрузки данных,
    а также выполнения различных операций над вакансиями в формате JSON
    """

    def __init__(self, parse_data, file_path: str) -> None:
        """
        Инициализирует экземпляр JSONSaver.

        Args:
            parse_data: Данные, которые необходимо сохранить или загрузить.
            file_path: Путь к файлу JSON.
        """
        self.parse_data = parse_data
        self.path = file_path

    def save_to_file(self):
        """
        Сохраняет данные parse_data в файл JSON.
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.parse_data, file, indent=4, ensure_ascii=False, default=lambda x: x.to_dict())


    def load_from_file(self) -> list[Vacancy]:
        """
        Загружает данные из файла JSON.

        :returns: Загруженные данные из файла.
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def get_vacancies_by_salary(self, sal_criteria: int) -> Union[list[Vacancy], str]:
        """
        Получает вакансии на основе критериев заработной платы.

        :param sal_criteria: Критерии зарплаты для фильтрации вакансий.
        :return: list: Список подходящих вакансий или пустой список, если совпадений не найдено.
        """
        data_get_vac = self.load_from_file()
        matching_vacancies = []
        for vacancy in data_get_vac:
            if vacancy['salary_from'] is not None and vacancy['salary_from'] >= sal_criteria:
                matching_vacancies.append(vacancy)
        if not matching_vacancies:
            return []
        return matching_vacancies

    def get_vacancies_by_city(self, city_criteria: str) -> Union[list[Vacancy], str]:
        """
        Получает вакансии по критериям города.

        :param city_criteria: Критерии города для фильтрации вакансий.
        :returns: list: Список подходящих вакансий или пустой список, если совпадений не найдено.
        """
        data_city = self.load_from_file()
        matching_vacancies = []
        for vacancy in data_city:
            if city_criteria.title() in vacancy['city']:
                matching_vacancies.append(vacancy)
        if not matching_vacancies:
            return []
        return matching_vacancies

    def delete_vacancy(self, remove_criteria: str):
        """
        Удаляет вакансию из хранилища на основе критериев и сохраняет обновленные данные в файл.

        :param remove_criteria: Критерии для идентификации удаляемой вакансии.
        """
        data_del = self.load_from_file()
        self.parse_data = [vacancy for vacancy in data_del if vacancy['title'] != remove_criteria]
        self.save_to_file()

    def top_vacancies(self, top_number: int) -> list[Vacancy]:
        """
        Получает N лучших вакансий из хранилища.

        :param top_number: Количество N лучших вакансий, которые необходимо получить.
        :returns: Список N лучших вакансий.
        """
        data = self.load_from_file()
        new_data = data[:top_number]

        return new_data
