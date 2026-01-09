from sort_utils import quick_sort
from display_utils import show_table, save_file

# Отчет 1: Полный список вакансий, отсортированный по образованию и должности
def report1(vacancies):
    print("\n=== ОТЧЕТ 1 ===")
    print("Сортировка: образование и должность")

    # Функция сравнения для сортировки
    def compare(v1, v2):
        # Сначала сравниваем по образованию (возрастание)
        edu_vals = {"Среднее": 1, "Среднее спец.": 2, "Высшее": 3}  # Веса для сортировки
        e1 = edu_vals.get(v1.education, 0)
        e2 = edu_vals.get(v2.education, 0)

        if e1 != e2:
            return e1 - e2  # Разница весов определяет порядок

        # Если образование одинаковое, сравниваем по должности (возрастание)
        if v1.position < v2.position:
            return -1
        elif v1.position > v2.position:
            return 1
        else:
            return 0

    # Сортируем копию списка вакансий
    sorted_list = quick_sort(vacancies.copy(), compare)

    # Показываем результат в виде таблицы
    show_table(sorted_list, "Отчет 1: Все вакансии по образованию и должности")

    # Сохраняем результат в файл
    save_file(sorted_list, "Отчет 1: Все вакансии по образованию и должности", "otchet1.txt")

    return sorted_list


# Отчет 2: Вакансии с испытательным сроком не менее 2 месяцев
def report2(vacancies):
    print("\n=== ОТЧЕТ 2 ===")
    print("Испытательный срок от 2 месяцев")

    # Отбираем вакансии с испытательным сроком >= 2 месяцев
    filtered = []
    for v in vacancies:
        if v.probation_period >= 2:
            filtered.append(v)

    # Функция сравнения для сортировки
    def compare(v1, v2):
        # Сначала по испытательному сроку
        if v1.probation_period > v2.probation_period:
            return -1
        elif v1.probation_period < v2.probation_period:
            return 1

        # Если сроки равны, сравниваем по стажу (убывание)
        if v1.experience > v2.experience:
            return -1
        elif v1.experience < v2.experience:
            return 1

        # Если стаж равен, сравниваем по максимальному возрасту (возрастание)
        if v1.max_age < v2.max_age:
            return -1
        elif v1.max_age > v2.max_age:
            return 1
        else:
            return 0

    # Сортируем отфильтрованный список
    sorted_list = quick_sort(filtered, compare)

    # Показываем результат
    show_table(sorted_list, "Отчет 2: Испытательный срок от 2 месяцев")
    print("Сортировка: срок, стаж, возраст")

    # Сохраняем в файл
    save_file(sorted_list, "Отчет 2: Испытательный срок от 2 месяцев\nСортировка: срок, стаж, возраст",
              "otchet2.txt")

    return sorted_list


# Отчет 3: Вакансии с окладом в заданном диапазоне
def report3(vacancies, min_sal, max_sal):
    print("\n=== ОТЧЕТ 3 ===")
    print(f"Оклад от {min_sal} до {max_sal} рублей")

    # Отбираем вакансии по диапазону оклада
    filtered = []
    for v in vacancies:
        if min_sal <= v.min_salary <= max_sal:
            filtered.append(v)

    # Функция сравнения для сортировки
    def compare(v1, v2):
        # Сначала по наличию соцпакета (возрастание: сначала без соцпакета)
        if not v1.social_package and v2.social_package:
            return -1  # v1 (без соцпакета) должен быть перед v2 (с соцпакетом)
        elif v1.social_package and not v2.social_package:
            return 1  # v1 (с соцпакетом) должен быть после v2 (без соцпакета)

        # Если соцпакет одинаковый, сравниваем по испытательному сроку (убывание)
        if v1.probation_period > v2.probation_period:
            return -1
        elif v1.probation_period < v2.probation_period:
            return 1
        else:
            return 0

    # Сортируем отфильтрованный список
    sorted_list = quick_sort(filtered, compare)

    # Показываем результат
    show_table(sorted_list, f"Отчет 3: Оклад от {min_sal} до {max_sal} руб.")
    print("Сортировка: соцпакет,срок")

    # Сохраняем в файл (имя файла содержит диапазон окладов)
    save_file(sorted_list, f"Отчет 3: Оклад от {min_sal} до {max_sal} руб.\nСортировка: соцпакет, срок",
              f"otchet3_{min_sal}_{max_sal}.txt")

    return sorted_list