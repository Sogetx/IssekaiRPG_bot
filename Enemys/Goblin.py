from Enemys.Enemy import Enemy


class Goblin(Enemy): # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.hp = 55
        self.damage1 = 4
        self.damage2 = 9
        self.money = 15
        self.xp = 25
        self.description = 'Гоблин.\nМелкое, противное, хитрое и крайне омерзительное чудовище размером не выше 7 летнего ребенка.'
        self.death = "Одной мелкой тварью меньше."