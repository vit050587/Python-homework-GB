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

# ----------------------------------------Решения GB------------

month = int(input('Введите интересующий Вас месяц от 1 до 12: '))

month_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
              9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
              'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
if month in month_dict:
    print(f'{month}-й месяц года - это {month_dict[month]}')
    print(f'{month}-й месяц года - это {month_list[month - 1]}')
else:
    print('Не правильный номер!')

# ------------------------------------------------------------------

season_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
month_num = int(input('Введите номер месяца (только цифра): '))
if month_num in sum(season_dict.values(), []):
    for i in season_dict.items():
        if month_num in i[1]:
            print(i[0])

# --------------------------------------------------------------------

while True:
    user_month = input('Введите номер месяца от 1 до 12: ')
    if user_month.isdigit() and 0 < int(user_month) <= 12:
        season_1 = ['Зима', 'Весна', 'Лето', 'Осень', 'Зима']
        season_2 = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень', 4: 'Зима'}
        print(f'Список сезонов - {season_1[int(user_month) // 3]}\nСловарь сезонов - {season_2[int(user_month) // 3]}')
        break
    else:
        print('Error!!!')
