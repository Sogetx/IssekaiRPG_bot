from Items.Item import Item


class Banana(Item):
    def __init__(self):
        super().__init__()
        self.name = "🍌"
        self.description = "я 🍌 я я 🍌 🍌 чищу 🍌"
        self.price = 5  # цена
        self.is_used = True  # можно ли использовать этот предмет

    def use(self, user):
        user.heal(10)
        super().use(user)
        return "Ты использовал {0} и получил: +10 ❤\n\nТеперь у тебя {1}/{2} ❤".format(self.name, user.hp, user.max_hp)
