# Продолжить работу над первым заданием. Разработать методы, отвечающие
# за приём оргтехники на склад и передачу в определенное подразделение
# компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую
# структуру, например словарь.



class StorageError(Exception):
    def __init__(self, sms):
        self.sms = sms

    def __str__(self):
        return self.sms


class AddStorageError(StorageError):
    def __init__(self, text):
        self.sms = f"Невозможно добавить товар на склад:\n {sms}"


class TransferStorageError(StorageError):
    def __init__(self, sms):
        self.sms = f"Ошибка прередачи оборудования:\n {sms}"


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeDevice"):
        if not isinstance(item, OfficeDevice):
            raise AddStorageError(f"{item} не оргтехника")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Недопустимый тип '{type(item)}'")

        item: OfficeDevice = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeDevice = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

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
        return f"На складе сейчас {len(self.__storage)} устройств"


class OfficeDevice:
    def __init__(
            self,
            type: str,
            company: str,
            model: str,
    ):
        self.type = type
        self.vendor = company
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeDevice):
    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeDevice):
    def __init__(self, *args):
        super().__init__('Сканер', *args)


class Xerox(OfficeDevice):
    def __init__(self, *args):
        super().__init__('Ксерокс', *args)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer("HP", "LaserJet P1102W"))
    storage.add(Scanner("Epson", "M3336"))
    storage.add(Xerox("Kycera", "ECOSIS"))
    print(storage)

    last_idx = None
    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)
        last_idx = idx

    print("Передаем 1 устройство")
    storage.transfer(last_idx, 'Отдел логистики')

    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)

    print(storage)
    print("Удаляем 1 устройство")
    del storage[last_idx]
    print(storage)
