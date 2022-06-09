from Items.Item import Item


class Ring_of_omnipotence(Item):
    def __init__(self):
        super().__init__()
        self.name = "Кольцо всевластия"
        self.description = "Дешевая подделка"
        self.price = 3  # цена
