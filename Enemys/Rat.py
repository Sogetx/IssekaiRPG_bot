from Enemys.Enemy import Enemy

class Rat(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 25
        self.damage1 = 1
        self.damage2 = 3
        self.money1 = 0
        self.money2 = 5
        self.description = "Крыса 🐀"
        self.death = "Ты убил крысу"

    # def to_damage(self):
    #     return random.randint(self.damage1, self.damage2)
    #
    # def take_damage(self, received_damage):
    #     self.hp -= received_damage
    #
    # def __repr__(self):
    #     return "{0}❤, {1} - {2}💥".format(self.hp, self.damage1, self.damage2)
