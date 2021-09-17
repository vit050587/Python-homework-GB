# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    square = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.square += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        sgr = Clothes.square
        Clothes.square = 0
        return f'{sgr}'


class Coat(Clothes):
    @property
    def consumption(self):
        return round((self.param / 6.5) + 0.5)


class Costume(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)


coat = Coat(40)
costume = Costume(180)
print('Для пальто нужно:')
print(coat.consumption)
print('Для костюма нужно:')
print(costume.consumption)
print('Общее кол-во ткани:')
print(coat + costume + coat)