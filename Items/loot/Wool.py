from Items.Item import Item


class Wool(Item):
    def __init__(self):
        super().__init__()
        self.name = "Шерсть"
        self.description = "3 шерсти + 3 доски = кровать"
        self.price = 5
