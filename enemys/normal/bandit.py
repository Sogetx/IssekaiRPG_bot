from enemys.enemy import Enemy


class Bandit(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 90
        self.hp = self.max_hp
        self.damage1 = 8
        self.damage2 = 12
        self.money = 50
        self.xp = 45
        self.name = "Бандит"
        self.description = 'Человек лишенный положительних моральных качеств как бы в фильмы не доказывали обратное'
        self.death = "Ля, маслину поймал!"
        self.sticker = "CAACAgIAAxkBAAEE-BBipKr2RBywDWBrpRahT5a6_4a8mgACgBgAAiGIKUlETpEgg1cAAZckBA"
        self.loot = []
