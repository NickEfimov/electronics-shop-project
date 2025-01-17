from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, __name, price, amount):
        """Класс данных по товару в магазине: название, цена, количество"""
        self.__name = __name
        self.price = price
        self.amount = amount
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.amount})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        return self.amount + other.amount

    def calculate_total_price(self):
        """Рассчитывает общую стоимость конкретного товара в магазине."""
        return self.price * self.amount

    def apply_discount(self):
        """Применяет установленную скидку для конкретного товара."""
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, filename):
        cls.all = []
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                items = DictReader(file)
                for item in items:
                    name = item['name']
                    price = item['price']
                    quantity = item['quantity']
                    cls(name, price, quantity)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        except InstantiateCSVError:
            raise ('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(string):
        return int(float(string))


class InstantiateCSVError(Exception):

    def read_csv_file(self):
        required_columns = ['name', 'price', 'quantity']
        if not all(column in required_columns for column in required_columns):
            raise InstantiateCSVError('Файл item.csv поврежден')
