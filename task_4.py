import random
import pathlib
import re

KEYWORD = 'example'
REPLACE_KEYWORD = 'sample'


def write_file():
    dir_path = pathlib.Path.cwd()
    file_path = pathlib.Path(dir_path, 'file.txt')
    with open(file_path, 'w') as f:
        list_1 = [str(i) for i in 'abcdefg']
        list_2 = [f'{KEYWORD}{i}' if round(random.random()) else i for i in [j for j in range(1, 8)]]

        res = zip(list_1, list_2)
        for i in res:
            f.write(f'{i[0]}: {i[1]}\n')
    read_file(file_path)


def read_file(file_path):
    with open(file_path) as f:
        for line in f:
            if line.find(KEYWORD) != -1:
                line = line.replace(KEYWORD, REPLACE_KEYWORD)
                if re.search('\w', line) and re.search('\d', line):
                    print(line, end='')

write_file()
