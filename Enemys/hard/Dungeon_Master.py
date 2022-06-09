from Items import *
from Enemys.Enemy import Enemy


class Dungeon_Master(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 55
        self.hp = self.max_hp  # хп противника
        self.damage1 = 4
        self.damage2 = 9
        self.money = 15
        self.xp = 25
        self.name = "♂Dungeon Master♂"
        self.description = 'Надо описание'
        self.death = "Одной мелкой тварью меньше"
        self.sticker = "CAACAgIAAxkBAAEEonxidAYAAbCeIdVXU6mTTRCqvY_tw2gAAnkYAAJymJhLrpRlJmL2F6IkBA"
        self.loot = []
