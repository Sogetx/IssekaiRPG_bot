from Items import *
from Enemys.Enemy import Enemy


class Bowser(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 200
        self.hp = self.max_hp
        self.damage1 = 9
        self.damage2 = 11
        self.money = 140
        self.xp = 220
        self.name = "Боузер"
        self.description = 'Тот самый монстр из Марио что постоянно крадет принцессу.'
        self.death = "Боузер побежден но принцеcса неоценила вашего героизма и ушла."
        self.sticker = "CAACAgIAAxkBAAEE99pipIhTmeXPLRNSu-az5jSHCsQYuAAC1xwAAsnIEEmIZZDJ7VwpIiQE"
        self.loot = [Turtle_shell()]
