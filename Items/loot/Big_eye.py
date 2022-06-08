from Items.Item import Item


class Big_eye(Item):
    def __init__(self):
        super().__init__()
        self.name = "Большой глаз"
        self.description = "Он настолько большой что смотрит тебе в душу, если она конечно у тебя есть"
        self.count = 1  # количество
        self.price = 10  # цена
