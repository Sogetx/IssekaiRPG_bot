from items.item import Item


class Candy(Item):
    def __init__(self):
        super().__init__()
        self.name = "🍬"
        self.description = "Гордон в шоколаде"
        self.price = 20
        self.is_used = True

    def use(self, user):
        user.heal(15)
        super().use(user)
        return "Ты использовал {0} и получил: +15 ❤\n\nТеперь у тебя {1}/{2} ❤".format(self.name, user.hp, user.max_hp)