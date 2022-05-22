import random
from Enemys import *
from constants import *


def bot_fight(user, menu, newlvl, msg):
    if user.enemy.hp < user.enemy.max_hp // 10 and user.enemy.run_att == 0:  # условие для побега моба
        val = random.randint(1, 30)
        user.enemy.run_att = 1
        if val == 1:
            bot.send_message(user.id, user.enemy.name + " сбежал, ну не знаю мог бы его и догнать, "
                                                        "но раз тебе лень то ладно")
            user.enemy = None
            menu(user.id, GAME_MENU)
    elif msg in user.items.keys():  # если игрок использовал оружие
        dmg_to_enemy = user.enemy.take_damage(user.to_damage(True, msg))
        if user.enemy.hp > 0:  # если враг жив
            dmg_to_user = user.take_damage(user.enemy.to_damage())
            if user.hp > 0:  # если пользователь жив
                bot.send_message(user.id, "Используя " + user.items[msg].name + " ты нанес: " + str(dmg_to_enemy) +
                                 " 💥\nУ врага осталось:" + str(user.enemy.hp) +
                                 " ❤\n\nВраг ударил: " + str(dmg_to_user) +
                                 " 💥\nУ тебя осталось:" + str(user.hp) + " ❤")
            else:  # Если умрет пользователь
                bot.send_message(user.id, user.death_msg(), reply_markup=types.ReplyKeyboardMarkup().add('/start'))
                bot.send_sticker(user.id, DEATH_STICKER)
                user.menu = DEATH
        else:  # если умрет враг
            bot.send_message(user.id, user.enemy.enemy_loot(user))
            if user.add_xp(user.enemy.xp):  # проверка условия достиг ли игрок нового уровня
                user.enemy = None
                newlvl(user, NEW_LVL)  # выдача нового уровня
            else:
                user.enemy = None
                menu(user, GAME_MENU)  # показывается игровое меню
    elif msg == TO_DAMAGE:  # если игрок ударил без оружия
        is_crit = ""
        # получение мобом урона от пользователя
        if user.crit >= random.randint(1, 100):  # если критический
            dmg_to_enemy = user.enemy.take_damage(user.to_damage(False, None) * 2)
            is_crit = "критические "
        else:
            dmg_to_enemy = user.enemy.take_damage(user.to_damage(False, None))
        if user.enemy.hp > 0:  # если враг жив
            dmg_to_user = user.take_damage(user.enemy.to_damage())
            if user.hp > 0:  # если пользователь жив
                bot.send_message(user.id, "Ты нанес: " + is_crit + str(dmg_to_enemy) +
                                 " 💥\nУ врага осталось:" + str(user.enemy.hp) +
                                 " ❤\n\nВраг ударил: " + str(dmg_to_user) +
                                 " 💥\nУ тебя осталось:" + str(user.hp) + " ❤")
            else:  # Если умрет пользователь
                bot.send_message(user.id, user.death_msg(), reply_markup=types.ReplyKeyboardMarkup().add('/start'))
                bot.send_sticker(user.id, DEATH_STICKER)
                user.menu = DEATH
        else:  # если умрет враг
            bot.send_message(user.id, user.enemy.enemy_loot(user))
            if user.add_xp(user.enemy.xp):  # проверка условия достиг ли игрок нового уровня
                user.enemy = None
                newlvl(user, NEW_LVL)  # выдача нового уровня
            else:
                user.enemy = None
                menu(user, GAME_MENU)  # показывается игровое меню
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def enemy_create(user):  # Генерация мобов
    if user.enemy is None:  # если игрок не дерется с мобом
        enemys = [Rat(), RadCockroach(), Slime(), Goblin(), Zombie()]
        # if user.lvl >= 5:
        #     enemys += []  # + средние мобы
        # if user.lvl >= 10:
        #     enemys += []  # + сложные мобы
        user.enemy = random.choice(enemys)
    # Описание моба при первой встерече
        return "{0}\n\n{1}\n\nХарактеристики врага:\n{2}".format(user.enemy.name, user.enemy.description, repr(user.enemy))
