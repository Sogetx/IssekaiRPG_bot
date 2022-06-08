from Items import *
from Enemys.Enemy import Enemy


class Rat(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 25
        self.hp = self.max_hp  # хп противника
        self.damage1 = 1
        self.damage2 = 3
        self.money = 5
        self.xp = 5
        self.name = "Крыса"
        self.description = "Крыса 🐀"
        self.death = "Ты добил крысу"
        self.sticker = "CAACAgIAAxkBAAEEonpidAX8NoblMe8cdTaSeZiIIyIAAVQAAvQYAAKjVZlLiO25jHP6UVYkBA"
        self.loot = [Wool()]
