from Items.Item import Item


class Furious_Sword(Item):
    def __init__(self):
        super().__init__()
        self.name = "Яростный меч"
        self.description = "Меч что прям отдаёт животной яростью"
        self.price = 700
        self.is_used = True
        self.damage = 30
