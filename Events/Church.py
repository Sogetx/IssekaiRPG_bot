from Events.Event import Event
import random

class Church(Event):
    def __init__(self):
        super().__init__()
        self.description = "Вы заходите в небольшое святилище, оно аккуратное, чистое хотя никого в нем нету. " \


    def action(self, user):
        val = random.randint(1, 2)
        if val == 1:
            result = user.max_hp - user.hp
            user.heal(user.max_hp)
            return "Постояв у алтаря вам становиться легче а раны затягиваються.\n+" + str(result) + " ❤"
        elif val == 2:
            return "Вы думали что боги смилуються над вами?\nМожете раслабиться вы им все также безраличны как и раньше."
        else:
            return 0 # заглушка для вставки битвы с мобов в будующем
