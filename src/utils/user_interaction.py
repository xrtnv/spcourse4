from src.utils.funcs import *


def user_interaction():
    """Функция взаимодействия пользователя с консолью"""

    vacancies = []

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

        choice = input("Enter the action number: ")

        if choice == "1":
            vacancies = search_vacancy()

        elif choice == "2":
            if vacancies:
                save_vacancies(vacancies)
            else:
                print("You must first perform a vacancy search (action 1) before saving.")

        elif choice == "3":
            remove_vacancies(vacancies)

        # elif choice == "4":
        #     get_vac_by_salary(vacancies)
        #
        # elif choice == "5":
        #     get_vac_by_city(vacancies)
        #
        # elif choice == "6":
        #     get_top_vac(vacancies)
        #
        # elif choice == "7":
        #     get_all_vacancies(vacancies)

        elif choice == "0":
            print("Выход...")
            exit()
        else:
            print("Wrong choice. Please select an existing option.")