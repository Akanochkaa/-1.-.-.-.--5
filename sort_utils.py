# Сортировка быстрая (Хоара)
def quick_sort(vac_list, cmp_func):
    # Если список пустой или содержит 1 элемент - он уже отсортирован
    if len(vac_list) <= 1:
        return vac_list

    # Берем средний элемент как опорный
    middle = vac_list[len(vac_list) // 2]

    # Разделяем на три списка:
    left = []  # Элементы меньше опорного
    center = []  # Элементы равные опорному
    right = []  # Элементы больше опорного

    # Распределяем элементы по спискам
    for v in vac_list:
        result = cmp_func(v, middle)  # Сравниваем элемент с опорным
        if result < 0:
            left.append(v)  # Меньше опорного
        elif result == 0:
            center.append(v)  # Равно опорному
        else:
            right.append(v)  # Больше опорного

    # Рекурсивно сортируем левую и правую части, затем объединяем
    return quick_sort(left, cmp_func) + center + quick_sort(right, cmp_func)