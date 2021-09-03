# 1. Реализовать скрипт,
# в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

name, user_name, hours, staff_hour, prem = argv

print("Имя: ", user_name)
print("Выработка в часах- ", hours)
print("Ставка в час- ", staff_hour)
print("Премия- ", prem)
print("*" * 50)
print("Расчет заработной платы сотрудника: ", (float(hours) * float(staff_hour)) + float(prem))

#---------------------решения GB-----------------------------

from sys import argv


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Salary - {time * rate + bonus}")
    except ValueError:
        print("Enter all 3 numbers. Not string or empty character.")


salary()