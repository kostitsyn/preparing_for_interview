"""
Скрипт поиска полного пути до файла.
"""

import os


def get_data(file):
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name == file:
                spam = os.path.abspath(os.path.join(root))
                eggs = name.rfind('.')
                file_name = name[:eggs]
                print(f'Путь до файла: {spam}\nИмя файла: {file_name}\n')


get_data('task_1.py')
