from Items.Item import Item


class Mussels(Item):
    def __init__(self):
        super().__init__()
        self.name = "Мидии"
        self.description = "Добавьте лимон, будет вкусно"
        self.price = 30
        self.is_used = True

    def use(self, user):
        user.heal(20)
        super().use(user)
        return "Ты использовал {0} и получил: +20 ❤\n\nТеперь у тебя {1}/{2} ❤".format(self.name, user.hp,
                                                                                           user.max_hp)
