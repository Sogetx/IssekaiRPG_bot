from Events.Event import Event
import random


class Church(Event):
    def __init__(self):
        self.description = "Вы заходите в небольшое святилище, оно аккуратное, чистое хотя никого в нем нету. " \


    def action(self, user):
        val = random.randint(1, 2)
        if val == 1:
            result = min(user.max_hp-user.hp, user.max_hp//4)
            user.heal(result)
            return "Постояв у алтаря вам становиться легче а раны затягиваються.\n\n+" + str(result) + " ❤"
        else:
            return "Вы думали что боги смилуються над вами?\n\n" \
                   "Можете раслабиться вы им все также безраличны как и раньше."
        # else:
        #     return 0  # заглушка для вставки битвы с мобов в будующем
