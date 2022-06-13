from items.item import Item


class RingOfOmnipotence(Item):
    def __init__(self):
        super().__init__()
        self.name = "Кольцо всевластия"
        self.description = "Дешевая подделка"
        self.price = 3
