# Реализовать функцию поиска определенных подстрок в файле по следующим условиям: вывод первого вхождения, вывод всех вхождений.
# Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк.
# (это ДВЕ ОТДЕЛЬНЫЕ функции которые ВЫВОДЯТ значения, не записывают и не модифицируют файлы)


import os
import random
import re

RAND_RANGE = [0, 25]
RAND_LENGTH = 100
LETTERS = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'


def create_text_file(name, path=os.getcwd()):
    if os.path.isfile(os.path.join(path, name)):
        print('Уже есть')
    else:
        list_01 = [random.randint(RAND_RANGE[0], RAND_RANGE[1]) for _ in range(RAND_LENGTH)]
        list_02 = [random.choice(LETTERS) for _ in range(RAND_LENGTH)]
        with open(name, 'w+') as f:
            for key, value in zip(list_01, list_02):
                if random.randint(-10, 50) < 0:
                    to_write = f'{value}{key}\n'
                else:
                    to_write = f'{key}{value}\n'
                f.write(to_write)


def open_created_file(name, path=os.getcwd()):
    if os.path.isfile(os.path.join(path, name)):
        with open(name, 'r') as f:
            for line in f:
                print(line.strip())
    else:
        print('Такого файла нет')


def find_subline(filename, pattern, all_includes=True):
    '''
    Функция поиска определенных подстрок в файле по следующим условиям: вывод первого вхождения, вывод всех вхождений.
    :param filename:
    :param pattern:
    :param all_includes:
    :return:
    '''
    with open(filename, 'r') as f:
        data = f.read()
        if all_includes:
            result = re.findall(pattern, data)
            return result
        else:
            match = re.match(pattern, data)
            return match.group(0)

def reverse_search_lines(line):
    '''
    Заменa всех найденных подстрок на новое значение и вывод измененных строк
    :param line:
    :return:
    '''
    for i, element in enumerate(line):
        line[i] = element[::-1]
    return line

filename = 'test.txt'
create_text_file('test.txt')
print(find_subline(filename, f'[0-9]*', False))
open_created_file(filename)
line = find_subline(filename, f'\w*')
print(line)
print(reverse_search_lines(line))


