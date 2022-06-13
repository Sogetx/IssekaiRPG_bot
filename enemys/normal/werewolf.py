from items import *
from enemys.enemy import Enemy


class Werewolf(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 110
        self.hp = self.max_hp
        self.damage1 = 9
        self.damage2 = 12
        self.money = 20
        self.xp = 75
        self.name = "Оборотень"
        self.description = "Днём он человек, а ночью звереет в ожидании нового сезона ДжоДжо. \nМожет все таки не " \
                           "стоит лазить по ночам чтоб с такими типами не встречаться? "
        self.death = "Ты избавил от мучений этого бедолагу"
        self.sticker = "CAACAgIAAxkBAAEE99JipIhKaZk3XOj73ANSKVSlKWyO6QACxhgAAiZcEEnoc0M4oQZyTCQE"
        self.loot = [Fang(), Wool(), Meat()]
