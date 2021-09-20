# Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет
# базовым для классов-наследников. Эти классы — конкретные типы
# оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках
# реализовать параметры, уникальные для каждого типа оргтехники.


class Storage:
    pass


class OfficeDevice:
    vat = 0.13
    added_value = 2.0
    retail_rate = 1.3

    def __init__(
            self,
            type: str,
            company: str,
            model: str,
            purchase_price: float,
    ):
        self.type = type
        self.company = company
        self.model = model
        self.purchase_price = purchase_price
        self.print = True if self.type in ("printer", "xerox") else False
        self.scan = True if self.type in ("scanner", "xerox") else False

    @property
    def retail_price(self):
        return self.wholesale_price * self.retail_rate

    @property
    def wholesale_price(self):
        return self.purchase_price * (1 + self.vat) * (1 + self.added_value)

    def __str__(self):
        return f"{self.type} {self.company} {self.model}"


class Printer(OfficeDevice):
    print = True
    scan = False

    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeDevice):
    print = False
    scan = True

    def __init__(self, *args):
        super().__init__('Сканер', *args)


class Xerox(OfficeDevice):
    print = True
    scan = True

    def __init__(self, *args):
        super().__init__('Ксерокс', *args)


if __name__ == '__main__':
    p1 = Printer("HP", "LaserLet P1102W", 4000)
    print(p1)