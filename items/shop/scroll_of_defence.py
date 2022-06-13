from items.item import Item


class ScrollOfDefence(Item):
    def __init__(self):
        super().__init__()
        self.name = "Свиток защиты"
        self.description = "Увеличивает максимальную 🛡 на 1"
        self.price = 150
        self.is_used = True

    def use(self, user):
        user.defence += 1
        super().use(user)
        return "Ты использовал {0} и получил: +1 🛡\n\nТеперь у тебя {1} 🛡".format(self.name, user.defence)
