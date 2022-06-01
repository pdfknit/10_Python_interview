import os
import random

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
                to_write = f'{key}{value}\n'
                f.write(to_write)


def open_created_file(name, path=os.getcwd()):
    if os.path.isfile(os.path.join(path, name)):
        with open(name, 'r') as f:
            for line in f:
                print(line.strip())

    else:
        print('Такого файла нет')


# create_text_file('test.txt')
open_created_file('test4.txt')
