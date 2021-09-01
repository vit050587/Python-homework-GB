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

#-----------------решения GB------------------------------

from functools import reduce


def mul_list(el_1, el_2):
    return el_1 * el_2


uniq_list = [el for el in range(100, 1001, 2)]
print(f"List\n{uniq_list}\nMultiplication of numbers\n{reduce(mul_list, uniq_list)}")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


from functools import reduce

print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))