#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы.
#Реализовать вывод данных о пользователе одной строкой.

def user_ch(**kwargs):
    return ' * '.join(kwargs.values())

print(user_ch(name=input('Ведите Ваше имя - '), surname=input('Введите Вашу фамилию - '),
              birthday=input('Ведите дату вашего рождния - '), town=input('Введите город вашего проживания - '),
              email=input('Введите Вашу почту - '), phone=input('Введите Ваш телефон - ')))