# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.


class AppError(Exception):
    def __init__(self, sms):
        self.sms = sms

    def __str__(self):
        return self.sms


class AcceptStorageError(AppError):
    def __init__(self, sms):
        self.sms = f"Невозможно добавить товар на склад:\n {sms}"


class TransferStorageError(AppError):
    def __init__(self, text):
        self.sms = f"Ошибка прередачи оборудования:\n {sms}"


AddStorageError = AcceptStorageError


class ValidateDeviceError(AppError):
    pass


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, devices):
        if not all([isinstance(device, OfficeDevice) for device in devices]):
            raise AddStorageError(f"Устройство не является офисным!")

        self.__storage.extend(devices)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Ошибка типа данных '{type(item)}'")

        item: OfficeDevice = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Устройство {item} закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"На складе: {len(self.__storage)} устройства"


print('-' * 70)


class OfficeDevice:
    __required_props = ("type", "company", "model")

    def __init__(self, eq_type: str = None, company: str = "", model: str = ""):
        self.type = eq_type
        self.company = company
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' должен иметь значение отличное от false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.company} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateDeviceError(f"'{type(cnt)}'; количество инстансов должен быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeDevice):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)


class Scanner(OfficeDevice):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)


class Xerox(OfficeDevice):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Xerox', **kwargs)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer.create(1, company="HP", model="LaserJet P1102W"))
    storage.add(Scanner.create(1, company="Epson", model="M3336"))
    storage.add(Xerox.create(1, company="Kyocera", model="ECOSIS"))
    print(storage)

    for idx, itm in storage.filter_by(department=None, company="Kyocera", model="ECOSIS"):
        print(f"Резервируем {itm} в Отдел логистики")
        storage.transfer(idx, 'Отдел логистики')

    for idx, itm in storage.filter_by(department=None):
        print(idx, f"{itm} не распределены по отделам")

    print('-' * 70)
    print(storage)
    print('-' * 70)
    print("Списываем 1 устройство")
    print('-' * 70)
    del storage[0]
    print(storage)
    print('-' * 70)
