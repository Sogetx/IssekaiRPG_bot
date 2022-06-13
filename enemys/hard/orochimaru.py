from items import *
from enemys.enemy import Enemy


class Orochimaru(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 250
        self.hp = self.max_hp
        self.damage1 = 5
        self.damage2 = 8
        self.money = 95
        self.xp = 300
        self.name = "Орочимару"
        self.description = "Убил 3-го хокаге"
        self.death = "Ушел, оставив тебе свою награду, и стал мамой"
        self.sticker = "CAACAgIAAxkBAAEE-A5ipKkxIefRIPLRnEEO1fPJg2fW6AAC_xoAAurNIUmHJWi5LnMnDSQE"
        self.loot = [Fang()]
