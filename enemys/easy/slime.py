from enemys.enemy import Enemy


class Slime(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 30
        self.hp = self.max_hp
        self.damage1 = 1
        self.damage2 = 6
        self.money = 7
        self.xp = 11
        self.name = 'Слайм'
        self.description = 'Большого размера сгусток слизи получивший сознание'
        self.death = "Слайм растекся и мокрого места не осталось"
        self.sticker = "CAACAgIAAxkBAAEEonhidAX4km3ap7f0haUYzt5BSituTgACIxsAAm6RmEu0XLKlYU9AhCQE"
        self.loot = []
