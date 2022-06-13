from items import *
from enemys.Enemy import Enemy


class AgentSmith(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 160
        self.hp = self.max_hp
        self.damage1 = 10
        self.damage2 = 14
        self.money = 100
        self.xp = 200
        self.name = "Аген Смитт"
        self.description = 'Делового вида человек с какого-то известного фильма'
        self.death = "Мистер Андерсон вы так ничего и не поняли"
        self.sticker = "CAACAgIAAxkBAAEE99hipIhRyPXIelsAAXI32WbTLjs8AAHAAAImGQACpDIRSSMIKc4tRHxsJAQ"
        self.loot = [Sunglasses()]
