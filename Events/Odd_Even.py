import random
from Events.Event import Event
from constants import bot


class Odd_Even(Event):
    def __init__(self):
        super().__init__()
        self.name = "Четное-Нечетное"
        self.description = "Сейчас тебе покажется случайное число, нужно угадать является оно четным или же нет" \
                           "\n\nЕсли угадаеш, то получиш 50 💵, если нет - то потеряеш 50 💵\n\nВыбирай:"
        self.buttons = ["Четное", "Нечетное", ""]
        self.is_active = True

    def active_action(self, user, msg):
        val = random.randint(1, 100)
        if (msg == "Четное" and val % 2 == 0) or (msg == "Нечетное" and val % 2 == 1):
            user.money += 50
            bot.send_message(user.id, "Число: " + str(val) + "\n\n🎉Ты угадал!🎉\n\nРезультат: +50 💵")
            return True
        elif (msg == "Четное" and val % 2 == 1) or (msg == "Нечетное" and val % 2 == 0):
            mon = 50
            if user.money < 50:
                mon = user.money
            bot.send_message(user.id, "Число: " + str(val) + "\n\nТы не угадал.\n\nРезультат: -" + str(mon) + "💵")
            user.minusmoney(mon)
            return True
        else:
            return False
