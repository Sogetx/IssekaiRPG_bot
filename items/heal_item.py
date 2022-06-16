from items.item import Item


class HealItem(Item):
    def __init__(self,stats):
        super().__init__(stats),
        self.heal = stats[4]

    def use(self, user):
        user.heal(self.heal)
        super().use(user)
        return "Ты использовал {0} и получил: +{1} ❤\n\nТеперь у тебя {2}/{3} ❤".format(self.name,self.heal, user.hp, user.max_hp)