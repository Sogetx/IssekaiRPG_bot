import random
from events.event import Event
from constants import bot


class Anisimov(Event):
    def __init__(self):
        super().__init__()
        self.name = "Анисимов"
        self.is_active = True

        answers = {"В чем измеряется сила?": ["В любви", "Дж", "Н"],
                   "Чему равно ускорение свободного падения?": ["10,3", "9,8", "10"],
                   "Что из этого самое тяжелое?": ["Вода", "Лед", "Пар"],
                   "Примерная скорость движения света?": ["300000 км/с", "300000 м/с", "300000 см/с"],
                   "Формула скорости?": ["v/t", "l/t", "t/l"]}
        question = random.choice(list(answers.keys()))

        self.description = "Вы попали на экзамен к физику Анисимову А.В.\n\nОтветиш верно: +100💵, неверно: " \
                           "-200💵\n\nВнимание: вопрос! \n" + question
        self.buttons = answers[question]

    def active_action(self, user, msg):
        if msg in ["Н", "9,8", "Вода", "300000 км/с", "l/t"]:
            user.money += 100
            bot.send_message(user.id, "🎉Молодец, правильно🎉\nВот твои 100 💵")
        elif msg in ["В любви", "Дж", "10,3", "10", "Лед", "Пар", "300000 м/с", "300000 см/с", "v/t", "t/l"]:
            val = 200
            if user.money < 200:
                val = user.money
            bot.send_message(user.id, "Неверно! Теперь " + str(val) + " твоих 💵 мои!!!")
            bot.send_sticker(user.id, "CAACAgIAAxkBAAEE7MZini34iaGG7nqav_UbdVmTIJbF6wACAgADNpB7Ot2m94b8xdNVJAQ")
            user.minusmoney(val)
