from buttons_generator import buttons_generator
from constants import *
from Pets import *


class User:

    def __init__(self, uid):
        self.id = uid  # айди пользователя
        self.money = 200  # деньги
        self.max_hp = 100  # максимальное здоровье
        self.hp = self.max_hp  # здоровье
        self.power = 10  # Сила (урон без предметов)
        self.damage = self.power  # урон
        self.defence = 1  # защита
        self.enemy_count = 0  # кол-во убитых мобов
        self.go_ahead_count = 0  # кол-во совершеных походов
        self.xp = 0  # опыт
        self.xp_to_lvl = 100  # сколько опыта до след. уровня
        self.lvl = 1  # уровень
        self.menu = MAIN_MENU  # в каком меню находится пользователь
        self.enemy = None  # с каким мобов бьется игрок
        self.event = None  # ивент
        self.crit = 5  # шанс крит удара
        self.items = {
            Big_hp_potion().name: [Big_hp_potion(), 1]}  # предметы в инвентаре в виде "ключ: [предмет, кол-во]"
        # страничка инвентаря (если делать через отдельный аргумент в методе, то работает не так  как нужно почемуто)
        self.inv_page = 1
        self.pet = Pet()  # без модификаторов

    def __repr__(self):  # Статистика пользователя
        msg = "Уровень: {0}\nХП: {1}/{2} ❤\nДеньги: {3} 💵\nОпыт: {4}/{5} ⭐\nУрон: {6} 💥\nСила: {7} 💪\nШанс крита: " \
              "{8} 🎯\nЗащита: {9} 🛡\nУбито мобов: {10} 👹\nСовершено походов: {11} 🚶‍♂". \
            format(self.lvl, self.hp, self.max_hp, self.money, self.xp, self.xp_to_lvl, self.damage, self.power,
                   self.crit, self.defence, self.enemy_count, self.go_ahead_count)
        if self.pet.name is not None:
            msg += "\n\nПитомец:\n{0}\n{1}\nx{2} 💥, x{3} 💪, x{4} 🛡\n". \
                format(self.pet.name, self.pet.description, self.pet.damage, self.pet.power, self.pet.defence)
        return msg

    def to_damage(self, weapon, msg):  # Нанесение урона
        if weapon:
            return int(self.items[msg][0].damage * self.pet.damage)
        else:
            return int(self.damage * self.pet.power * self.pet.damage)

    def take_damage(self, received_damage):  # Получение урона
        self.hp -= int(max(received_damage - ((self.defence * self.pet.defence) // 2), 0))
        return received_damage

    def add_xp(self, add):
        self.xp += add
        if self.xp >= self.xp_to_lvl and self.lvl < 25:
            self.xp -= self.xp_to_lvl
            self.xp_to_lvl = int(self.xp_to_lvl * 1.3)
            self.lvl += 1
            self.menu = NEW_LVL
            bot.send_message(self.id, "🎉Ты получил {0} уровень🎉 {1}"
                                      "\n\nТвои характеристики:\n\n"
                                      "Сила: {2} 💪\nЗащита: {3} 🛡\nШанс крита: {4} 🎯\n"
                                      "Максимальное ХП: {5}❤\n\nВыбери какую хар-ку ты хочешь увеличить:".
                             format(self.lvl, self.get_pet(), self.power, self.defence, self.crit, self.max_hp),
                             reply_markup=buttons_generator([ADD_POWER, ADD_DEFENCE, ADD_CRIT, ADD_HP]))
            if self.lvl % 5 == 0:
                bot.send_sticker(self.id, self.pet.sticker)
            return True

    def addpower(self, plus_power):
        self.power += plus_power
        self.damage += plus_power

    def heal(self, heal_hp):
        self.hp = min(self.hp + heal_hp, self.max_hp)

    def minusmoney(self, minus):
        self.money = max(self.money - minus, 0)

    def add_item(self, item):
        if item.name not in self.items.keys():
            self.items[item.name] = [item, 1]
        else:
            self.items[item.name][1] += 1

    def get_pet(self):
        if self.lvl % 5 != 0:
            return ""
        else:
            if self.lvl == 5:
                self.pet = Wolf()
            # elif self.lvl == 10:
            #    self.pet =
            # elif self.lvl == 15:
            #     self.pet =
            # elif self.lvl == 20:
            #     self.pet =
            # elif self.lvl == 25:
            #     self.pet =
            return "\n\nИ нового питомца:\n\n" + repr(self.pet)

            # тут дальше сделаю систему выбора петов с разными бафами
