from items import *
from enemys.Enemy import Enemy


class Zombie(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 70
        self.hp = self.max_hp
        self.damage1 = 3
        self.damage2 = 6
        self.money = 20
        self.xp = 30
        self.name = 'Зомби'
        self.description = 'Довольно неприятное существо, передвигается и ведет себя как типичный победитель ' \
                           'Октоберфеста. Единственный кто реально ценит ваши мозги'
        self.death = "Вы убили то что и так уже мертво"
        self.sticker = "CAACAgIAAxkBAAEE-BlipLCqgF6w1ovAnTsoyKmAxFrEkAACJhoAAgwRKUn-THMTQG0LoyQE"
        self.loot = [Meat()]
