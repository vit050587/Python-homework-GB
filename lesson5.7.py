# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json


def company_func():
    try:
        with open('file_7.txt', 'r+', encoding='utf-8') as file:
            statistics = []
            profit_dict = {}
            profit_ave = {}
            av = 0
            val = 0
            i = 4
            for line in file:
                firm, form, profit, waste = line.split()
                margin = int(profit) - int(waste)
                if margin >= 0:
                    val = val + margin
                else:
                    i -= 1
                profit_dict[firm] = margin
            statistics.append(profit_dict)
            if i != 0:
                (av) = val / i
                profit_ave['profit_ave'] = round(av)
                statistics.append(profit_ave)
            else:
                print('Все компании работают в убыток!')
            print(statistics)
        with open('file_7.json', 'a+', encoding='utf-8') as json_file:
            json.dump(statistics, json_file)
    except FileNotFoundError:
        return 'Err!!!'


company_func()
