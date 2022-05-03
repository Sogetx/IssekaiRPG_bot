import types
import random
from Enemys import *
from constants import *
from telebot import *


def bot_fight(user_id, user, enemys, bot, menu):
    if user_id not in enemys.keys():  # создание нового моба, если бот крашнулся посреди боя
        enemy_create(user_id, enemys)
        user.enemy_met_count += 1
    enemy = enemys[user_id]
    dmg_to_enemy = enemy.take_damage(user.to_damage())
    if enemy.hp > 0:  # если враг жив
        dmg_to_user = user.take_damage(enemy.to_damage()) - user.defence//2
        if user.hp > 0:  # если пользователь жив
            bot.send_message(user_id, "Ты нанес: " + str(dmg_to_enemy) +
                             " 💥\nУ врага осталось:" + str(enemy.hp) +
                             " ❤\n\nВраг ударил: " + str(dmg_to_user) +
                             " 💥\nУ тебя осталось:" + str(user.hp) + " ❤")
        else:  # Если умрет пользователь
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            restart = types.KeyboardButton('/start')
            markup.add(restart)
            bot.send_message(user_id, user.death_msg(), reply_markup=markup)
            bot.send_sticker(user_id, DEATH_STICKER)
            user.menu = DEATH
    else:  # если умрет враг
        user_reward_money = enemy.reward_money()
        if user_reward_money > 0:
            user.money += user_reward_money
            bot.send_message(user_id, enemy.death + "\n\n" + "У врага ты нашел {0}💵".format(user_reward_money))
        else:
            bot.send_message(user_id, enemy.death + "\n\n" + "У врага ты ничего не нашел")
        user.enemy_count += 1
        enemys.pop(user_id)
        menu(user_id, GAME_MENU)  # показывается игровое меню


def enemy_create(user_id, enemys):  # Генерация мобов
    if user_id not in enemys.keys():
        enm = random.randint(1, 2)
        if enm == 1:
            enemys[user_id] = GiantCockroach.GiantCockroach()
        elif enm == 2:
            enemys[user_id] = Rat.Rat()
    # Описание моба при первой встерече
    return enemys[user_id].description + "\n\nХарактеристики врага:\n" + repr(enemys[user_id])

