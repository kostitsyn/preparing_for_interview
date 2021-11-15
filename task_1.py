class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    parent_obj = None

    @classmethod
    def get_parent_data(cls):
        print(f'Товар {cls.parent_obj.name} стоимостью {cls.parent_obj.price}')


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

# Не понял в этом задании зачем создавать объект родительского класса,
# а потом вызывать метод дочернего, будто обратное наследование получается.
# Сделал передачу объекта родительского класса как атрибут дочернего класса, а на сам метод
# навесил декторатор @classmethod.
