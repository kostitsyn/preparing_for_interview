import os

def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    for i in os.listdir(sPath):
        if os.path.isfile(f'./{sPath}/{i}'):
            file_path = f'./{sPath}'
            file_name = i
            print(f'File path: {file_path}\t File name: {file_name}')
        else:
            print_directory_contents(f'{sPath}/{i}')


print_directory_contents('root_folder')
