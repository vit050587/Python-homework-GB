# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random

spisok = random.sample(range(1, 100), 10)
print(spisok)
print("*" * 50)
result = []
for el in range(len(spisok) - 1):
    if spisok[el] < spisok[el + 1]:
        result.append(spisok[el + 1])

print(result)

#--------------решение GB------------------------------

my_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)

#  ------------------------------------------- вариант решения ---------------------------------------------------------

from random import randint


original_list = [randint(0, 1000) for _ in range(0, randint(2, 20))]
answer_list = [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]

print(original_list)
print(answer_list)