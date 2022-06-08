from Items.Item import Item


class Meat(Item):
    def __init__(self):
        super().__init__()
        self.name = "Мясо"
        self.description = "Гнилое, ни на что не годится, разве что продать"
        self.count = 1  # количество
        self.price = 4  # цена
