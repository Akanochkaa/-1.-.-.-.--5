from data_utils import make_data
from reports import report1, report2, report3

# Главная программа
def main():
    print("=" * 50)
    print("КАДРОВОЕ АГЕНТСТВО")
    print("=" * 50)

    # Загружаем тестовые данные
    all_vacancies = make_data()
    print(f"Загружено вакансий: {len(all_vacancies)}")

    while True:
        # Вывод меню
        print("\n" + "-" * 50)
        print("МЕНЮ:")
        print("1. Все вакансии (сорт: образование, должность)")
        print("2. Испытательный срок от 2 мес")
        print("3. Поиск по окладу")
        print("4. Выход")
        print("-" * 50)

        choice = input("Ваш выбор (1-4): ")

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
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор!")

        if choice in ["1", "2", "3"]:
            input("\nНажмите Enter...")


if __name__ == "__main__":
    main()