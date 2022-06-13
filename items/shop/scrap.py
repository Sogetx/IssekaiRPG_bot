from items.item import Item


class Scrap(Item):
    def __init__(self):
        super().__init__()
        self.name = "Лом"
        self.description = "Легендарное оружие ближнего боя Гордона Фримена"
        self.price = 650
        self.is_used = True
        self.damage = 20
