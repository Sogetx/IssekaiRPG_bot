import random
import config
from buttons_generator import *
from Enemys import *
from constants import *

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)


def bot_fight(uid, user, menu, newlvl):
    if user.enemy.hp < user.enemy.max_hp // 10 and user.enemy.run_att == 0:  # условие для побега моба
        val = random.randint(1, 30)
        user.enemy.run_att = 1
        if val == 1:
            bot.send_message(uid, user.enemy.name + " сбежал, ну не знаю мог бы его и догнать, "
                                                    "но раз тебе лень то ладно")
            user.enemy = None
            menu(uid, GAME_MENU)
    else:
        is_crit = ""
        # получение мобом урона от пользователя
        if user.crit >= random.randint(1, 100):  # если критический
            dmg_to_enemy = user.enemy.take_damage(user.to_damage() * 2)
            is_crit = "Критические "
        else:
            dmg_to_enemy = user.enemy.take_damage(user.to_damage())

        if user.enemy.hp > 0:  # если враг жив
            dmg_to_user = user.take_damage(user.enemy.to_damage())
            if user.hp > 0:  # если пользователь жив
                bot.send_message(uid, "Ты нанес: " + is_crit + str(dmg_to_enemy) +
                                 " 💥\nУ врага осталось:" + str(user.enemy.hp) +
                                 " ❤\n\nВраг ударил: " + str(dmg_to_user) +
                                 " 💥\nУ тебя осталось:" + str(user.hp) + " ❤")
            else:  # Если умрет пользователь
                bot.send_message(uid, user.death_msg(user.enemy.name), reply_markup=buttons_generator(['/start']))
                bot.send_sticker(uid, DEATH_STICKER)
                user.menu = DEATH
        else:  # если умрет враг
            user.money += user.enemy.money  # получение денег с моба
            bot.send_message(uid, user.enemy.death + "\n\n" +
                             "За победу над врагом ты получил {0}⭐ и {1}💵".format(user.enemy.xp, user.enemy.money))
            user.enemy_count += 1  # счетчик мобов
            user.xp += user.enemy.xp  # получение хр от моба
            user.enemy = None
            if user.next_lvl():  # проверка условия достиг ли игрок нового уровня
                newlvl(uid, NEW_LVL)  # выдача нового уровня
            else:
                menu(uid, GAME_MENU)  # показывается игровое меню


def enemy_create(user):  # Генерация мобов
    if user.enemy is None:  # если игрок не дерется с мобом
        enm = random.randint(1, 4)  # генерируем определенного моба на условии того какое число выпадет
        if enm == 1:
            user.enemy = RadCockroach.RadCockroach()
        elif enm == 2:
            user.enemy = Rat.Rat()
        elif enm == 3:
            user.enemy = Slime.Slime()
        elif enm == 4:
            user.enemy = Goblin.Goblin()
    # Описание моба при первой встерече
    return "{0}\n\n{1}\n\nХарактеристики врага:\n{2}".format(user.enemy.name, user.enemy.description, repr(user.enemy))
