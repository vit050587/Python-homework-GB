# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    spisok = [a, b, c]
    try:
        spisok.remove(min(spisok))
        return sum(spisok)
    except TypeError:
        return 'Ведите только цифры!'


print(f'Сумма двух наибольших чисел равна: {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')
