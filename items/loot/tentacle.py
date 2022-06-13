from items.item import Item


class Tentacle(Item):
    def __init__(self):
        super().__init__()
        self.name = "Щупальце"
        self.description = "Не не, хентая не будет"
        self.price = 20
