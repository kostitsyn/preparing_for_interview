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


class ItemDiscountReport1(ItemDiscount):
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

    def get_info(self):
        print(f'Название товара: {self.parent_obj.name}')


class ItemDiscountReport2(ItemDiscount):
    parent_obj = None

    def __init__(self, discount):
        super().__init__(self.parent_obj.name,
                         self.parent_obj.price)
        self.discount = discount

    def __str__(self):
        return f'Цена товара со скидкой: ' \
               f'{round((self.parent_obj.price * (1 - self.discount / 100)), 2)}'

    @classmethod
    def get_parent_data(cls):
        print(f'Товар {cls.parent_obj.name} стоимостью '
              f'{cls.parent_obj.price}')

    def get_info(self):
        print(f'Цена товара: {self.parent_obj.price}')


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
        ItemDiscountReport1.parent_obj = good_obj
        ItemDiscountReport2.parent_obj = good_obj
        ItemDiscountReport1.get_parent_data()
        while True:
            try:
                discount = input('Введите скидку: ')
                discount = float(discount)
            except ValueError:
                print('Вы ввели не число\n')
            else:
                if 0 < discount < 100:
                    report_obj_1 = ItemDiscountReport1(discount)
                    report_obj_2 = ItemDiscountReport2(discount)
                    print(f'{str(report_obj_1)}\n')

                    print('Полиморфизм:\n')
                    print('1 способ')
                    report_obj_1.get_info()
                    report_obj_2.get_info()
                    print()

                    print('2 способ')
                    for obj in [report_obj_1, report_obj_2]:
                        obj.get_info()
                    print()

                    print('3 способ')
                    def obj_handler(obj):
                        obj.get_info()

                    obj_handler(report_obj_1)
                    obj_handler(report_obj_2)
                    print()
                    break
                else:
                    print('Вы ввели неверное значение скидки\n')
        break
