from constants import *


class User:

    def __init__(self):
        self.money = 200  # деньги
        self.max_hp = 10  # максимальное здоровье
        self.hp = self.max_hp  # здоровье
        self.power = 10  # Сила (урон без предметов)
        self.damage = self.power  # урон
        self.defence = 1  # защита
        self.enemy_count = 0  # кол-во убитых мобов
        self.go_ahead_count = 0  # кол-во встреченых мобов
        self.xp = 0  # опыт
        self.xp_to_lvl = 100  # сколько опыта до след. уровня
        self.lvl = 1  # уровень
        self.menu = MAIN_MENU  # в каком меню находится пользователь

    def __repr__(self):  # Статистика пользователя
        return "Уровень: {10}\nТекущее ХП: {0} ❤\nМаксимальное ХП: {1} ❤\nДеньги: {2} 💵\n" \
               "Опыт: {3}/{4} ⭐\nУрон: {5} 💥\nСила: {6} 💪" \
               "\nЗащита: {7} 🛡\nУбито мобов: {8} ⚔\nВстречено мобов и ивентов: {9} 👹". \
            format(self.hp, self.max_hp, self.money, self.xp, self.xp_to_lvl, self.damage, self.power, self.defence,
                   self.enemy_count, self.go_ahead_count, self.lvl)

    def to_damage(self):  # Нанесение урона
        return self.damage

    def take_damage(self, received_damage):  # Получение урона
        self.hp -= received_damage - self.defence // 2
        return received_damage

    def death_msg(self):
        return "Ты вмэр 💀\n\nТвоя статистика:\n" + \
               "Максимальное ХП: {0} ❤\n{1} 💵\n{2} 💥\n". \
                   format(self.max_hp, self.money, self.damage)  # + статистика

    def next_lvl(self):
        if self.xp >= self.xp_to_lvl:
            self.xp -= self.xp_to_lvl
            self.xp_to_lvl = int(self.xp_to_lvl * 1.5)
            self.lvl += 1
            return True

    def addpower(self, plus_power):
        self.power += plus_power
        self.damage += plus_power

    def adddamage(self, plus_damage):
        self.damage += plus_damage

    def heal(self, heal_hp):
        self.hp = min(self.hp + heal_hp, self.max_hp)

    def minusmoney(self, minus):
        self.money = max(self.money-minus, 0)
