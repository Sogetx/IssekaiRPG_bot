from Items import *
from Enemys.Enemy import Enemy


class Ork(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 100
        self.hp = self.max_hp  # хп противника
        self.damage1 = 7
        self.damage2 = 11
        self.money = 40
        self.xp = 50
        self.name = "Орк"
        self.description = "Большое тупое создание, пришло своровать твой 🚽"
        self.death = "Za путина!"
        # self.sticker = ""
        self.loot = []
