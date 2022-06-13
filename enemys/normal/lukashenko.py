from items import *
from enemys.enemy import Enemy


class Lukashenko(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 110
        self.hp = self.max_hp
        self.damage1 = 1
        self.damage2 = 12
        self.money = 100
        self.xp = 60
        self.name = "Лукашенко"
        self.description = 'А я сейчас вам покажу, откуда на беларусь готовилось нападение. И если бы за шесть часов ' \
                           'до операции не был нанесён превентивный удар по позициям — четыре позиции, ' \
                           'я сейчас покажу карту, привёз — они бы атаковали наши войска, беларуси и россии, ' \
                           'которые были на учениях. Поэтому не мы развязали эту войну, у нас совесть чиста. Хорошо, ' \
                           'что начали. Биологическое оружие, самые большие атомные электростанции — и всё это были ' \
                           'готовы взорвать, '
        self.death = "Картошечный король ушел в мир иной"
        self.sticker = "CAACAgIAAxkBAAEE9-ZipIhhiVdgFpBCH6satg2t_sBvlQAC4BwAArNCIEkAAeNkcEh3_KQkBA"
        self.loot = [Potato(), Wool()]

