from items import *
from enemys.Enemy import Enemy


class Cacodemon(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 80
        self.hp = self.max_hp
        self.damage1 = 9
        self.damage2 = 12
        self.money = 50
        self.xp = 50
        self.name = "Какодемон"
        self.description = 'Название демона сполна описывает его суть'
        self.death = "Ты убил большую летающую фрикадельку"
        self.sticker = "CAACAgIAAxkBAAEE99RipIhNCnRUNXJHVcCz4o6fIGp_WAACTxwAAshZEEk6ze16f6ar9SQE"
        self.loot = [BigEye()]
