from items.item import Item


class Excalibur(Item):
    def __init__(self):
        super().__init__()
        self.name = "Экскалибур"
        self.description = "Меч что засунули в камень но в оригинале выбросили в озеро"
        self.price = 850
        self.is_used = True
        self.damage = 35
