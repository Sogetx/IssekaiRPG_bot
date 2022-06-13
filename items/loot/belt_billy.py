from items.item import Item


class BeltBilly(Item):
    def __init__(self):
        super().__init__()
        self.name = "Ремень Билли"
        self.description = "Чтобы его получить ты убил Билли. Фаны гачи-мучи тебя никогда не простят"
        self.price = 35
