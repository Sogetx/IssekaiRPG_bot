from items.item import Item


class AdamsApple(Item):
    def __init__(self):
        super().__init__()
        self.name = "Кадык"
        self.description = "Гордон хотел тебе вырвать, но получилось наоборот"
        self.price = 20
