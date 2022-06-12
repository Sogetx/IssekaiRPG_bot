import random
from Items import *
from Enemys.Enemy import Enemy


class Super_Sus(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 75
        self.hp = self.max_hp
        self.damage1 = 4
        self.damage2 = 5
        self.money = 50
        self.xp = 50
        self.name = "Супер сус"
        self.description = 'Человек небольшого размера известен тем что влезет в любую нору, щель или заброшку'
        self.death = "Вы убили легенду"
        self.sticker = "CAACAgIAAxkBAAEE8x5ioe6QnepWS6tcY0oOpPirq3dHrwAC-xgAAmHMEElJOzpZkbyi4iQE"
        self.loot = []
        val = random.randint(1, 10)
        if val == 1:  # шанс 1 к 10 что лут золотая кнопка
            self.loot.append(Golden_YTB())
        elif 1 < val < 5:  # шанс 3 к 10 что лут серебряная кнопка
            self.loot.append(Silver_YTB())
