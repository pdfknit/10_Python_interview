def multiple_table(length):
    for i in range(1, length + 1):
        for j in range(1, length + 1):
            print(f'{i}x{j}={i * j}')
        print('-----')


length = int(input('Введите длину таблицы'))
multiple_table(length)
