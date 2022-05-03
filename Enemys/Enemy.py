import random


class Enemy:
    def __init__(self):
        self.hp = 0 #хп противника
        self.damage1 = 0 # минимальная атака
        self.damage2 = 0 # максимальная атака
        self.money = 0 # деньги с моба
        self.xp = 0 # опыт с моба
        self.description = "описание моба"
        self.death = "описание смерти моба"

    def to_damage(self):  # Нанесение урона
        return random.randint(self.damage1, self.damage2)

    def take_damage(self, received_damage):  # Получение урона
        self.hp -= received_damage
        return received_damage


    def __repr__(self):  # Характеристики моба
        return "{0}❤, урон: {1} - {2}💥".format(self.hp, self.damage1, self.damage2)
