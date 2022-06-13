from items.item import Item


class TurtleShell(Item):
    def __init__(self):
        super().__init__()
        self.name = "Панцырь большой черепахи"
        self.description = "Лучше не описывать процедуру получения этого предмета"
        self.price = 45
