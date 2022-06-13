from items import *
from enemys.Enemy import Enemy


class DarkKnight(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 140
        self.hp = self.max_hp
        self.damage1 = 10
        self.damage2 = 15
        self.money = 100
        self.xp = 300
        self.name = "Темный рыцарь"
        self.description = 'Дойстойный рыцарь нашего времени'
        self.death = "Латексное воинство лишилось своего командира"
        self.sticker = "CAACAgIAAxkBAAEE99ZipIhPxQFM0VDJppXvVkIMV0CM6gACSx0AAqbfEUlA1uaTAAFhoAMkBA"
        self.loot = [PoliceCap()]
