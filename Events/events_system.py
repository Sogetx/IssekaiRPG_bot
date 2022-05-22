import random
from Events import *


def events_create(user):  # Генерация ивентов
    # генерируем определенный ивент на условии того какое число выпадет
    user.event = random.choice([Tavern(), Church()])
    return user.event.action(user)
