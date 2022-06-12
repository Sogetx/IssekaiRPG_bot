from Items.Item import Item


class Iron_Sword(Item):
    def __init__(self):
        super().__init__()
        self.name = "Железный меч"
        self.description = "Обычный железный меч, ничем не примечателен"
        self.price = 400
        self.is_used = True
        self.damage = 16
