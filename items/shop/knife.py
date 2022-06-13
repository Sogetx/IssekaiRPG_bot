from items.item import Item


class Knife(Item):
    def __init__(self):
        super().__init__()
        self.name = "🔪"
        self.description = "Обычный кухонный нож"
        self.price = 300
        self.is_used = True
        self.damage = 13
