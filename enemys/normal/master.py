from items import *
from enemys.enemy import Enemy


class Master(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 100
        self.hp = self.max_hp
        self.damage1 = 8
        self.damage2 = 10
        self.money = 60
        self.xp = 55
        self.name = "Создатель"
        self.description = 'Существо абсолютно безформеное только слегка напоминающие человека. Мечтает сделать мир ' \
                           'лучше вмешавшись в природу человека. '
        self.death = "Мечтам идеального мира выродков не суждено было сбыться"
        self.sticker = "CAACAgIAAxkBAAEE-AhipKa4t556TM-BkbvNAAH8gW0mfNsAArMZAAIg5ylJOgABjObs2gABJSQE"
        self.loot = []
