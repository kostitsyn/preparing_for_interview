"""Генератор случайных чисел."""

from datetime import datetime
from hashlib import sha1
import re


def get_random_number(start_num, end_num):
    res_list = list()
    res_dict = dict()
    for i in range(start_num, end_num+1):
        random_num = str(datetime.now()).split('.')[-1]
        random_num = sha1(random_num.encode('utf-8')).hexdigest()
        # random_num = re.sub('\D', '', random_num)
        random_num = ''.join(re.findall('\d', random_num))
        a = random_num[0]
        b = random_num[:int(a)]
        res_list.append(b)
        res_dict[f'elem_{i}'] = b
    print(*res_list)
    # print(**res_dict)

    # res_list = [int(str(datetime.now()).split('.')[-1]) for i in range(start_num, end_num+1)]
    # print(res_list)
    # res_dict = {i: str(datetime.now()).split('.')[-1] for i in range(start_num, end_num+1)}
    # print(res_dict)

print('Генератор случайных чисел.')
while True:
    num_1, num_2 = tuple(input('Введите через пробел начальное и '
                               'конечное число,\nнуль вводить нельзя: ').split())
    try:
        num_1, num_2 = int(num_1), int(num_2)
    except ValueError:
        print('Вы ввели не число.\n')
    else:
        if not num_1 or not num_2:
            print('Нули вводить не допускается.\n')
        elif num_1 == num_2:
            print('Вы ввели два одинаковых числа.\n')
        else:
            if num_1 < num_2:
                get_random_number(num_1, num_2)
            else:
                get_random_number(num_2, num_1)
