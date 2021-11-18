import re

my_num = '12*25'
spam = re.findall('\d+$', my_num)
print(spam)

input_num = input('Введите число: ')