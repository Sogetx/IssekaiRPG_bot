from Items.Item import Item


class Latex_mask(Item):
    def __init__(self):
        super().__init__()
        self.name = "Латексная маска"
        self.description = "Если ее одеть то можно спокойно идти на ограбление, или вступать в клуб любителей гачи-мучи"
        self.price = 15  # цена
