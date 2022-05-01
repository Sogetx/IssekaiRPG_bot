import random


class User:

    def __init__(self, userid):
        self.userid = userid
        self.money = 200
        self.hp = 100
        self.damage1 = 1
        self.damage2 = 10

    def __repr__(self): # Вывод данных после хода
        return "{0}💵  {1}❤, урон: {2} - {3}💥".format(self.money, self.hp, self.damage1, self.damage2)

    def to_damage(self): # Нанесение урона
        return random.randint(self.damage1, self.damage2)

    def take_damage(self, received_damage): # Получение урона
        self.hp -= received_damage

    def death(self):
        return "Ты вмэр 💀"  # + статистика
