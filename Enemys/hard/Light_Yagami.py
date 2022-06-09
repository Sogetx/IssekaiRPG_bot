from Items import *
from Enemys.Enemy import Enemy


class Light_Yagami(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 55
        self.hp = self.max_hp  # хп противника
        self.damage1 = 999999999
        self.damage2 = 999999999
        self.money = 15
        self.xp = 25
        self.name = "Лайт Ягами"
        self.description = 'Надо описание'
        self.death = "Одной мелкой тварью меньше"
        self.sticker = "CAACAgIAAxkBAAEEonxidAYAAbCeIdVXU6mTTRCqvY_tw2gAAnkYAAJymJhLrpRlJmL2F6IkBA"
        self.loot = []

    def __repr__(self):  # Характеристики моба
        return "{0}❤, урон: ∞💥".format(self.hp)
