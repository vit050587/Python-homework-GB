# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

goods = []
features = {'название': '', 'количество': '', 'цена': '', 'единица измерения': ''}
analitics = {'название': [], 'количество': [], 'цена': [], 'единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        pro = input(f'Введите значение свойства "{f}": ')
        f_copy[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        analitics[f].append(f_copy[f])
    goods.append((num, f_copy))
    print(f'\nСтруктура товаров\n{goods}')
    print(f'\n Текущаа аналитика по товарам: \n {"*" * 30}')
    for key, value in analitics.items():
        print(f'{key:>30}: {value}')
    print("*" * 30)
