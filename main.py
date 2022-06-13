from buttons_generator import buttons_generator
from constants import *
from user import User
import random
from enemys.fight_system import enemy_create, bot_fight
from events import *

users = {}  # словарь(масив ключ-значение) пользователей в виде {id: User()}


@bot.message_handler(commands=['start'])
def start(msg):  # обработчик команды /start
    users[msg.chat.id] = User(msg.chat.id)  # добавление пользователя в словарь при начале игры
    user = users[msg.chat.id]
    # приветственный стикер
    bot.send_sticker(user.id, "CAACAgIAAxkBAAEEmbFibmcM88jMUQhItJWitmTQeBjFdgACSRYAAsOLeEs1cJYvU2PfdyQE")
    bot.send_message(user.id, "Добро пожаловать, {0.first_name}!\n"
                              "Я - {1.first_name}, бот который будет вести тебя по вымышленому, "
                              "созданому по больной фантазии авторов, мире".
                     format(msg.from_user, bot.get_me()),
                     reply_markup=buttons_generator([START_NEW_GAME, SUPPORT], True))


@bot.message_handler(commands=['help'])
def settings(msg):  # обработчик команды /help
    bot.send_message(msg.chat.id, 'Вот мой список команд:\n /start \n /help')


@bot.message_handler(content_types=['text'])
def bot_message(msg):  # обработчик текста
    try:  # возможна ошибка KeyError
        user = users[msg.chat.id]
        if user.menu == GAME_MENU:  # игровое меню
            game_menu(user, msg.text)
        elif user.menu == FIGHT_MENU:  # меню боя
            fight_menu(user, msg.text)
        elif user.menu == INVENTORY_MENU:  # инвентарь
            inventory_menu(user, msg.text)
        elif user.menu == MAIN_MENU:  # главное меню
            main_menu(user, msg.text)
        elif user.menu == NEW_LVL:  # меню нового уровня
            new_level(user, msg.text)
        elif user.menu == SHOP_MENU:  # магазин
            shop_menu(user, msg.text)
        elif user.menu == EVENTS_MENU:  # меню ивента(если он активный)
            events_menu(user, msg.text)
        elif user.menu == DEATH:  # если пользователь пишет сообщение боту, но он уже мертв
            bot.send_message(user.id, 'Ты же уже мертв, куда тебе идти то?\n\n'
                                      '         --> /start <--')
            bot.send_message(user.id, "⚰️")
    except KeyError: # если пользователя нету в словаре пользователей
        bot.send_message(msg.chat.id, 'Произошли какие-то траблы, нужно перезапустить бота',
                         reply_markup=types.ReplyKeyboardMarkup().add('/start'))


def fight_menu(user, msg):  # Все что связано с взаимодействием в бою
    if msg == GO_AHEAD or msg == BACK:  # если игрок пошел вперед (в бой) или вернулся из инвентаря(во время боя)
        weapons = []  # масив для кнопок оружия во время боя(если у игрока есть оружие в инвентаре)
        for weapon in user.items.values():
            if weapon[0].damage != 0:
                weapons += ["", weapon[0].name, ""]
        if msg == GO_AHEAD:
            enemy = enemy_create(user)
            bot.send_message(user.id, "Ты встретил моба\n\n{0}\n\n{1}\n\nХарактеристики врага:\n{2}".
                             format(enemy.name, enemy.description, repr(enemy)),
                             reply_markup=buttons_generator([RUN, TO_DAMAGE, INVENTORY] + weapons, False))
            bot.send_sticker(user.id, enemy.sticker)
        elif msg == BACK:
            bot.send_message(user.id, "Ты вышел из инвентаря и продолжил бой",
                             reply_markup=buttons_generator([RUN, TO_DAMAGE, INVENTORY] + weapons, False))
        user.menu = FIGHT_MENU
    elif msg == RUN:  # сбежать
        user.enemy = None
        bot.send_message(user.id, 'Ты сбежал')
        game_menu(user, GAME_MENU)  # переход в игровое меню
    elif msg == TO_DAMAGE or msg in user.items.keys():  # Ударить врага
        bot_fight(user, game_menu, msg)
    elif msg == INVENTORY:
        inventory_menu(user, msg)
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def events_menu(user, msg):  # Все что связано с взаимодействием c ивентом
    if msg == GO_AHEAD:
        user.event = random.choice([Tavern(), Church(), Anisimov(), OddEven(), Dobby()])
        if not user.event.is_active:
            bot.send_message(user.id, "{1}\n\nРезультат: {0}".format(user.event.action(user), user.event.description))
            game_menu(user, GAME_MENU)
        else:
            bot.send_message(user.id, "{0}\n\n{1}".format(user.event.name, user.event.description),
                             reply_markup=buttons_generator(user.event.buttons + [BACK], True))
            user.menu = EVENTS_MENU
    elif msg == BACK:
        user.event = None
        game_menu(user, GAME_MENU)
    elif msg in user.event.buttons:
        user.event.active_action(user, msg)  # активный ивент
        user.event = None
        game_menu(user, GAME_MENU)
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def main_menu(user, msg):
    if msg == MAIN_MENU:  # Если было выбрано главное меню
        bot.send_message(user.id, "Ты вернулся в главное меню",
                         reply_markup=buttons_generator([CONTINUE_GAME, SUPPORT], True))
        user.menu = MAIN_MENU
    elif msg == CONTINUE_GAME or msg == START_NEW_GAME:
        game_menu(user, GAME_MENU)  # переход в игровое меню
    elif msg == SUPPORT:
        bot.send_message(user.id, "@Dimasik333 - Telegram Дима\nlevstepanenko@gmail.com - Gmail Лев",
                         reply_markup=buttons_generator([CONTINUE_GAME, SUPPORT], True))
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def game_menu(user, msg):  # игровое меню: статистика, магазин, пойти в бой и возврат в главное меню
    if msg == GAME_MENU:
        bot.send_message(user.id, "У тебя:\n{0}/{1}❤ {2}💵\n\nЧе дальше будеш делать?".
                         format(user.hp, user.max_hp, user.money),
                         reply_markup=buttons_generator([SHOP, GO_AHEAD, INVENTORY, STATISTICS, MAIN_MENU], True))
        user.menu = GAME_MENU
    elif msg == SHOP:
        shop_menu(user, msg)
    elif msg == GO_AHEAD:
        user.go_ahead_count += 1  # кол-во походов игрока +1
        if random.randint(1, 5) == 1:  # шанс 1 к 5 что будет ивент(не бой с мобом)
            events_menu(user, msg)
        else:
            fight_menu(user, msg)
    elif msg == MAIN_MENU:
        main_menu(user, msg)
    elif msg == INVENTORY:
        inventory_menu(user, msg)
    elif msg == STATISTICS:
        bot.send_message(user.id, "Твоя статистика:\n" + repr(user),
                         reply_markup=buttons_generator([SHOP, GO_AHEAD, INVENTORY, STATISTICS, MAIN_MENU], True))
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def new_level(user, msg):  # получение нового уровня( условия, кнопки выбора характеристик повышение параметров героя)
    if msg == ADD_HP:  # если игрок выбрал поднять макс хп на 10
        user.max_hp += 10
    elif msg == ADD_POWER:  # если выбран параметр Сила +2
        user.power += 2
    elif msg == ADD_DEFENCE:  # если выбран параметр Защита +2
        user.defence += 2
    elif msg == ADD_CRIT:  # если выбран параметр Шанс Крита +1
        user.crit += 1
    user.heal(user.max_hp)  # полный отхил за новый уровень
    if not (user.add_xp(0)):  # если игрок не получил сразу несколько уровней
        game_menu(user, GAME_MENU)


