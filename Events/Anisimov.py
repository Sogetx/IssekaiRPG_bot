import random

from Events.Event import Event
from buttons_generator import buttons_generator
from constants import bot


class Anisimov(Event):
    def __init__(self):
        super().__init__()
        self.name = "Анисимов"
        self.description = "Вы попали на экзамен к физику Анисимову А.В."
        self.is_active = True

    def action(self, user):
        question = random.choice(["В чем измеряется сила?",
                                  "Чему равно ускорение свободного падения?",
                                  "Что из этого самое тяжелое?",
                                  "Примерная скорость движения света?",
                                  "Формула скорости?"])
        answers = {"В чем измеряется сила?": ["В любви", "Дж", "Н"],
                   "Чему равно ускорение свободного падения?": ["10,3", "9,8", "10"],
                   "Что из этого самое тяжелое?": ["Вода", "Лед", "Пар"],
                   "Примерная скорость движения света?": ["300000 км/с", "300000 м/с", "300000 см/с"],
                   "Формула скорости?": ["v/t", "l/t", "t/l"]}
        bot.send_message(user.id, question, reply_markup=buttons_generator(answers[question]))

    def answer(self, user, msg):
        if msg in ["Н", "9,8","Вода","300000 км/с","l/t"]:
            user.money += 50
            bot.send_message(user.id, "Молодец, правильно, вот твои 50 денег")
        else:
            bot.send_message(user.id, "Неверно! Теперь все твои деньги мои!!!")
            bot.send_sticker(user.id, "CAACAgIAAxkBAAEE7MZini34iaGG7nqav_UbdVmTIJbF6wACAgADNpB7Ot2m94b8xdNVJAQ")
            user.money = 0
