from telebot import *


def buttons_generator(buttons):  # генератор кнопок
    # buttons - массив кнопок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i, x, y, z = 0, 0, 1, 2
    while i < len(buttons):
        if z < len(buttons):
            markup.add(buttons[x], buttons[y], buttons[z])
            x += 3
            y += 3
            z += 3
        elif y < len(buttons):
            markup.add(buttons[x], buttons[y])
        else:
            markup.add(buttons[x])
        i += 3
    return markup
