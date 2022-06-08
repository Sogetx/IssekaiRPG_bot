from Items.Item import Item


class Horn(Item):
    def __init__(self):
        super().__init__()
        self.name = "Рог"
        self.description = ""
        self.count = 1  # количество
        self.price = 9  # цена