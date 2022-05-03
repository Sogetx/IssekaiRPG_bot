from Enemys.Enemy import Enemy


class Slime(Enemy): # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.hp = 30
        self.damage1 = 1
        self.damage2 = 6
        self.money = 7
        self.xp = 11
        self.description = 'Cлайм. \nБольшого размера сгусток слизи получивший сознание'
        self.death = "Слайм растекся и мокрого места не осталось"