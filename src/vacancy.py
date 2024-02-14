class Vacancy:
    """
    Представляет вакансию с соответствующими атрибутами и методами.

    :param title: Название вакансии.
    :param vacancy_url: URL-ссылка на вакансию.
    :param salary_from: Минимальная зарплата, предлагаемая для данной вакансии.
    :param salary_to: Максимальная зарплата, предлагаемая для данной вакансии.
    :param employer: Имя работодателя.
    :param city: Город, в котором находится вакансия.
    :param requirements: Требования к вакансии.
    """

    def __init__(self, title, vacancy_url, salary_from, salary_to, employer, city, requirements) -> None:
        """
        Инициализирует объект Vacancy.


        :param title: Название вакансии.
        :param vacancy_url: URL-ссылка на вакансию.
        :param salary_from: Минимальная зарплата, предлагаемая для данной вакансии.
        :param salary_to: Максимальная зарплата, предлагаемая для данной вакансии.
        :param employer: Имя работодателя.
        :param city: Город, в котором находится вакансия.
        :param requirements: Требования к вакансии.

        :raises ValueError: Если любой из предоставленных атрибутов имеет недопустимый тип.
        """
        if not isinstance(title, str):
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(vacancy_url, str):
            raise ValueError("URL-адрес вакансии должен быть непустой строкой")
        if not (isinstance(salary_from, (int, float, type(None))) and isinstance(salary_to, (int, float, type(None)))):
            raise ValueError("Значения зарплаты должны быть числовыми или None")
        if not isinstance(employer, str):
            raise ValueError("Работодатель должен быть непустой строкой")
        if not isinstance(city, str):
            raise ValueError("Город должен быть непустой строкой")


        self.title = title
        self.vacancy_url = vacancy_url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employer = employer
        self.city = city


        if isinstance(requirements, str):
            self.requirements = requirements
        else:
            self.requirements = "Требования не указаны"
        if salary_from is None or salary_to is None:
            self.salary_comparison = 0
        else:
            self.salary_comparison = (salary_from + salary_to) / 2

    def __getitem__(self, key):
        """
        Получает доступ к атрибутам объекта Vacancy с помощью оператора [].

        :param key: Ключ атрибута для доступа.
        :returns: Значение указанного атрибута.
        :raises KeyError: Если указанный ключ не является действительным атрибутом вакансии.
        """
        if key == 'title':
            return self.title
        elif key == 'vacancy_url':
            return self.vacancy_url
        elif key == 'salary_from':
            return self.salary_from
        elif key == 'salary_to':
            return self.salary_to
        elif key == 'employer':
            return self.employer
        elif key == 'city':
            return self.city
        elif key == 'requirements':
            return self.requirements
        else:
            raise KeyError(f"'{key}' не является действительным ключом для Vacancy")

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Vacancy.
        """
        return (f"title: {self.title}\nvacancy URL: {self.vacancy_url}\n"
                f"salary from: {self.salary_from}\nsalary to: {self.salary_to}\n"
                f"employer: {self.employer}\ncity: {self.city}\nrequirements: {self.requirements}\n")

    def __lt__(self, other) -> bool:
        """
        Сравнивает два объекта Vacancy на основе их средней зарплаты.

        :param other: Другой объект Vacancy для сравнения.
        :returns: bool: True, если эта вакансия имеет более низкую среднюю зарплату, чем другая, False в противном
        случае.
        """
        return self.salary_comparison < other.salary_comparison

    def __le__(self, other) -> bool:
        """
        Сравнивает два объекта Vacancy на основе их средней зарплаты.

        :param other (Vacancy): Другой объект Vacancy для сравнения.
        :return: bool: True, если эта вакансия имеет меньшую или равную среднюю зарплату, чем другая, False в противном
        случае.
        """
        return self.salary_comparison <= other.salary_comparison

    def __gt__(self, other) -> bool:
        """
        Сравнивает два объекта "Вакансия" на основе их средней зарплаты.

        :param other (Vacancy): Другой объект Vacancy для сравнения.
        :return: bool: True, если средняя зарплата этой вакансии выше, чем у другой, False - в противном случае.
        """
        return self.salary_comparison > other.salary_comparison

    def __ge__(self, other) -> bool:
        """
        Сравнивает два объекта "Вакансия" на основе их средней зарплаты.

        :param other (Vacancy): Другой объект Vacancy для сравнения.
        :return: bool: True, если эта вакансия имеет более высокую или равную среднюю зарплату, чем другая, False -
        в противном случае.
        """
        return self.salary_comparison >= other.salary_comparison

    def __eq__(self, other) -> bool:
        """
         Сравнивает два объекта "Вакансия" на основе их средней зарплаты.

        :param other (Vacancy): Другой объект Vacancy для сравнения.
        :return: bool: True, если эта вакансия имеет ту же среднюю зарплату, что и другая, False - в противном случае.
        """
        return self.salary_comparison == other.salary_comparison

    def to_dict(self) -> dict:
        """
        Преобразует объект Vacancy в словарь.

        :return: dict: Словарь, содержащий атрибуты вакансии.
        """
        vacancy_data = {
            'title': self.title,
            'vacancy_url': self.vacancy_url,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'employer': self.employer,
            'city': self.city,
            'requirements': self.requirements
        }

        return vacancy_data
