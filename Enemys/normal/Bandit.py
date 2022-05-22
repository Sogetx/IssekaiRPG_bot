from Items import *
from Enemys.Enemy import Enemy


class Bandit(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 90
        self.hp = self.max_hp  # хп противника
        self.damage1 = 8
        self.damage2 = 12
        self.money = 50
        self.xp = 45
        self.name = "Бандос"
        self.description = 'Человек лишенный положительних моральных качеств как бы в фильмы не доказывали обратное'
        self.death = "Смерть мусорам, Свободу пацанам"
        # self.sticker = ""
        self.loot = []
