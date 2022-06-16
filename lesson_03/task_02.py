# Написать программу, которая запрашивает у пользователя ввод числа.
# На введенное число она отвечает сообщением, целое оно или дробное.
# Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.
from decimal import Decimal


def what_digit_is(digit):
    try:
        int(digit)
        print('Число целое')
    except:
        try:
            dec_digit = Decimal(digit)
            print('Число дробное')
            unit = round(dec_digit, 0)
            fraction = (dec_digit - unit) * 100
            return unit == fraction

        except:
            print('Вы ввели неверное значение')


digit = input('Введите число')
print(what_digit_is(digit))
