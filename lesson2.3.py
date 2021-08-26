# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

spisok = ['Зима', 'Весна', 'Лето', 'Осень']
quant = int(input("Введите число месяца: "))
if quant == 1 or quant == 12 or quant == 2:
    print(spisok[0])
elif quant == 3 or quant == 4 or quant == 5:
    print(spisok[1])
elif quant == 6 or quant == 7 or quant == 8:
    print(spisok[2])
elif quant == 9 or quant == 10 or quant == 11:
    print(spisok[3])
else:
    print("Такого месяца не существует")

    # -----------------------------------------------

slovar = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
quant = int(input("Введите число месяца: "))
if quant == 1 or quant == 12 or quant == 2:
    print(slovar.get(1))
elif quant == 3 or quant == 4 or quant == 5:
    print(slovar.get(2))
elif quant == 6 or quant == 7 or quant == 8:
    print(slovar.get(3))
elif quant == 9 or quant == 10 or quant == 11:
    print(slovar.get(4))
else:
    print("Такого месяца не существует")

# -----------------------------------------------

quant = int(input('Введите число месяца: '))
if quant == 1 or quant == 2 or quant == 12:
    print('Зима')
elif quant == 3 or quant == 4 or quant == 5:
    print('Весна')
elif quant == 6 or quant == 7 or quant == 8:
    print('Лето')
elif quant == 9 or quant == 10 or quant == 11:
    print('Осень')
else:
    print('Err')
