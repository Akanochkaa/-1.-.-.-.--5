# Показываем таблицу
def show_table(vacancies, name):
    # Проверяем, есть ли данные для отображения
    if len(vacancies) == 0:
        print("Нет вакансий")
        return

    # Собираем все данные для расчета ширины столбцов
    headers = ["№", "Должность", "Стаж", "Пол", "Образование", "Возраст", "Языки", "Оклад", "Соцпакет", "Исп.срок"]

    all_data = []
    all_data.append(headers)  # Добавляем заголовки в общий список данных

    # Добавляем данные вакансий в общий список
    num = 1
    for v in vacancies:
        social = "Да" if v.social_package else "Нет"
        row = [
            str(num),  # Номер строки
            v.position,  # Должность
            str(v.experience),  # Стаж (преобразуем в строку)
            v.gender,  # Пол
            v.education,  # Образование
            f"{v.min_age}-{v.max_age}",  # Возрастной диапазон
            v.languages,  # Языки
            str(v.min_salary),  # Оклад (преобразуем в строку)
            social,  # Соцпакет
            f"{v.probation_period} мес."  # Испытательный срок
        ]
        all_data.append(row)
        num += 1

    # Находим максимальную длину для каждого столбца
    col_widths = []
    for i in range(len(headers)):
        max_len = 0
        # Ищем максимальную длину значения в текущем столбце
        for row in all_data:
            cell_len = len(str(row[i]))
            if cell_len > max_len:
                max_len = cell_len
        col_widths.append(max_len + 2)

    # Выводим заголовок отчета
    print("\n" + "=" * 100)
    print(name)
    print("=" * 100)

    # Выводим заголовок таблицы с выравниванием
    header_line = ""
    for i in range(len(headers)):
        header_line += headers[i].ljust(col_widths[i])  # Выравниваем каждый заголовок
    print(header_line)

    # Разделитель под заголовком таблицы
    separator = ""
    for width in col_widths:
        separator += "-" * width
    print(separator)

    # Выводим данные с выравниванием
    num = 1
    for v in vacancies:
        social = "Да" if v.social_package else "Нет"

        # Подготавливаем данные для текущей строки
        row_data = [
            str(num),
            v.position,
            str(v.experience),
            v.gender,
            v.education,
            f"{v.min_age}-{v.max_age}",
            v.languages,
            str(v.min_salary),
            social,
            f"{v.probation_period} мес."
        ]

        # Формируем строку с выравниванием
        row_line = ""
        for i in range(len(row_data)):
            row_line += str(row_data[i]).ljust(col_widths[i])  # Выравниваем каждое значение
        print(row_line)
        num += 1

    # Выводим разделитель и итоговую информацию
    print(separator)
    print(f"Всего: {len(vacancies)} вакансий")


# Сохранить в файл (исправленная версия с выравниванием)
def save_file(vacancies, name, file_name):
    try:
        # Определяем заголовки столбцов
        headers = ["№", "Должность", "Стаж", "Пол", "Образование", "Возраст", "Языки", "Оклад", "Соцпакет", "Исп.срок"]

        # Собираем все данные для расчета ширины столбцов
        all_data = []
        all_data.append(headers)

        # Добавляем данные вакансий
        num = 1
        for v in vacancies:
            social = "Да" if v.social_package else "Нет"
            row = [
                str(num),
                v.position,
                str(v.experience),
                v.gender,
                v.education,
                f"{v.min_age}-{v.max_age}",
                v.languages,
                str(v.min_salary),
                social,
                f"{v.probation_period} мес."
            ]
            all_data.append(row)
            num += 1

        # Находим максимальную длину для каждого столбца
        col_widths = []
        for i in range(len(headers)):
            max_len = 0
            for row in all_data:
                cell_len = len(str(row[i]))
                if cell_len > max_len:
                    max_len = cell_len
            col_widths.append(max_len + 2)  # +2 для отступов

        # Открываем файл для записи
        f = open(file_name, 'w', encoding='utf-8')

        # Записываем название отчета
        f.write(name + "\n")

        # Рассчитываем общую ширину для разделителя
        total_width = sum(col_widths)
        f.write("=" * total_width + "\n\n")

        # Заголовок таблицы с выравниванием
        header_line = ""
        for i in range(len(headers)):
            header_line += headers[i].ljust(col_widths[i])
        f.write(header_line + "\n")

        separator = ""
        for width in col_widths:
            separator += "-" * width
        f.write(separator + "\n")

        # Записываем данные с выравниванием
        num = 1
        for v in vacancies:
            social = "Да" if v.social_package else "Нет"

            row_data = [
                str(num),
                v.position,
                str(v.experience),
                v.gender,
                v.education,
                f"{v.min_age}-{v.max_age}",
                v.languages,
                str(v.min_salary),
                social,
                f"{v.probation_period} мес."
            ]

            # Формируем строку с выравниванием
            row_line = ""
            for i in range(len(row_data)):
                row_line += str(row_data[i]).ljust(col_widths[i])
            f.write(row_line + "\n")
            num += 1

        # Записываем разделитель и итоговую информацию
        f.write(separator + "\n")
        f.write(f"Всего: {len(vacancies)} вакансий\n")
        f.close()

        print(f"Сохранено в {file_name}")
    except Exception as e:
        print(f"Ошибка записи файла: {e}")