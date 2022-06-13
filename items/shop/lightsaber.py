from items.item import Item


class Lightsaber(Item):
    def __init__(self):
        super().__init__()
        self.name = "Световой меч"
        self.description = "Да прибудет с тобой сила!"
        self.price = 1200
        self.is_used = True
        self.damage = 40
