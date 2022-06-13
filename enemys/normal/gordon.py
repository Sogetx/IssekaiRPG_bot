from items import *
from enemys.Enemy import Enemy


class Gordon(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 100
        self.hp = self.max_hp
        self.damage1 = 9
        self.damage2 = 12
        self.money = 60
        self.xp = 50
        self.name = "Дмитрий Гордон"
        self.description = 'Я тебе кадык вырву с*ка'
        self.death = "Пришло время"
        self.sticker = "CAACAgIAAxkBAAEE9-RipIhdyzb7FRsVTIvOruQ41zc1gQAChxoAAosXGUkKqxf8GgS0CCQE"
        self.loot = [AdamsApple(), Candy()]
