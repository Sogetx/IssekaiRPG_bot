import random

from Items import *
from Enemys.Enemy import Enemy


class Super_Sus(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 55
        self.hp = self.max_hp  # хп противника
        self.damage1 = 4
        self.damage2 = 9
        self.money = 15
        self.xp = 25
        self.name = "Супер сус"
        self.description = 'надо описание'
        self.death = "надо смерть"
        self.sticker = "CAACAgIAAxkBAAEEonxidAYAAbCeIdVXU6mTTRCqvY_tw2gAAnkYAAJymJhLrpRlJmL2F6IkBA"
        self.loot = []
        val = random.randint(1, 10)
        if val == 1:  # шанс 1 к 10 что лут золотая кнопка
            self.loot.append(Golden_YTB)
        elif 1 < val < 5:  # шанс 3 к 10 что лут серебряная кнопка
            self.loot.append(Silver_YTB)
