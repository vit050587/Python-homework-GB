
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def mass(self):
        mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна неободимо - {round(mass)} т')


r = Road(5000, 20)
r.mass()


#------------------------решения GB------------------------------


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self, weight=25, thickness=5):
        return f"{self._length} м * {self._width} м * {weight} кг * {thickness} см =" \
               f" {(self._length * self._width * weight * thickness) / 1000} т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())


#  ------------------------------------------- вариант решения ---------------------------------------------------------


class Road:
    def __init__(self, le, wi):
        self._length = le
        self._width = wi

    def calc(self, weight=25, thickness=5):
        print(f"Масса асфальта - {self._length * self._width * weight * thickness / 1000} тонн")


def main():
    while True:
        try:
            road_1 = Road(int(input("Enter width of road in m: ")), int(input("Enter lenght of road in m: ")))
            road_1.calc()
            break
        except ValueError:
            print("Only integer!")
