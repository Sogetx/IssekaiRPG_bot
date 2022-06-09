from Items.Item import Item


class Scroll_of_defence(Item):
    def __init__(self):
        super().__init__()
        self.name = "Свиток защиты"
        self.description = "Увеличивает максимальную 🛡 на 1"
        self.price = 150  # цена
        self.is_used = True  # можно ли использовать этот предмет

    def use(self, user):
        user.defence += 1
        super().use(user)
        return "Ты использовал {0} и получил: +1 🛡\n\nТеперь у тебя {1} 🛡".format(self.name, user.defence)