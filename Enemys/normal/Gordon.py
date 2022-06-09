from Items import *
from Enemys.Enemy import Enemy


class Gordon(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 110
        self.hp = self.max_hp  # хп противника
        self.damage1 = 7
        self.damage2 = 14
        self.money = 55
        self.xp = 55
        self.name = "Дмитрий Гордон"
        self.description = 'Я тебе кадык вырву с*ка'
        self.death = "Смерть мусорам, Свободу пацанам"
        # self.sticker = ""
        self.loot = [Adams_apple(), Candy()]
