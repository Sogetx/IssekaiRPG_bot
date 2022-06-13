from enemys.enemy import Enemy


class LightYagami(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 50
        self.hp = self.max_hp
        self.damage1 = 999999999
        self.damage2 = 999999999
        self.money = 50
        self.xp = 500
        self.name = "Лайт Ягами"
        self.description = "Да, Кира это я"
        self.death = "Убив его ты сказал - ""Это тебе за L"""
        self.sticker = "CAACAgIAAxkBAAEE-AxipKjz5U6uMSOP1jPUOG97VSQi8gACex4AAuSGKUnWmZrfzO3ZOyQE"
        self.loot = []

    def __repr__(self):  # Характеристики моба
        return "{0}❤, урон: ∞💥".format(self.hp)
