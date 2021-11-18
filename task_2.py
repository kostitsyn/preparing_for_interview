"""
Скрипт проверки чисел.
"""
import re


def handle_number(value):
    try:
        value = int(value)
    except ValueError:
        print('Число дробное')
        int_part, decimal_part = re.split('\D', value)
        if int_part == decimal_part:
            return True
        return False
    else:
        print('Число целое')


while True:
    try:
        input_num = input('Введите любое число. Если число дробное, в качестве разделителя используйте запятую: ')
        separator, = re.findall('^\d+(\D)\d+', input_num)
        input_num = input_num.replace(separator, '.')
        float(input_num)
    except ValueError:
        print('Вы ввели не число.\n')
    else:
        print(handle_number(input_num))
        break
