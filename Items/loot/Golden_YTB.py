from Items.Item import Item


class Golden_YTB(Item):
    def __init__(self):
        super().__init__()
        self.name = "Золотая кнопка ютуба"
        self.description = "Дают за 1млн подпищиков"
        self.count = 1  # количество
        self.price = 40  # цена