def inventory_menu(user, msg):
    if msg == INVENTORY:
        buttons = []
        a = 1  # счетчик предметов
        message = "У тебя в инвентаре есть:\n\n"
        if len(user.items) == 0:  # если у игрока нет предметов в инвентаре
            message += "Пусто 😐"
        else:
            for i in user.items.values():
                i = i[0]
                if ((user.inv_page - 1) * 5) + 1 <= a <= user.inv_page * 5:  # 1  страничка, 2, 3 и тд. по 5 предметов
                    if i.is_used and i.damage == 0:
                        buttons += [i.name]
                    else:
                        buttons += [""]
                    buttons += ["💵 Продать " + i.name, ""]
                    message += "{0} ({1} общей ценой {2} 💵) :\n{3}\n\n". \
                        format(i.name, user.items[i.name][1], user.items[i.name][1] * i.price, i.description)
                a += 1
        # если у игрока больше предметов чем (страничка * 5)
        if len(user.items) % 5 != 0 and len(user.items) > (user.inv_page * 5):
            buttons += [NEXT_PAGE, "", ""]
        if user.inv_page > 1:  # если игрок не на 1 страничке
            buttons += [BACK_PAGE, "", ""]
        bot.send_message(user.id, message, reply_markup=buttons_generator(buttons + [BACK, "", ""], False))
        user.menu = INVENTORY_MENU
    elif msg.startswith("💵 Продать"):
        bot.send_message(user.id, user.items[msg[10:]][0].sell(user))
        # если уменьшилось кол-во предметов в инвентаре, то проверка нужно ли вернутся на 1 страничку инвентаря назад
        if len(user.items) % 5 == 0 and len(user.items) != 0:
            user.inv_page -= 1
        inventory_menu(user, INVENTORY)
    elif msg in user.items.keys():
        bot.send_message(user.id, user.items[msg][0].use(user))
        # если уменьшилось кол-во предметов в инвентаре, то проверка нужно ли вернутся на 1 страничку инвентаря назад
        if len(user.items) % 5 == 0 and len(user.items) != 0:
            user.inv_page -= 1
        inventory_menu(user, INVENTORY)
    elif msg == NEXT_PAGE:  # переход на след. страничку инвентаря
        user.inv_page += 1
        inventory_menu(user, INVENTORY)
    elif msg == BACK_PAGE:  # переход на предидущую страничку инвентаря
        user.inv_page -= 1
        inventory_menu(user, INVENTORY)
    elif msg == BACK:  # выход из инвентаря
        user.inv_page = 1
        if user.enemy is not None:  # если игрок был в инвентаре во время боя
            fight_menu(user, msg)
        else:
            game_menu(user, GAME_MENU)
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def shop_menu(user, msg):
    if msg == SHOP:
        buttons = []
        message = "Лампы, верёвки, бомбы! Тебе всё это нужно? Оно твоё, мой друг… если у тебя достаточно рупий!?\n\n"
        while len(buttons) < 4:
            val = random.choice(list(SHOP_ITEMS.keys()))
            if val not in buttons:
                buttons.append(val)
                message += repr(SHOP_ITEMS[val]) + "\n\n"
        bot.send_message(user.id, message + "У тебя на счету {0} 💵".format(user.money),
                         reply_markup=buttons_generator([""] + buttons + ["", BACK], False))
        bot.send_sticker(user.id, "CAACAgIAAxkBAAEEmbNibmeymHwNw_LwnwmbL7sC4ifSoAACYRYAApUBeUsatN_ZdOmq6CQE")
        user.menu = SHOP_MENU
    elif msg in SHOP_ITEMS.keys():
        bot.send_message(user.id, SHOP_ITEMS[msg].buy(user))
    elif msg == BACK:
        game_menu(user, GAME_MENU)
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


bot.polling()
