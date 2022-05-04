from Enemys.Enemy import Enemy


class Goblin(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.hp = 55
        self.damage1 = 4
        self.damage2 = 9
        self.money = 15
        self.xp = 25
        self.name = "Гоблин"
        self.description = 'Мелкое, противное, хитрое и крайне омерзительное чудовище ' \
                           'размером не выше семилетнего ребенка'
        self.death = "Одной мелкой тварью меньше"
