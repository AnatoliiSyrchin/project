import random
import window


class Storage:
    storage = {}

    def accept(self, equipment_type):
        match equipment_type:
            case 'Printer':
                func = self.random_printer()
            case 'Scaner':
                func = self.random_printer()
            case 'Copier':
                func = self.random_printer()
        if equipment_type not in self.storage:
            self.storage[equipment_type] = []
            self.storage[equipment_type].append(self.random_printer())
        else:
            self.storage[equipment_type].append(self.random_printer())

    def __str__(self):
        storage_string = ''
        for key, value in self.storage.items():
            storage_string += f'{key}:\n'
            for item in value:
                storage_string += f'{item.model}({item.serial_number}), '
            storage_string.strip(', ')
            storage_string += '\n'
        return storage_string

    def count(self):
        count_str = 'На складе\n'
        for key, value in self.storage.items():
            count_str += f'{len(value)} {key}s\n'
        return count_str

    @staticmethod
    def random_printer():
        model = random.choice(['HP', 'Canon', 'Epson', 'Brother'])
        serial_number = f'sn{random.randint(100000, 999999)}'
        cost = random.randint(5000, 100000)
        print_speed = random.choice([10, 30, 50, 100])
        color = bool(random.getrandbits(1))
        return Printer(model, serial_number, cost, print_speed, color)

    @staticmethod
    def random_scaner():
        model = random.choice(['Mustek', 'Canon', 'Epson'])
        serial_number = f'sn{random.randint(100000, 999999)}'
        cost = random.randint(5000, 100000)
        scan_quality = random.choice([300, 600, 1200, 1400])
        return Scaner(model, serial_number, cost, scan_quality)

    @staticmethod
    def random_copier():
        model = random.choice(['Xerox', 'Canon', 'HP', 'Brother'])
        serial_number = f'sn{random.randint(100000, 999999)}'
        cost = random.randint(5000, 100000)
        copy_speed = random.choice([5, 10, 20])
        color = bool(random.getrandbits(1))
        return Copier(model, serial_number, cost, copy_speed, color)


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


class Scaner(OfficeEquipment):
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
    # import random
    # printers = []
    # for i in range(1, 10):
    #     model = random.choice(['HP', 'Canon', 'Epson', 'Brother'])
    #     serial_number = f'sn{random.randint(100000, 999999)}'
    #     cost = random.randint(5000, 100000)
    #     print_speed = random.choice([10, 30, 50, 100])
    #     color = bool(random.getrandbits(1))
    #     printers.append(Printer(model, serial_number, cost, print_speed, color))
    #
    # scanners = []
    # for i in range(1, 10):
    #     model = random.choice(['Mustek', 'Canon', 'Epson'])
    #     serial_number = f'sn{random.randint(100000, 999999)}'
    #     cost = random.randint(5000, 100000)
    #     scan_quality = random.choice([300, 600, 1200, 1400])
    #     scanners.append(Scaner(model, serial_number, cost, scan_quality))
    # scaner_epson = Scaner('Epson', 'sn4352', 5600, 1200)
    #
    # copiers = []
    # for i in range(1, 10):
    #     model = random.choice(['Xerox', 'Canon', 'HP', 'Brother'])
    #     serial_number = f'sn{random.randint(100000, 999999)}'
    #     cost = random.randint(5000, 100000)
    #     copy_speed = random.choice([5, 10, 20])
    #     color = bool(random.getrandbits(1))
    #     copiers.append(Copier(model, serial_number, cost, copy_speed, color))

    main_storage = Storage()
    # main_storage.accept(copiers[5])
    # main_storage.accept(printers[5])
    # main_storage.accept(printers[6])
    print(main_storage)
    print(main_storage.count())

    storage = window.Window(main_storage)
    storage.run()
    # for i in printers:
    #     print(i)
    # for i in scanners:
    #     print(i)
    # for i in copiers:
    #     print(i)
