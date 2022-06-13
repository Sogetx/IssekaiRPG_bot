from items import *
from enemys.enemy import Enemy


class Kaneki(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 160
        self.hp = self.max_hp
        self.damage1 = 11
        self.damage2 = 15
        self.money = 70
        self.xp = 350
        self.name = "Канеки"
        self.description = 'Сколько будет 1000 - 7?'
        self.death = "Теперь он дединсайд в прямом и переносном смысле"
        self.sticker = "CAACAgIAAxkBAAEE9-BipIhYOdd958-aqHXEJFnLhoPYnwACqRsAAigBEUlAeuR4jgtKAAEkBA"
        self.loot = [Tentacle()]
