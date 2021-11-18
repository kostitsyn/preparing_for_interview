"""
Скрипт построения словаря.
"""

import itertools


def build_dict(list_1, list_2):
    if len(list_1) <= len(list_2):
        res_dict = dict(zip(list_1, list_2))
    else:
        res_dict = dict(itertools.zip_longest(list_1, list_2))
    print(res_dict)


# Вариант 1: ключу не хватает значения
list_1 = ['one', 'two', 'three', 'four', 'five']
list_2 = [i for i in range(3)]
build_dict(list_1, list_2)

# Вариант 2: значению не хватило ключа
list_3 = [i for i in range(8)]
build_dict(list_1, list_3)
