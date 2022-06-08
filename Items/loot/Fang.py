from Items.Item import Item


class Fang(Item):
    def __init__(self):
        super().__init__()
        self.name = "Клык"
        self.description = "надо описание"
        self.count = 1  # количество
        self.price = 7  # цена
