from items.item import Item


class WhiteShirt(Item):
    def __init__(self):
        super().__init__()
        self.name = "Белая майка"
        self.description = "Легендарная дефолтная майка Си Джея"
        self.price = 10
