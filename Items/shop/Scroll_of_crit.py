from Items.Item import Item


class Scroll_of_crit(Item):
    def __init__(self):
        super().__init__()
        self.name = "Свиток крита"
        self.description = "Увеличивает шанс критического урона 🎯 на 1"
        self.price = 200  # цена
        self.is_used = True  # можно ли использовать этот предмет

    def use(self, user):
        user.crit += 1
        super().use(user)
        return "Ты использовал {0} и получил: +1 🎯\n\nТеперь у тебя {1} 🎯".format(self.name, user.crit)
