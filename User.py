from constants import *


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
        self.items = {'Нож': Knife.Knife(), "Малое зелье хп": Small_hp_potion.Small_hp_potion()}  # тестовые данные
        # self.items = {}  # предметы в инвентаре
        # страничка инвентаря (если делать через отдельный аргумент в методе, то работает не так  как нужно почемуто)
        self.inv_page = 1
        self.pet = Pet.Pet()

    def __repr__(self):  # Статистика пользователя
        msg = "Уровень: {0}\nТекущее ХП: {1} ❤\nМаксимальное ХП: {2} ❤\nДеньги: {3} 💵\n" \
              "Опыт: {4}/{5} ⭐\nУрон: {6} 💥\nСила: {7} 💪\nШанс крита: {8} 🎯" \
              "\nЗащита: {9} 🛡\nУбито мобов: {10} 👹\nСовершено походов: {11} 🚶‍♂". \
            format(self.lvl, self.hp, self.max_hp, self.money, self.xp, self.xp_to_lvl, self.damage, self.power,
                   self.crit, self.defence, self.enemy_count, self.go_ahead_count)
        if self.pet.name is not None:
            msg += "\n\nПитомец:{0}\n{1}\nМодификатор 💥: {2}\nМодификатор 💪: {3}\nМодификатор 🛡: {4}\n". \
                format(self.pet.name, self.pet.description, self.pet.damage, self.pet.power, self.pet.defence)
        return msg

    def to_damage(self, weapon, msg):  # Нанесение урона
        if weapon:
            return int(self.items[msg].damage * self.pet.damage)
        else:
            return int(self.damage * self.pet.power * self.pet.damage)

    def take_damage(self, received_damage):  # Получение урона
        self.hp -= int(max(received_damage - ((self.defence * self.pet.defence) // 2), 0))
        return received_damage

    def death_msg(self):
        return "Ты вмэр 💀\n\nПричина смерти: {0}\n\nТвоя статистика:\n".format(self.enemy.name) + repr(self)

    def add_xp(self, add):
        self.xp += add
        if self.xp >= self.xp_to_lvl and self.lvl < 25:
            self.xp -= self.xp_to_lvl
            self.xp_to_lvl = int(self.xp_to_lvl * 1.3)
            self.lvl += 1
            self.get_pet()  # при достижении каждого 5-го уровня даеться питомец
            return True

    def addpower(self, plus_power):
        self.power += plus_power
        self.damage += plus_power

    def adddamage(self, plus_damage):
        self.damage += plus_damage

    def heal(self, heal_hp):
        self.hp = min(self.hp + heal_hp, self.max_hp)

    def minusmoney(self, minus):
        self.money = max(self.money - minus, 0)

    def add_item(self, item):
        if item.name not in self.items.keys():
            self.items[item.name] = item
        else:
            self.items[item.name].count += 1

    def get_pet(self):
        if self.lvl % 5 == 0:
            if self.lvl == 5:
                self.pet = Wolf.Wolf()
            elif self.lvl == 10:
                self.pet = Pet1.Pet1()
            # elif self.lvl == 15:
            #     self.pet =
            # elif self.lvl == 20:
            #     self.pet =
            # elif self.lvl == 25:
            #     self.pet =
            bot.send_message(self.id, "Ты получил нового питомца:\n\n{0}".format(repr(self.pet)))
            bot.send_sticker(self.id, self.pet.sticker)
            # тут дальше сделаю систему выбора петов с разными бафами
