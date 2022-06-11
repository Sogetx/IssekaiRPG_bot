from Items.Item import Item


class Lightsaber(Item):
    def __init__(self):
        super().__init__()
        self.name = "Световой меч"
        self.description = "Да прибудет с тобой сила!"
        self.price = 1000  # цена
        self.is_used = True  # можно ли использовать этот предмет
        self.damage = 35
