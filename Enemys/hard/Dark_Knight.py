from Items import *
from Enemys.Enemy import Enemy


class Dark_Knight(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 140
        self.hp = self.max_hp  # хп противника
        self.damage1 = 10
        self.damage2 = 15
        self.money = 100
        self.xp = 300
        self.name = "Темный рыцарь"
        self.description = 'Дойстойный рыцарь нашего времени'
        self.death = "Латексное воинство лишилось своего командира"
        self.sticker = "CAACAgIAAxkBAAEE99ZipIhPxQFM0VDJppXvVkIMV0CM6gACSx0AAqbfEUlA1uaTAAFhoAMkBA"
        self.loot = [Police_cap()]
