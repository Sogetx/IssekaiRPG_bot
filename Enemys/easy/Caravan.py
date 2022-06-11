from Items import *
from Enemys.Enemy import Enemy


class Caravan(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 3000
        self.hp = self.max_hp  # хп противника
        self.money = 400
        self.run_att = 1  # чтоб караван не сбежал
        self.name = "Караван"
        self.description = 'Долго бить, но награда стоит того'
        self.death = "Караван ограблен"
        self.sticker = "CAACAgIAAxkBAAEEonxidAYAAbCeIdVXU6mTTRCqvY_tw2gAAnkYAAJymJhLrpRlJmL2F6IkBA"
        self.loot = []
