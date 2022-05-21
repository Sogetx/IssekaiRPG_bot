from Items.Item import Item


class Big_hp_potion(Item):
    def __init__(self):
        super().__init__()
        self.name = "Большое зелье хп"
        self.description = "Остался без руки? Не проблема!"
        self.count = 1  # количество
        self.price = 100  # цена
        self.is_used = True  # можно ли использовать этот предмет

    def use(self, user):
        user.heal(user.max_hp // 2)
        return "Ты использовал {0} и получил: +{1} ❤\n\nТеперь у тебя {2}/{3} ❤".format(self.name, user.max_hp // 2,
                                                                                        user.hp, user.max_hp)
