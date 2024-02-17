from src.utils.funcs import *


def user_interaction():
    """Функция взаимодействия пользователя с консолью"""

    vacancies = []

    json_saver = JSONSaver(vacancies, 'data/saved_vacancies/json_vacancies.json')

    while True:
        print("Выберите действие:")
        print("1 - Поиск вакансии")
        print("2 - Сохранить вакансию в файл")
        print("3 - Удалить вакансию из файла")
        print("4 - Выбрать вакансию из файла, на основе зарплаты")
        print("5 - Выбрать вакансию из файла, на основе местоположения")
        print("6 - Получить топ вакансий из файла")
        print("7 - Получить все вакансии из файла")
        print("0 - Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            vacancies = search_vacancy()

        elif choice == "2":
            if vacancies:
                save_vacancies(vacancies)
            else:
                print("Сначала вы должны выполнить поиск вакансий.")

        elif choice == "3":
            if len(json_saver.load_from_file()) > 0:
                remove_vacancies(vacancies)
            else:
                print("Файл с вакансиями пуст.")

        elif choice == "4":
            if len(json_saver.load_from_file()) > 0:
                get_vac_by_salary(vacancies)
            else:
                print("Файл с вакансиями пуст.")

        elif choice == "5":
            if len(json_saver.load_from_file()) > 0:
                get_vac_by_city(vacancies)
            else:
                print("Файл с вакансиями пуст.")

        elif choice == "6":
            if len(json_saver.load_from_file()) > 0:
                get_top_vac(vacancies)
            else:
                print("Файл с вакансиями пуст.")

        elif choice == "7":
            if len(json_saver.load_from_file()) > 0:
                get_all_vacancies(vacancies)
            else:
                print("Файл с вакансиями пуст.")

        elif choice == "0":
            print("Выход...")
            exit()
        else:
            print("Повторите ввод.")
