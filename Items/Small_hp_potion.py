from Items.Item import Item


class Small_hp_potion(Item):
    def __init__(self):
        super().__init__()
        self.name = "Малое зелье хп"
        self.description = "лечит вас от легких ранений"
        self.count = 1  # количество
        self.price = 20  # цена
        self.is_used = True  # можно ли использовать этот предмет

    def use(self, user):
        user.heal(user.max_hp // 10)
        self.use_sell(user)
        return "Ты использовал {0} и получил: +{1} ❤\n\nТеперь у тебя {2}/{3} ❤".format(self.name, user.max_hp // 10,
                                                                                        user.hp, user.max_hp)
