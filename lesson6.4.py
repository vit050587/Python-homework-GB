# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


from random import choice


class Car:
    direction = ["право", "лево"]

    def __init__(self, speed, color, name, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f'Автомобиль: {name} {color} цвета. Полицейская? - {is_police}!')
        print(60 * '-')

    def go(self):
        print(f'Автомобиль {self.name} едет!')

    def stop(self):
        print(f'Автомобиль {self.name} стоит!')

    def turn(self):
        print(f'Автомобиль {self.name} повернул в {choice(self.direction)}')

    def show_speed(self):
        print(f'со скоростью: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'\nС превышением скорости на {self.speed - 60} км/ч.')
        else:
            print(f'С разрешенной скоростью: {self.speed} км/ч.')


class SportCar(Car):
    def show_speed(self):
        print(f'\nС максимальной скоростью: {self.speed} км/ч.')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'\nС превышением скорости на {self.speed - 40} км/ч.')
        else:
            print(f'С разрешенной скоростью:{self.speed} км/ч.')


class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'\nС превышением скорости на {self.speed - 60} км/ч. - с мигалкой можно!')
        else:
            print(f'С разрешенной скоростью:{self.speed} км/ч.')


town = TownCar(90, 'черного', 'АУДИ', False)
sport = SportCar(270, 'красного', 'БМВ', False)
work = WorkCar(30, 'белого', 'ГРУЗОВИК', False)
police = PoliceCar(100, 'синего', 'Жигули', True)

list_of_cars = [police, work, sport, town]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print(60 * '-')
