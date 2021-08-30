# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(a, b):
    try:
        a, b = int(a), int(b)
        div_num = a / b
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    return round(div_num, 1)


print(div(input('Ведите первое число - '), input('Введите второе число - ')))
