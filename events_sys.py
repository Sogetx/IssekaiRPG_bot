import types
import random

from telebot import *
from Events import *
def events_create(user_id, events):  # Генерация ивентов

        evnt = random.randint(1, 2) # генерируем определенного моба на условии того какое число выпадет
        if evnt == 1:
            events[user_id] = test.test()
        else:
            return 0
    # Описание ивента
  #  return events[user_id].description + "\n\nХарактеристики врага:\n" + repr(enemys[user_id])