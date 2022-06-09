from Items.Item import Item


class Knife(Item):
    def __init__(self):
        super().__init__()
        self.name = "Нож"
        self.description = "наносит 25 урона"
        self.price = 50  # цена
        self.is_used = True  # можно ли использовать этот предмет
        self.damage = 15
