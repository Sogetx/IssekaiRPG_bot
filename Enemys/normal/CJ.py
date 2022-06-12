from Items import *
from Enemys.Enemy import Enemy


class CJ(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 90
        self.hp = self.max_hp
        self.damage1 = 8
        self.damage2 = 12
        self.money = 50
        self.xp = 45
        self.name = "Си Джей"
        self.description = "Гроу стрит рулит"
        self.death = "Ah shit here we go again"
        self.sticker = "CAACAgIAAxkBAAEE9-JipIhabT9RYs9VZfmGggznmru9OgACgBoAAiliEUm2YjT2G4J9ICQE"
        self.loot = [White_shirt()]
