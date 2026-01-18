from data_utils import make_data
from reports import report1, report2, report3
from vacancy import Vacancy


# Главная программа
def main():
    print("=" * 50)
    print("КАДРОВОЕ АГЕНТСТВО")
    print("=" * 50)

    # Загружаем тестовые данные
    all_vacancies = make_data()
    print(f"Загружено вакансий: {len(all_vacancies)}")

    # Список допустимых должностей
    valid_positions = [
        "Бухгалтер", "Дизайнер", "Менеджер", "Консультант",
        "Водитель", "Охранник", "Программист", "Повар",
        "Юрист", "Аналитик", "Геолог", "Учитель"
    ]

    while True:
        # Вывод меню
        print("\n" + "-" * 50)
        print("МЕНЮ:")
        print("1. Все вакансии (сорт: образование, должность)")
        print("2. Испытательный срок от 2 мес")
        print("3. Поиск по окладу")
        print("4. Добавить вакансию")
        print("5. Удалить вакансию")
        print("6. Выход")
        print("-" * 50)

        choice = input("Ваш выбор (1-6): ")

        # Обработка выбора
        if choice == "1":
            # Запуск отчета 1
            report1(all_vacancies)

        elif choice == "2":
            # Запуск отчета 2
            report2(all_vacancies)

        elif choice == "3":
            try:
                print("\nВведите диапазон оклада:")
                min_s = int(input("От: "))
                max_s = int(input("До: "))

                if min_s > max_s:
                    print("Ошибка: минимальный больше максимального!")
                else:
                    report3(all_vacancies, min_s, max_s)
            except ValueError:
                print("Ошибка! Введите числа.")

        elif choice == "4":
            # Добавление вакансии
            try:
                print("\n=== ДОБАВЛЕНИЕ ВАКАНСИИ ===")

                # Ввод должности
                position = ""
                while True:
                    position = input(
                        "Должность (Бухгалтер/Дизайнер/Менеджер/Консультант/Водитель/Охранник/Программист/Повар/Юрист/Аналитик/Геолог/Учитель): ").strip()
                    if position in valid_positions:
                        break
                    else:
                        print("Неверная должность! Выберите из списка:")
                        print(", ".join(valid_positions))

                experience = int(input("Стаж (лет): "))

                # Проверка пола
                gender = ""
                while True:
                    gender_input = input("Пол (Мужской/Женский/Любой): ").strip()
                    if gender_input in ["Мужской", "Женский", "Любой"]:
                        gender = gender_input
                        break
                    else:
                        print("Неверный пол! Введите: Мужской, Женский или Любой")

                # Проверка образования
                education = ""
                while True:
                    edu_input = input("Образование (Среднее/Среднее спец./Высшее): ").strip()
                    if edu_input in ["Среднее", "Среднее спец.", "Высшее"]:
                        education = edu_input
                        break
                    else:
                        print("Неверное образование! Введите: Среднее, Среднее спец. или Высшее")

                # Возраст
                while True:
                    min_age = int(input("Минимальный возраст (18-70): "))
                    max_age = int(input("Максимальный возраст (18-70): "))
                    if 18 <= min_age <= 70 and 18 <= max_age <= 70 and min_age <= max_age:
                        break
                    else:
                        print(
                            "Неверный возраст! Минимальный возраст должен быть от 18 до 70, максимальный - от 18 до 70, и минимальный не должен превышать максимальный.")

                languages = input("Языки (или 'Нет'): ")
                if languages.strip() == "":
                    languages = "Нет"

                # Зарплата
                while True:
                    min_salary = int(input("Оклад (20000-200000 руб): "))
                    if 20000 <= min_salary <= 200000:
                        break
                    else:
                        print("Оклад должен быть от 20000 до 200000 руб!")

                # Соцпакет
                social_input = ""
                while True:
                    social_input = input("Соцпакет (Да/Нет): ").strip().lower()
                    if social_input in ["да", "нет", "д", "н"]:
                        social = social_input in ["да", "д"]
                        break
                    else:
                        print("Введите 'Да' или 'Нет'")

                # Испытательный срок
                while True:
                    probation = int(input("Испытательный срок (1-6 мес): "))
                    if 1 <= probation <= 6:
                        break
                    else:
                        print("Испытательный срок должен быть от 1 до 6 месяцев!")

                # Создаем новую вакансию
                new_vacancy = Vacancy(position, experience, gender, education,
                                      min_age, max_age, languages, min_salary,
                                      social, probation)
                all_vacancies.append(new_vacancy)
                print(f"\n Вакансия '{position}' успешно добавлена!")
                print(f"Всего вакансий: {len(all_vacancies)}")

                # Показываем добавленную вакансию простым способом
                print("\n=== ДОБАВЛЕННАЯ ВАКАНСИЯ ===")
                social_text = "Да" if new_vacancy.social_package else "Нет"
                print(f"Должность: {new_vacancy.position}")
                print(f"Стаж: {new_vacancy.experience} лет")
                print(f"Пол: {new_vacancy.gender}")
                print(f"Образование: {new_vacancy.education}")
                print(f"Возраст: {new_vacancy.min_age}-{new_vacancy.max_age}")
                print(f"Языки: {new_vacancy.languages}")
                print(f"Оклад: {new_vacancy.min_salary}")
                print(f"Соцпакет: {social_text}")
                print(f"Испытательный срок: {new_vacancy.probation_period} мес.")

            except ValueError as e:
                print(f"Ошибка ввода числа: {e}")
            except Exception as e:
                print(f"Ошибка при добавлении: {e}")

        elif choice == "5":
            # Удаление вакансии
            if len(all_vacancies) == 0:
                print("Список вакансий пуст!")
                continue

            # Сначала показываем все вакансии с номерами
            print("\n=== СПИСОК ВАКАНСИЙ ===")
            for i, v in enumerate(all_vacancies, 1):
                social = "Да" if v.social_package else "Нет"
                print(f"{i}. {v.position}, стаж {v.experience} лет, оклад {v.min_salary}, соцпакет: {social}")

            try:
                num = int(input(f"\nВведите номер вакансии для удаления (1-{len(all_vacancies)}): "))
                if 1 <= num <= len(all_vacancies):
                    deleted = all_vacancies.pop(num - 1)
                    print(f" Удалена вакансия: {deleted.position}")
                    print(f"Осталось вакансий: {len(all_vacancies)}")
                else:
                    print(" Неверный номер!")
            except:
                print(" Ошибка ввода! Введите число.")

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print(" Неверный выбор!")

        if choice in ["1", "2", "3", "4", "5"]:
            input("\nНажмите Enter...")


if __name__ == "__main__":
    main()