# Создайте собственный класс-исключение, обрабатывающий ситуацию
# деления на нуль. Проверьте его работу на данных, вводимых
# пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться
# с ошибкой.


class OneZeroDivisionError(Exception):
    sms = "На ноль делить нельзя!"

    def __str__(self):
        return self.sms


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise OneZeroDivisionError

        return Number(float(self) / float(other))


if __name__ == '__main__':
    while True:
        try:
            num_1, num_2 = map(Number, input(
                "Введите делимое / делитель: ").split('/'))
            print(num_1 / num_2)
        except OneZeroDivisionError as result:
            print(result)
        except ValueError as result:
            print(result)
            break