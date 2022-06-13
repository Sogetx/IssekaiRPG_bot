from items import *
from enemys.Enemy import Enemy


class Ork(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 100
        self.hp = self.max_hp
        self.damage1 = 7
        self.damage2 = 11
        self.money = 40
        self.xp = 50
        self.name = "Орк"
        self.description = "Мелкое тупое создание, пришло своровать твой 🚽"
        self.death = "Za путина!"
        self.sticker = "CAACAgIAAxkBAAEE-B1ipLJ7e3or0IvJTUEx7t3o33LUDQACORsAAkJ9KUmE5lTgDRrfeCQE"
        self.loot = [Horn(), Fang()]
