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

    def to_damage(self): # Нанесение урона
        return random.randint(self.damage1, self.damage2)

    def take_damage(self, received_damage): # Получение урона
        self.hp -= received_damage

    def reward(self): # Награда
        return random.randint(self.money1, self.money2)

    def __repr__(self): # Вывод урона
        return "{0}❤, урон: {1} - {2}💥".format(self.hp, self.damage1, self.damage2)

