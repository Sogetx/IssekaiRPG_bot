from Items import *
from Enemys.Enemy import Enemy


class Caravan(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 1000
        self.hp = self.max_hp  # хп противника
        self.damage1 = 0
        self.damage2 = 0
        self.money = 300
        self.xp = 0
        self.run_att = 1  # чтоб караван не сбежал
        self.name = "Караван"
        self.description = 'Долго бить, но награда стоит того'
        self.death = "Караван ограблен"
        self.sticker = "CAACAgIAAxkBAAEEonxidAYAAbCeIdVXU6mTTRCqvY_tw2gAAnkYAAJymJhLrpRlJmL2F6IkBA"
        self.loot = []
