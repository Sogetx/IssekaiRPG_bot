from Items.Item import Item


class Turtle_shell(Item):
    def __init__(self):
        super().__init__()
        self.name = "Панцырь большой черепахи"
        self.description = "надо описание"
        self.count = 1  # количество
        self.price = 45  # цена
