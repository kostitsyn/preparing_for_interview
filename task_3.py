class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    parent_obj = None

    @classmethod
    def get_parent_data(cls):
        print(f'Товар {cls.parent_obj._ItemDiscount__name} стоимостью '
              f'{cls.parent_obj._ItemDiscount__price}')


while True:
    try:
        name, price = input('Введите через пробел название и цену товара: ').split()
    except ValueError:
        print('Вы ввели не два параметра.\n')
    else:
        good_obj = ItemDiscount(name, price)
        ItemDiscountReport.parent_obj = good_obj
        ItemDiscountReport.get_parent_data()
        break
