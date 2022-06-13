from items.item import Item


class PoliceCap(Item):
    def __init__(self):
        super().__init__()
        self.name = "Фуражка полицая"
        self.description = "Сталин рекомендует 👍🏼"
        self.price = 20
