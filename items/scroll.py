from items.item import Item


class Scroll(Item):
    def __init__(self, stats):
        super().__init__(stats),

    def use(self, user):
        super().use(user)
        if self.name == "Свиток крита":
            user.crit += 1
            return "Ты использовал {0} и получил: +1 🎯\n\nТеперь у тебя {1} 🎯".format(self.name, user.crit)
        elif self.name == "Свиток защиты":
            user.defence += 1
            return "Ты использовал {0} и получил: +1 🛡\n\nТеперь у тебя {1} 🛡".format(self.name, user.defence)
        elif self.name == "Свиток силы":
            user.power += 1
            return "Ты использовал {0} и получил: +1 💪\n\nТеперь у тебя {1} 💪".format(self.name, user.power)
