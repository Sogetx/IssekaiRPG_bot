from items import *
from enemys.enemy import Enemy


class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 55
        self.hp = self.max_hp
        self.damage1 = 4
        self.damage2 = 9
        self.money = 15
        self.xp = 25
        self.name = "Гоблин"
        self.description = 'Мелкое, противное, хитрое и крайне омерзительное чудовище ' \
                           'размером не выше семилетнего ребенка'
        self.death = "Одной мелкой тварью меньше"
        self.sticker = "CAACAgIAAxkBAAEEonxidAYAAbCeIdVXU6mTTRCqvY_tw2gAAnkYAAJymJhLrpRlJmL2F6IkBA"
        self.loot = [Fang()]
