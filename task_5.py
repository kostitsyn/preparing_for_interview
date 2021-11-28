class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        try:
            new_price = float(new_price)
        except ValueError:
            print('Вы указали не число')
        else:
            if new_price >= 0:
                self.__price = new_price
            else:
                print('Вы указали отрцательное число')


class ItemDiscountReport(ItemDiscount):
    parent_obj = None

    def __init__(self, discount):
        super().__init__(self.parent_obj.name,
                         self.parent_obj.price)
        self.discount = discount

    def __str__(self):
        return f'Цена товара со скидкой: ' \
               f'{round((self.parent_obj.price * (1-self.discount/100)), 2)}'

    @classmethod
    def get_parent_data(cls):
        print(f'Товар {cls.parent_obj.name} стоимостью '
              f'{cls.parent_obj.price}')


while True:
    try:
        name, price = input('Введите через пробел название и цену товара: ').split()
        price = float(price)
    except ValueError:
        print('Вы ввели не два параметра.\n')
    else:
        good_obj = ItemDiscount(name, price)
        new_price = input("Введите новую цену: ")
        good_obj.price = new_price
        ItemDiscountReport.parent_obj = good_obj
        ItemDiscountReport.get_parent_data()
        while True:
            try:
                discount = input('Введите скидку: ')
                discount = float(discount)
            except ValueError:
                print('Вы ввели не число\n')
            else:
                if 0 < discount < 100:
                    report_obj = ItemDiscountReport(discount)
                    print(str(report_obj))
                    break
                else:
                    print('Вы ввели неверное значение скидки\n')
        break
