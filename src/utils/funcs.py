import os

from src.head_hunter_api import HeadHunterAPI
from src.save_file import JSONSaver


def search_vacancy():
    """Функция поиска вакансий"""

    hh_api = HeadHunterAPI()

    name = input("Введите название: ")
    salary = int(input("Введите нижний порог зарплаты (в рублях): "))
    quantity = int(input("Введите количество вакансий для поиска (максимум 50): "))

    vacancies = hh_api.get_vacancies(name, salary, quantity)
    hh_vacancies = hh_api.parse(vacancies)
    if len(hh_vacancies) > 0:
        print('Поиск работы успешно завершен')
    else:
        print('Поиск работы не удался, попробуйте изменить параметры запроса')
    return hh_vacancies


def save_vacancies(vacancies):
    """Функция сохранения вакансий в файл"""

    json_save = JSONSaver(vacancies, f'data/saved_vacancies/json_vacancies.json')
    json_save.save_to_file()

    print(f'Файл был успешно сохранен по пути: data/saved_vacancies/')


def remove_vacancies(vacancies):
    """Функция удаления вакансии из файла"""

    json_save = JSONSaver(vacancies, f'data/saved_vacancies/json_vacancies.json')

    remove_vac = input('Введите точное название вакансии, которую нужно удалить: ')

    if os.path.isfile("data/saved_vacancies/json_vacancies.json"):
        json_save.delete_vacancy(remove_vac)
        print('Вакансия была успешно удалена из файла')
    else:
        print('Файл с вакансиями не был найден')
