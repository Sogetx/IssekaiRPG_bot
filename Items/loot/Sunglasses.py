from Items.Item import Item


class Sunglasses(Item):
    def __init__(self):
        super().__init__()
        self.name = "Солнцезащитные очки"
        self.description = "надо описание"
        self.price = 12  # цена