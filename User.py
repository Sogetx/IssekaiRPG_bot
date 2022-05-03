import random
from constants import *


class User:

    def __init__(self):
        self.money = 200  # деньги
        self.max_hp = 100  # максимальное здоровье
        self.hp = self.max_hp  # здоровье
        self.power = 10  # Сила (урон без предметов)
        self.damage = self.power  # урон
        self.defence = 1  # защита
        self.enemy_count = 0
        self.enemy_met_count = 0
        self.menu = MAIN_MENU  # в каком меню находится пользователь

    def __repr__(self):  # Статистика пользователя
        return "Текущее ХП: {0} ❤\nМаксимальное ХП: {1} ❤\nДеньги: {2} 💵\nУрон: {3} 💥\nСила: {4} 💪" \
               "\nЗащита: {5} 🛡\nУбито мобов: {6}\nВстречено мобов: {7} 👹".\
            format(self.hp, self.max_hp, self.money, self.damage, self.power, self.defence,
                   self.enemy_count, self.enemy_met_count)

    def to_damage(self):  # Нанесение урона
        return self.damage

    def take_damage(self, received_damage):  # Получение урона
        self.hp -= received_damage
        return received_damage

    def death_msg(self):
        return "Ты вмэр 💀\n\nТвоя статистика:\n" +\
               "Максимальное ХП: {0} ❤\n{1} 💵\n{2} 💥\n".\
                   format(self.max_hp, self.money, self.damage)  # + статистика

    def addpower(self, plus_power):
        self.power += plus_power
        self.damage += plus_power

    def adddamage(self, plus_damage):
        self.damage += plus_damage


