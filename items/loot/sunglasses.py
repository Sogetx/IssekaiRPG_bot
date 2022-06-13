from items.item import Item


class Sunglasses(Item):
    def __init__(self):
        super().__init__()
        self.name = "Солнцезащитные очки"
        self.description = "с ними можно с увереностью выйти на улицу"
        self.price = 12
