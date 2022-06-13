from items import *
from enemys.enemy import Enemy


class Rat(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 25
        self.hp = self.max_hp
        self.damage1 = 1
        self.damage2 = 3
        self.money = 5
        self.xp = 5
        self.name = "🐀"
        self.description = "Вы встречаете здоровую крысу копающуюся в вашем холодильнике. Может мусорить дома меньше " \
                           "надо чтоб таких тварей не встречать? "
        self.death = "Ты добил крысу и возможно спас часть еды с холодильника."
        self.sticker = "CAACAgIAAxkBAAEE-B9ipLMcSYlZihQw82e2uPIUKtUQ9gACFhkAAqAMKUlSFm2iQyRMQCQE"
        self.loot = [Wool()]
