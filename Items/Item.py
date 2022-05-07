import main
from constants import *


class Item:
    def __init__(self):
        self.name = ""  # название
        self.description = ""  # описание
        self.count = 0  # количество
        self.price = 0  # цена
        self.is_used = False  # можно ли использовать этот предмет
        self.heal = 0  # сколько хилит(если это хилящий предмет)
        self.addpower = 0  # сколько добавляет силы(если это предмет добавляющий силу)
        self.adddefence = 0  # сколько добавляет защиты(если это предмет добавляющий защиту)
        self.addxp = 0  # сколько добавляет опыта(если это предмет добавляющий опыт)
        # если предмет можно использовать, то показывается соответствующая кнопка
        self.buttons = [lambda x: (x and "Использовать " + self.name or "")(self.is_used),
                        "💵 Продать " + self.name, ""]

    def buy(self, user):  # покупка предмета
        if user.money >= self.price:  # если у пользователя хватает денег, то предмет можно купить
            user.items.append(self)
        return "Ты успешно купил: " + self.name + "\n\nпо цене " + str(self.price)  # квитанция об оплате

    def use(self, user):
        if self.heal != 0:
            user.heal(self.heal)
        elif self.addpower != 0:
            user.addpower(self.addpower)
        elif self.adddefence != 0:
            user.defence += self.adddefence
        elif self.addxp != 0:
            user.add_xp(self.addxp)
            main.new_level(user.id, NEW_LVL)

    def __repr__(self):
        return self.name + " (" + str(self.count) + "ценой " + \
               str(self.count * self.price) + ") :\n" + self.description + "\n"
