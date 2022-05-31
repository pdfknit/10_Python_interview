# Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
# Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе будет
# отвечать за вывод названия товара, а вторая — его цены. Далее реализовать вызов каждой из функции get_info.


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountName(ItemDiscount):
    def get_info(self):
        print(f'{self.name}')


class ItemDiscountPrice(ItemDiscount):
    def get_info(self):
        print(f'{self.price}')


Item_01 = ItemDiscountName('Name', 10000)
Item_02 = ItemDiscountPrice('Name2', 20000)

Item_01.get_info()
Item_02.get_info()
