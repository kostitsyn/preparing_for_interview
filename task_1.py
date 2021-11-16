"""Скрипт выводящий в консоль таблицу умножения размерностью A x B"""

from functools import reduce


def print_multiply_table(a: int, b: int):
    """Вывести в консоль таблицу умножения."""

    [print(*reduce(lambda x, y: f'{x}\t{y}',
                   [row_num * col_num for col_num in range(1, b+1)]))
     for row_num in range(1, a+1)]


print('Вывод таблицы умножения.')
while True:
    try:
        num_1, num_2 = tuple(input('Введите через пробел два числа: ').split())
        num_1, num_2 = int(num_1), int(num_2)
    except ValueError:
        print('Вы ввели не число.\n')
    else:
        print_multiply_table(num_1, num_2)
        break
