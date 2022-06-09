from Items.Item import Item


class White_shirt(Item):
    def __init__(self):
        super().__init__()
        self.name = "Белая майка"
        self.description = "Легендарная дефолтная майка Си Джея"
        self.price = 10  # цена
