import random
from Events import *


def events_create(user):  # Генерация ивентов
    # генерируем определенный ивент на условии того какое число выпадет
    evnt = random.randint(1, 2)
    if evnt == 1:
        user.event = Tavern.Tavern()
    elif evnt == 2:
        user.event = Church.Church()
    return user.event.action(user)
