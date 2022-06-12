from Items.Item import Item


class Big_hp_potion(Item):
    def __init__(self):
        super().__init__()
        self.name = "Большое зелье хп"
        self.description = "Остался без руки? Не проблема!"
        self.price = 150
        self.is_used = True

    def use(self, user):
        user.heal(user.max_hp // 2)
        super().use(user)
        return "Ты использовал {0} и получил: +{1} ❤\n\nТеперь у тебя {2}/{3} ❤".format(self.name, user.max_hp // 2,
                                                                                        user.hp, user.max_hp)
