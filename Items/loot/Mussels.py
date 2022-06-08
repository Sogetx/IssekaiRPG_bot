from Items.Item import Item


class Mussels(Item):
    def __init__(self):
        super().__init__()
        self.name = "Мидии"
        self.description = ""
        self.count = 1  # количество
        self.price = 30  # цена
