from items import *
from enemys.Enemy import Enemy


class Dio(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 170
        self.hp = self.max_hp
        self.damage1 = 9
        self.damage2 = 12
        self.money = 100
        self.xp = 300
        self.name = "Дио"
        self.description = 'За Вардо'
        self.death = "Ты переиграл его переигрывание"
        self.sticker = "CAACAgIAAxkBAAEE995ipIhXdZUYlUMhJG-mW8X0S3SmjgACPx4AAovfEUmQZSnYbAPkYiQE"
        self.loot = [StandArrow()]
