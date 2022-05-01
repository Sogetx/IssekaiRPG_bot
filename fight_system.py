import types
import random
from Enemys import *
from constants import *
from telebot import *


def bot_fight(user_id, user, enemys, bot, menu):
    if user_id not in enemys.keys():  # создание нового моба, если бот крашнулся посреди боя
        enemy_create(user_id, enemys)
    enemy = enemys[user_id]

    user.take_damage(enemy.to_damage())
    enemy.take_damage(user.to_damage())

    if user.hp > 0:     # Пока моб и пользователь жив
        if enemy.hp > 0:
            bot.send_message(user_id, "У врага осталось: " + repr(enemy) + "\n\n\nУ тебя осталось: " + repr(user))
        else: # Смерть моба
            user_reward = enemy.reward()
            user.money += user_reward
            bot.send_message(user_id, enemy.death + "\n\n" + "ты получил {0}💵".format(user_reward))
            enemys.pop(user_id)
            menu(user_id)
    else: # Если умрет пользователь
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        restart = types.KeyboardButton('/start')
        markup.add(restart)
        bot.send_message(user_id, user.death(), reply_markup=markup)
        bot.send_sticker(user_id, DEATH_STICKER)


def enemy_create(user_id, enemys):  # Генерация мобов
    if user_id not in enemys.keys():
        enm = random.randint(1, 2)
        if enm == 1:
            enemys[user_id] = GiantCockroach.GiantCockroach()
        elif enm == 2:
            enemys[user_id] = Rat.Rat()
    return enemys[user_id].description + "\n\nХарактеристики врага:\n" + repr(enemys[user_id]) # Описание моба при первой встерече
