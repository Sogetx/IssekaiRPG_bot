from enemys.enemy import Enemy


class Grass(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 1
        self.hp = self.max_hp
        self.money = 1
        self.xp = 1
        self.name = "Трава"
        self.description = 'Тебе показалось что на тебя быканула обычная безобидная травка'
        self.death = "Непонимаю зачем нужно было нападать на траву"
        self.sticker = "CAACAgIAAxkBAAEE985ipIgmlCKt_fHb0L6S3_mXrHQ1yAAC9x4AAiHeKUm0uNZakWkwwiQE"
