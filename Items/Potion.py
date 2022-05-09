from Items.Item import Item


class Potion(Item):
    def __init__(self):
        super().__init__()
        self.name = "Зелье хп"
        self.description = "лечит вас от легких ранений"
        self.count = 1  # количество
        self.price = 20  # цена
        self.is_used = True  # можно ли использовать этот предмет
        self.heal = 10  # сколько хилит(если это хилящий предмет)
