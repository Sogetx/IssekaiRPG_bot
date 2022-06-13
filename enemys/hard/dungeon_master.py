from items import *
from enemys.enemy import Enemy


class DungeonMaster(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 180
        self.hp = self.max_hp
        self.damage1 = 11
        self.damage2 = 15
        self.money = 100
        self.xp = 350
        self.name = "♂Dungeon Master♂"
        self.description = "Ну вы его знаете: Swallow my ♂🥛♂"
        self.death = "Rest in peace Billy."
        self.sticker = "CAACAgIAAxkBAAEE99xipIhVrKaP-T8clHc1QyVo344jlQACbxoAAmDWEElL_TTMPLKX9CQE"
        self.loot = [BeltBilly()]
