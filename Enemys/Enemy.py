import random


class Enemy:
    def __init__(self):
        self.max_hp = 0  # полное хп
        self.hp = self.max_hp  # хп
        self.damage1 = 0  # минимальная атака
        self.damage2 = 0  # максимальная атака
        self.money = 0  # деньги с моба
        self.xp = 0  # опыт с моба
        self.name = "имя"
        self.description = "описание"
        self.death = "описание смерти"
        self.sticker = "айди стикера"
        self.run_att = 0  # количество попыток побега
        self.loot = []  # лут

    def enemy_loot(self, user):  # получение награды за убийство моба
        user.money += self.money  # получение денег
        msg = self.death + "\n\nЗа победу над врагом ты получил {0}⭐ и {1}💵\nА также залутал: ".format(self.xp, self.money)
        user.enemy_count += 1  # +1 к счетчику убитых мобов
        if len(self.loot) == 0:  # если у моба нету лута
            return msg + "ничего"
        else:
            items = []
            for item in self.loot:
                items.append(item.name)
                user.add_item(item)
            return msg + ", ".join(items)

    def to_damage(self):  # Нанесение урона
        return random.randint(self.damage1, self.damage2)

    def take_damage(self, received_damage):  # Получение урона
        self.hp -= received_damage
        return received_damage

    def escape(self):  # побег моба
        if self.hp <= self.max_hp // 10 and self.run_att == 0:  # условие для побега моба
            self.run_att = 1
            if random.randint(1, 30) == 1:
                return True

    def __repr__(self):  # Характеристики моба
        return "{0}❤, урон: {1} - {2}💥".format(self.hp, self.damage1, self.damage2)
