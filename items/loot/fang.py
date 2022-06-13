from items.item import Item


class Fang(Item):
    def __init__(self):
        super().__init__()
        self.name = "Клык"
        self.description = "Не знаю зачем он тебе если честно"
        self.price = 7
