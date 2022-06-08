from Items.Item import Item


class Scrap(Item):
    def __init__(self):
        super().__init__()
        self.name = "Лом"
        self.description = "Легендарное оружие ближнего боя Гордона Фримена"
        self.count = 1  # количество
        self.price = 50  # цена
        self.is_used = True  # можно ли использовать этот предмет
        self.damage = 20
