from Items import *
from Enemys.Enemy import Enemy


class Grass(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 1
        self.hp = self.max_hp  # хп противника
        self.money = 1
        self.xp = 1
        self.name = "Трава"
        self.description = 'Тебе показалось что на тебя быканула обычная безобидная травка'
        self.death = "Непонимаю зачем нужно было нападать на траву"
        self.sticker = "CAACAgIAAxkBAAEE985ipIgmlCKt_fHb0L6S3_mXrHQ1yAAC9x4AAiHeKUm0uNZakWkwwiQE"
