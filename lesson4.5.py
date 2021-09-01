# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

spisok = [el for el in range(100, 1001) if el % 2 == 0]
print(spisok)
print("*" * 50)


def result(el_p, el):
    return el_p * el


print(reduce(result, spisok))
