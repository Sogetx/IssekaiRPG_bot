import random


class Enemy:
    def __init__(self):
        self.max_hp = 0
        self.hp = self.max_hp  # хп противника
        self.damage1 = 0  # минимальная атака
        self.damage2 = 0  # максимальная атака
        self.money = 0  # деньги с моба
        self.xp = 0  # опыт с моба
        # self.name = "имя моба"
        # self.description = "описание моба"
        self.death = "описание смерти моба"
        self.sticker = "CAACAgIAAxkBAAEEyURiijB_lEfWYrQTkobxFUM7UPEynQACMhEAAuwOiEq0aIFtwmbMqiQE"  # айди стикера моба
        self.run_att = 0  # количество попыток побега
        self.loot = []

    def enemy_loot(self, user):
        user.money += self.money  # получение денег с моба
        msg = self.death + "\n\n" + "За победу над врагом ты получил {0}⭐ и {1}💵\n".format(self.xp, self.money)
        msg += "А также залутал: "
        i = 1
        if len(self.loot) == 0:
            msg += "ничего"
        else:
            for item in self.loot:
                if i < len(self.loot):
                    msg += item.name + ", "
                    i += 1
                else:
                    msg += item.name  # чтоб после последнего залутаного предмета небыло ","
                user.add_item(item)
        user.enemy_count += 1  # счетчик убитых мобов
        return msg

    def to_damage(self):  # Нанесение урона
        return random.randint(self.damage1, self.damage2)

    def take_damage(self, received_damage):  # Получение урона
        self.hp -= received_damage
        return received_damage

    def escape(self):
        if self.hp <= self.max_hp // 10 and self.run_att == 0:  # условие для побега моба
            self.run_att = 1
            if random.randint(1, 30) == 1:
                return True

    def __repr__(self):  # Характеристики моба
        return "{0}❤, урон: {1} - {2}💥".format(self.hp, self.damage1, self.damage2)
