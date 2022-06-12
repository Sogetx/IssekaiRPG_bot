from Enemys.Enemy import Enemy


class Nezuko(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 90
        self.hp = self.max_hp
        self.damage1 = 6
        self.damage2 = 10
        self.money = 50
        self.xp = 50
        self.name = "Незуко"
        self.description = '*пытается что-то сказать с закрытым ртом*'
        self.death = "*мило плачет*"
        self.sticker = "CAACAgIAAxkBAAEE-BJipKz4Grg4zCB-eKtiQlp9nSIfDwACNRcAAjh-KUmN9Z1pI2lKHSQE"
        self.loot = []
