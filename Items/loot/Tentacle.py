from Items.Item import Item


class Tentacle(Item):
    def __init__(self):
        super().__init__()
        self.name = "Щупальце"
        self.description = "надо описание"
        self.count = 1  # количество
        self.price = 20  # цена
