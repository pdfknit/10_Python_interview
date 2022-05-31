class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'{self.name} {self.price}')


Item_01 = ItemDiscount('Name', 10000)
Item_02 = ItemDiscountReport('Name', 11000)

Item_02.get_parent_data()
