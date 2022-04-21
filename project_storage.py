import random
from window import Window


class MyTypeError(Exception):
    pass


class MyQuantityError(Exception):
    pass


class Storage:
    def __init__(self):
        self.storage = {'Printer': [], 'Scanner': [], 'Copier': []}

    # добавляем случайную технику
    def random_accept(self, equipment_type):
        match equipment_type:
            case 'Printer':
                func = self.random_printer()
            case 'Scanner':
                func = self.random_scanner()
            case 'Copier':
                func = self.random_copier()
        self.storage[equipment_type].append(func)

    def __str__(self):
        storage_string = ''
        for key, value in self.storage.items():
            storage_string += f'{key}s:\n'
            count = 0
            for item in value:
                count += 1
                storage_string += f'{count}. {item.model}({item.serial_number})\n'
        return storage_string

    # собираем строку со всем, что есть на складе
    def count(self):
        count_str = 'In storage\n'
        for key, value in self.storage.items():
            count_str += f'{len(value)} {key}s\n'
        return count_str

    # перемещение техники
    def move_to(self, target_obj, *equipment):
        printers, scanners, copiers = equipment
        try:
            self.validate_equipment(printers, scanners, copiers )
        except MyTypeError as err:
            return err
        except MyQuantityError as err:
            return err
        move_text = ' Moved:\n'
        for i in range(int(printers)):
            item = self.storage['Printer'].pop()
            target_obj.storage['Printer'].append(item)
            move_text += str(item)
        for i in range(int(scanners)):
            target_obj.storage['Scanner'].append(self.storage['Scanner'].pop())
        for i in range(int(copiers)):
            target_obj.storage['Copier'].append(self.storage['Copier'].pop())
        return move_text
    
    # проверка вводимых данных
    def validate_equipment(self, printers, scanners, copiers):
        if not printers.isdigit() or not scanners.isdigit()  or not copiers.isdigit():
            raise MyTypeError('количество должно быть числом')
        if int(printers) > len(self.storage['Printer']) or int(scanners) > len(self.storage['Scanner']) or int(copiers)  > len(self.storage['Copier']):
            raise MyQuantityError('такого количества нет на складе')

    # Создание случайного принтера
    @staticmethod
    def random_printer():
        model = random.choice(['HP', 'Canon', 'Epson', 'Brother'])
        serial_number = f'sn{random.randint(100000, 999999)}'
        cost = random.randint(5000, 100000)
        print_speed = random.choice([10, 30, 50, 100])
        color = bool(random.getrandbits(1))
        return Printer(model, serial_number, cost, print_speed, color)

    # Создание случайного сканера
    @staticmethod
    def random_scanner():
        model = random.choice(['Mustek', 'Canon', 'Epson'])
        serial_number = f'sn{random.randint(100000, 999999)}'
        cost = random.randint(5000, 100000)
        scan_quality = random.choice([300, 600, 1200, 1400])
        return Scanner(model, serial_number, cost, scan_quality)

    # Создание случайного ксерокса
    @staticmethod
    def random_copier():
        model = random.choice(['Xerox', 'Canon', 'HP', 'Brother'])
        serial_number = f'sn{random.randint(100000, 999999)}'
        cost = random.randint(5000, 100000)
        copy_speed = random.choice([5, 10, 20])
        color = bool(random.getrandbits(1))
        return Copier(model, serial_number, cost, copy_speed, color)


# дальше классы нужные по заданию, но почти не используемые. не успел))
class OfficeEquipment:
    def __init__(self, model, serial_number, cost):
        self.model = model
        self.serial_number = serial_number
        self.cost = cost


class Printer(OfficeEquipment):
    def __init__(self, model, serial_number, cost, print_speed, color=False):
        super().__init__(model, serial_number, cost)
        self.print_speed = print_speed
        self.color = color

    def __str__(self):
        return f'Принтер фирмы {self.model}, серийный номер {self.serial_number}'


class Scanner(OfficeEquipment):
    def __init__(self, model, serial_number, cost, scan_quality):
        super().__init__(model, serial_number, cost)
        self.scan_quality = scan_quality

    def __str__(self):
        return f'Сканер фирмы {self.model}, серийный номер {self.serial_number}'


class Copier(OfficeEquipment):
    def __init__(self, model, serial_number, cost, copy_speed, color=False):
        super().__init__(model, serial_number, cost)
        self.copy_speed = copy_speed
        self.color = color

    def __str__(self):
        return f'Ксерокс фирмы {self.model}, серийный номер {self.serial_number}'


if __name__ == '__main__':
    main_storage = Storage()
    office_storage = Storage()

    storage_project = Window(main_storage, office_storage)
    storage_project.run()
