import os

from src.head_hunter_api import HeadHunterAPI
from src.save_file import JSONSaver

save_path = 'data/saved_vacancies/json_vacancies.json'


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

    if not os.path.isfile(save_path):
        with open(save_path, "w+"):
            print(f'Файл с вакансиями не был найден. Создан новый.')

    json_save = JSONSaver(vacancies, save_path)
    json_save.save_to_file()

    print(f'Файл был успешно сохранен по пути: data/saved_vacancies/')


def remove_vacancies(vacancies):
    """Функция удаления вакансии из файла"""

    json_save = JSONSaver(vacancies, save_path)

    remove_vac = input('Введите точное название вакансии, которую нужно удалить: ')

    if os.path.isfile("data/saved_vacancies/json_vacancies.json"):
        json_save.delete_vacancy(remove_vac)
        print('Вакансия была успешно удалена из файла')
    else:
        print('Файл с вакансиями не был найден')


def get_vac_by_salary(vacancies):
    """Функция для получения вакансий на основе зарплаты"""

    json_save = JSONSaver(vacancies, save_path)

    vac_by_sal = int(input('Введите зарплату, чтобы получить вакансии: '))

    if os.path.isfile(save_path):
        vac_sal = json_save.get_vacancies_by_salary(vac_by_sal)
        for vac in vac_sal:
            print(vac)

    else:
        print('Файл с вакансиями не был найден')


def get_vac_by_city(vacancies):
    """Функция для получения вакансий по городу"""

    json_save = JSONSaver(vacancies, save_path)

    vac_by_city = input('Введите название города, чтобы получить информацию о вакансиях: ')

    if os.path.isfile(save_path):
        vac_city = json_save.get_vacancies_by_city(vac_by_city)
        for vac in vac_city:
            print(vac)

    else:
        print('Файл с вакансиями не был найден')


def get_top_vac(vacancies):
    """Функция для получения N лучших вакансий"""

    json_save = JSONSaver(vacancies, save_path)

    top_num = int(input(
        'Внимание, если вы введете число, превышающее количество вакансий в файле, будут показаны все вакансии.\n'
        f'Сейчас в файле {len(json_save.load_from_file())} вакансий:\n'
        'Введите количество вакансий, чтобы отобразить N лучших вакансий:\n'))
    if os.path.isfile(save_path):
        vac_top = json_save.top_vacancies(top_num)
        for vac in vac_top:
            print(vac)

    else:
        print('Файл с вакансиями не был найден')


def get_all_vacancies(vacancies):
    """Функция для получения всех вакансий"""

    json_save = JSONSaver(vacancies, save_path)

    if os.path.isfile(save_path):
        vac_all = json_save.load_from_file()
        for vac in vac_all:
            print(vac)

    else:
        print('Файл с вакансиями не был найден')
