from constants import *


class Item:
    def __init__(self):
        self.name = "item"  # название
        self.description = "описание"  # описание
        self.count = 1  # количество
        self.price = 0  # цена
        self.is_used = False  # можно ли использовать этот предмет
        self.heal = 0  # сколько хилит(если это хилящий предмет)
        self.addpower = 0  # сколько добавляет силы(если это предмет добавляющий силу)
        self.adddefence = 0  # сколько добавляет защиты(если это предмет добавляющий защиту)
        self.addxp = 0  # сколько добавляет опыта(если это предмет добавляющий опыт)
        # если предмет можно использовать, то показывается соответствующая кнопка
        self.buttons = ["💵 Продать " + self.name, ""]

    def buy(self, user):  # покупка предмета
        if user.money >= self.price:  # если у пользователя хватает денег, то предмет можно купить
            user.money -= self.price
            if self.name not in user.items.keys():
                user.items[self.name] = self
            else:
                user.items[self.name].count += 1
        return "Ты успешно купил: " + self.name + "\n\nпо цене " + str(self.price)  # квитанция об оплате

    def sell(self, user):
        user.money += self.price
        self.count -= 1
        if user.items[self.name].count == 0:
            user.items.pop(self.name)

    def use(self, user,func):
        if self.heal != 0:
            user.heal(self.heal)
        elif self.addpower != 0:
            user.addpower(self.addpower)
        elif self.adddefence != 0:
            user.defence += self.adddefence
        elif self.addxp != 0:
            user.add_xp(self.addxp)
            func(user.id, NEW_LVL)
        self.count -= 1
        if user.items[self.name].count == 0:
            user.items.pop(self.name)

    def __repr__(self):
        return self.name + " (" + str(self.count) + "ценой " + \
               str(self.count * self.price) + ") :\n" + self.description + "\n\n"
