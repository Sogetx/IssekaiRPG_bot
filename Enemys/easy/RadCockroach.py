from Items import *
from Enemys.Enemy import Enemy


class RadCockroach(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 50
        self.hp = self.max_hp  # хп противника
        self.damage1 = 2
        self.damage2 = 5
        self.money = 5
        self.xp = 15
        self.name = "Радтаракан"
        self.description = "ТАРАКАН ААААААААА"
        self.death = "Ты раздавил его, маленького, бедного таракашку. Что ж ты за человек?"
        self.sticker = "CAACAgIAAxkBAAEEon5idAYDWTUgJIt7qjJRJVpnIbnM-wACGxgAAr6MkEuPx1Y-cS-V9iQE"
        self.loot = [Meat()]
