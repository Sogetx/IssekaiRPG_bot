from Items import *
from Enemys.Enemy import Enemy


class Gollum(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 55
        self.hp = self.max_hp  # хп противника
        self.damage1 = 4
        self.damage2 = 9
        self.money = 15
        self.xp = 25
        self.name = "Голум"
        self.description = 'Лысое маленькое существо родственное гоблинам. Считает себя великим властелином всея руси.'
        self.death = "Погиб так и не реализовав силу кольца и свои бредовые идеи, ну зато хоть мир от себя спас."
        self.sticker = "CAACAgIAAxkBAAEE99BipIhEHawzQ4r6Dwe6ej-nokayNgACTBkAAhpUEElF2uENNrotZSQE"
        self.loot = [Ring_of_omnipotence()]
