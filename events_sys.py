import random
from Events import *


def events_create(user_id, events, user):  # Генерация ивентов
    # генерируем определенного моба на условии того какое число выпадет
    evnt = random.randint(1, 2)
    if evnt == 1:
        events[user_id] = test.Test()
        # user.heal(user.max_hp)  # полный отхил
        user.minusmoney(5)  # - 5 денег
    else:
        events[user_id] = church.Church()
        user.heal(user.max_hp)
    return events[user_id].description

# def events_traits(user_id,events):
# event = events[user_id]
# if evnt == 1:
#     event.regenerate
# else:
#    event.regenerate
