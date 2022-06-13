from items.item import Item


class BigEye(Item):
    def __init__(self):
        super().__init__()
        self.name = "Большой глаз 👁"
        self.description = "Он настолько большой что смотрит тебе в душу, если она конечно у тебя есть"
        self.price = 10
