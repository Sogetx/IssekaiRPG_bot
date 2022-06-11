from Items.Item import Item


class Knife(Item):
    def __init__(self):
        super().__init__()
        self.name = "🔪"
        self.description = "Обычный кухонный нож"
        self.price = 400  # цена
        self.is_used = True  # можно ли использовать этот предмет
        self.damage = 15
