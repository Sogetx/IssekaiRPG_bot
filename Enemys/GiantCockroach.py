from Enemys.Enemy import Enemy


class GiantCockroach(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 50
        self.damage1 = 2
        self.damage2 = 5
        self.money = 5
        self.xp = 15
        self.description = "ТАРАКАН ААААААААА"
        self.death = "Ты раздавил его, маленького, бедного таракашку. Что ж ты за человек?"
