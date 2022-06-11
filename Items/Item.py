class Item:
    def __init__(self):
        self.name = "item"
        self.description = "описание"
        self.price = 0  # цена
        self.is_used = False  # можно ли использовать этот предмет
        self.damage = 0  # сколько наносит урона(если это оружие)

    def buy(self, user):  # покупка предмета
        if user.money >= self.price:  # если у пользователя хватает денег, то предмет можно купить
            user.minusmoney(self.price)
            user.add_item(self)
            return "Ты успешно купил: " + self.name + "\n\nпо цене " + str(self.price) + " 💵"  # квитанция об оплате
        else:
            return "Прости, Линк. Я не могу предоставить тебе кредит. Возвращайся, когда ты станешь… мммммм… побогаче!"

    def sell(self, user):
        self.use(user)
        user.money += self.price
        return "Ты продал {0} и получил {1} 💵".format(self.name, self.price)

    def use(self, user):
        user.items[self.name][1] -= 1
        if user.items[self.name][1] == 0:
            user.items.pop(self.name)

    def __repr__(self):  # для магазина
        return "{0}\nЦена: {1} 💵 :\n{2}\n\n".format(self.name, self.price, self.description)
