from items.item import Item


class SilverYTB(Item):
    def __init__(self):
        super().__init__()
        self.name = "Серебряная кнопка ютуба"
        self.description = "Дают за 100 тис подпищиков"
        self.price = 50
