import random

from enemys import *
from constants import *
from enemys.enemy import *


def bot_fight(user, msg):
    if user.enemy.escape():  # если враг сбежал
        bot.send_message(user.id, user.enemy.name + " сбежал, ну не знаю мог бы его и догнать, "
                                                    "но раз тебе лень то ладно")
        user.enemy = None
        return True
    else:
        is_crit = ""
        dmg_to_enemy = 0
        if msg == TO_DAMAGE:  # если игрок ударил без оружия
            if user.crit >= random.randint(1, 100):  # если критический
                dmg_to_enemy = user.enemy.take_damage(user.to_damage(False, None) * 2)
                is_crit = "критические "
            else:
                dmg_to_enemy = user.enemy.take_damage(user.to_damage(False, None))
        elif msg in user.items.keys():  # если игрок использовал оружие
            dmg_to_enemy = user.enemy.take_damage(user.to_damage(True, msg))

        if user.enemy.hp > 0:  # если враг жив
            dmg_to_user = user.take_damage(user.enemy.to_damage())
            if user.hp > 0:  # если пользователь жив
                bot.send_message(user.id, "Ты нанес: {0}{1} 💥\nУ {2} осталось: {3} ❤\n\n"
                                          "{2} ударил: {4} 💥\nУ тебя осталось: {5} ❤".
                                 format(is_crit, dmg_to_enemy, user.enemy.name,
                                        user.enemy.hp, dmg_to_user, user.hp))
            else:  # Если умрет пользователь
                bot.send_message(user.id, "Ты вмэр 💀\n\nПричина смерти: {0}\n\nТвоя статистика:\n".
                                 format(user.enemy.name) + repr(user),
                                 reply_markup=types.ReplyKeyboardMarkup().add('/start'))
                bot.send_sticker(user.id, "CAACAgIAAxkBAAEEms1ibridDAOemzBFkVXyS8LUmExOVgACRxcAAvuxcEvbmQyQSCSazyQE")
                user.menu = DEATH
        else:  # если умрет враг
            enemy = user.enemy
            bot.send_message(user.id, enemy.enemy_loot(user))
            user.enemy = None

            if not (user.add_xp(enemy.xp)):  # если игрок неполучил новый уровень
                return True


def enemy_create(user):  # Генерация мобов
    enemys = [Enemy(RAT), Enemy(RAD_COCKROACH), Enemy(SLIME), Enemy(ZOMBIE), Enemy(GOBLIN), Enemy(GOLLUM), Enemy(GRASS),
              Enemy(CARAVAN)]
    # enemys = ENEMYS

    # enemys = [Rat(), RadCockroach(), Slime(), Goblin(), Zombie(), Gollum(), Grass(), Caravan()]  # легкие мобы
    if user.lvl >= 5:
        enemys += [Enemy(BANDIT), Enemy(CACODEMON), Enemy(CJ), Enemy(GORDON), Enemy(LUKASHENKO), Enemy(MASTER),
                   Enemy(NEZUKO), Enemy(ORK), Enemy(SUPER_SUS), Enemy(WEREWOLF)]
        # enemys += [Ork(), Bandit(), Werewolf(), Cacodemon(), Master(),
        #            CJ(), Nezuko(), SuperSus(), Gordon(), Lukashenko()]  # + средние мобы
    if user.lvl >= 15:
        enemys += [Enemy(DARK_NIGHT), Enemy(DIO), Enemy(AGENT_SMITH), Enemy(OROCHIMARU), Enemy(KANEKI),
                   Enemy(DAVY_JONES), Enemy(BOWSER), Enemy(DUNGEON_MASTER), Enemy(LIGHT_YAGAMI)]
        # enemys += [DarkKnight(), Dio(), AgentSmith(), Orochimaru(), Kaneki(),
        #            DavyJones(), Bowser(), DungeonMaster(), LightYagami()]  # + сложные мобы

    user.enemy = random.choice(enemys)
    # Описание моба при первой встрече
    return user.enemy
