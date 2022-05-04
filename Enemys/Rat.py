from Enemys.Enemy import Enemy


class Rat(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 25
        self.damage1 = 1
        self.damage2 = 3
        self.money = 5
        self.xp = 5
        self.name = "Крыса"
        self.description = "Крыса 🐀"
        self.death = "Ты добил крысу"
