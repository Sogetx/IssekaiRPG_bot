from Items.Item import Item


class Silver_YTB(Item):
    def __init__(self):
        super().__init__()
        self.name = "Золотая кнопка ютуба"
        self.description = "Дают за 100 тис подпищиков"
        self.price = 50  # цена
