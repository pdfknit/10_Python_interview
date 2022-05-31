class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # Инкапсулировать оба параметра (название и цену) товара родительского класса.
    # Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
    # Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
    # Результат выполнения заданий 1 и 2 должен быть идентичным.

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    # Реализовать возможность переустановки значения цены товара в родительском классе.
    # Проверить, распечатать информацию о товаре.

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):

    # Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
    # Выполнить перегрузку методов конструктора дочернего класса
    # (метод __init__, в который должна передаваться переменная — скидка), и перегрузку метода __str__ дочернего класса.
    # В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
    # Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
    # (вторая и третья строка после объявления дочернего класса).

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        discount_price = self.get_price() - (self.get_price() * 0.01 * self.discount)
        return f'{self.get_name()} \nЦена со скидкой: {discount_price}'

    def get_parent_data(self):
        print(f'{self.get_name()} {self.get_price()}')


Item_01 = ItemDiscount('Name', 10000)
Item_02 = ItemDiscountReport('Name', 11000, 10)
Item_02.set_price(2000)
Item_02.set_name('Name2')

Item_02.get_parent_data()
