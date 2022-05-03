import random
from constants import *


class User:

    def __init__(self):
        self.money = 200
        self.max_hp = 100
        self.hp = self.max_hp
        self.damage1 = 1
        self.damage2 = 10
        self.menu = MAIN_MENU

    def __repr__(self):  # Статистика пользователя
        return "Текущее ХП: {0} ❤\nМаксимальное ХП: {1} ❤\n{2} 💵\n{3}-{4} 💥\n".\
            format(self.hp, self.max_hp, self.money, self.damage1, self.damage2)

    def to_damage(self):  # Нанесение урона
        return random.randint(self.damage1, self.damage2)

    def take_damage(self, received_damage):  # Получение урона
        self.hp -= received_damage
        return received_damage

    def death_msg(self):
        return "Ты вмэр 💀\n\nТвоя статистика:\n" +\
               "Максимальное ХП: {0} ❤\n{1} 💵\n{2}-{3} 💥\n".\
                   format(self.max_hp, self.money, self.damage1, self.damage2)  # + статистика
