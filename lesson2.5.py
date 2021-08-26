# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

spisok = [7, 5, 3, 3, 2]
print(f"Рейтинг: {spisok}")
i = int(input("Введите число: "))
while i:
    for el in range(len(spisok)):
        if spisok[el] == i:
            spisok.insert(el + 1, i)
            break
        elif spisok[0] < i:
            spisok.insert(0, i)
        elif spisok[-1] > i:
            spisok.append(i)
        elif spisok[el] > i and spisok[el + 1] < i:
            spisok.insert(el + 1, i)
    print(f"Обновленный рейтинг: {spisok}")
    i = int(input("Введите число: "))