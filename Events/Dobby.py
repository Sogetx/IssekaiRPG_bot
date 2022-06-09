import random
from Events.Event import Event
from constants import bot, BACK


class Dobby(Event):
    def __init__(self):
        super().__init__()
        self.name = "Добби"
        self.description = "Добби хочет быть свободен. Даш Добби носок? Добби будет очень благодарен."
        self.buttons = ["Дать носок✅", "Не давать носок❌", ""]
        self.is_active = True

    def give_sock(self, user, msg):
        if msg == "Не давать носок❌":
            return True
        elif msg == "Дать носок✅":
            if not ("Носок 🧦" in user.items.keys()):
                bot.send_message(user.id, "У тебя нету носка")
                return True
            user.money += 200
            user.items["Носок 🧦"].use(user)
            bot.send_sticker(user.id, "CAACAgIAAxkBAAEE8utiod5drKCIr9VFeESUDKJbBgJUIgACgxgAAldJEEn8H67si4stVCQE")
            bot.send_message(user.id, "Cпасибо, вот моя тебе благодарность: \n +200 💵")
            return True
