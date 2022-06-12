from Items.Item import Item


class Horn(Item):
    def __init__(self):
        super().__init__()
        self.name = "Рог"
        self.description = "ну вы знаете остренький из кости"
        self.price = 9
