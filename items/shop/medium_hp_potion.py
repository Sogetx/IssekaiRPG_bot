from items.item import Item


class MediumHpPotion(Item):
    def __init__(self):
        super().__init__()
        self.name = "Среднее зелье хп"
        self.description = "Лечит вас от нормальных таких ранений"
        self.price = 90
        self.is_used = True

    def use(self, user):
        user.heal(user.max_hp // 4)
        super().use(user)
        return "Ты использовал {0} и получил: +{1} ❤\n\nТеперь у тебя {2}/{3} ❤".format(self.name, user.max_hp // 4,
                                                                                        user.hp, user.max_hp)
