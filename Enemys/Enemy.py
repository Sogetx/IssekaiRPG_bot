import random


class Enemy:
    def __init__(self):
        self.hp = 0
        self.damage1 = 0
        self.damage2 = 0
        self.money1 = 0
        self.money2 = 0
        self.description = "описание моба"
        self.death = "описание смерти моба"

    def to_damage(self):  # Нанесение урона
        return random.randint(self.damage1, self.damage2)

    def take_damage(self, received_damage):  # Получение урона
        self.hp -= received_damage
        return received_damage

    def reward_money(self):  # Награда деньги
        return random.randint(self.money1, self.money2)

    # def reward_xp(self):  # Награда опыт
    #     return random.randint(self.xp1, self.xp2)

    def __repr__(self):  # Характеристики моба
        return "{0}❤, урон: {1} - {2}💥".format(self.hp, self.damage1, self.damage2)
