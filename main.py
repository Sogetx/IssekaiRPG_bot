from buttons_generator import buttons_generator
from constants import *
from User import User
import random
from Enemys.fight_system import enemy_create, bot_fight
from Events import *

users = {}  # словарь(масив ключ-значение) пользователей


@bot.message_handler(commands=['start'])
def start(msg):  # обработчик команды /start
    users[msg.chat.id] = User(msg.chat.id)  # добавление пользователя в словарь при начале игры
    user = users[msg.chat.id]
    # удаление моба, если игрок ввел /start в процессе боя, иначе будет продолжатся прерваный бой
    if user.enemy is not None:
        user.enemy = None
    bot.send_sticker(user.id, "CAACAgIAAxkBAAEEmbFibmcM88jMUQhItJWitmTQeBjFdgACSRYAAsOLeEs1cJYvU2PfdyQE")  # приветственный стикер
    bot.send_message(user.id, "Добро пожаловать, {0.first_name}!\n"
                              "Я - {1.first_name}, бот который будет вести тебя по вымышленому, "
                              "созданому по больной фантазии авторов, фэнтези мире".
                     format(msg.from_user, bot.get_me()), reply_markup=buttons_generator([START_NEW_GAME, SUPPORT]))


@bot.message_handler(commands=['help'])
def settings(msg):  # обработчик команды /help
    bot.send_message(msg.chat.id, 'Вот мой список команд:\n /start \n /help')


@bot.message_handler(content_types=['text'])
def bot_message(msg):  # обработчик текста
    try:  # возможна ошибка KeyError
        user = users[msg.chat.id]
        if user.menu == GAME_MENU:
            game_menu(user, msg.text)
        elif user.menu == FIGHT_MENU:
            fight_menu(user, msg.text)
        elif user.menu == INVENTORY_MENU:
            inventory_menu(user, msg.text)
        elif user.menu == MAIN_MENU:
            main_menu(user, msg.text)
        elif user.menu == NEW_LVL:
            new_level(user, msg.text)
        elif user.menu == SHOP_MENU:
            shop_menu(user, msg.text)
        elif user.menu == EVENTS_MENU:
            events_menu(user, msg.text)
        elif user.menu == DEATH:  # если пользователь пишет сообщение боту, но он уже мертв
            bot.send_message(user.id, 'Ты же уже мертв, куда тебе идти то?\n\n'
                                      '         --> /start <--')
            bot.send_message(user.id, "⚰️")
    except KeyError:
        bot.send_message(msg.chat.id, 'Произошли какие-то траблы, нужно перезапустить бота',
                         reply_markup=types.ReplyKeyboardMarkup().add('/start'))


def fight_menu(user, msg):  # Все что связано с взаимодействием в бою
    if msg == GO_AHEAD:
        weapons = []
        for weapon in user.items.values():
            if weapon[0].damage != 0:
                weapons += ["", weapon[0].name, ""]
        bot.send_message(user.id, "Ты встретил моба\n\n" + enemy_create(user),
                         reply_markup=buttons_generator([RUN, TO_DAMAGE, INVENTORY] + weapons))
        bot.send_sticker(user.id, user.enemy.sticker)
        user.menu = FIGHT_MENU
    elif msg == BACK:
        weapons = []
        for weapon in user.items.values():
            if weapon[0].damage != 0:
                weapons += ["", weapon[0].name, ""]
        bot.send_message(user.id, "Ты вышел из инвентаря и продолжил бой",
                         reply_markup=buttons_generator([RUN, TO_DAMAGE, INVENTORY] + weapons))
        user.menu = FIGHT_MENU
    elif msg == RUN:  # сбежать
        user.enemy = None
        game_menu(user, GAME_MENU)  # переход в игровое меню
        bot.send_message(user.id, 'Ты сбежал')
    elif msg == TO_DAMAGE or msg in user.items.keys():  # Ударить врага
        bot_fight(user, game_menu, new_level, msg)
    elif msg == INVENTORY:
        inventory_menu(user, msg)
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def events_menu(user, msg):  # Все что связано с взаимодействием c ивентом
    if msg == GO_AHEAD:
        user.event = random.choice([Tavern(), Church(), Anisimov(), Odd_Even(), Dobby()])
        if not user.event.is_active:
            bot.send_message(user.id, "{1}\n\nРезультат: {0}".format(user.event.action(user), user.event.description))
            game_menu(user, GAME_MENU)
        else:
            bot.send_message(user.id, "{0}".format(user.event.description),
                             reply_markup=buttons_generator(user.event.buttons + [BACK]))
            user.menu = EVENTS_MENU
    if msg == BACK:
        game_menu(user, GAME_MENU)
    elif not (msg == GO_AHEAD):
        if user.event.name == "Анисимов" and user.event.answer(user, msg):
            game_menu(user, GAME_MENU)
        elif user.event.name == "Четное-Нечетное" and user.event.choice(user, msg):
            game_menu(user, GAME_MENU)
        elif user.event.name == "Добби" and user.event.give_sock(user, msg):
            game_menu(user, GAME_MENU)


def main_menu(user, msg):
    if msg == MAIN_MENU:  # Если было выбрано главное меню
        bot.send_message(user.id, "Ты вернулся в главное меню", reply_markup=buttons_generator([CONTINUE_GAME, SUPPORT]))
        user.menu = MAIN_MENU
    elif msg == CONTINUE_GAME or msg == START_NEW_GAME:
        game_menu(user, GAME_MENU)  # переход в игровое меню
    elif msg == SUPPORT:
        bot.send_message(user.id, "@Dimasik333 - Telegram Дима\nlevstepanenko@gmail.com - Gmail Лев")
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def game_menu(user, msg):  # игровое меню: статистика, магазин, пойти в бой и возврат в главное меню
    if msg == GAME_MENU:
        bot.send_message(user.id, "У тебя:\n{0}/{1}❤ {2}💵\n\nЧе дальше будеш делать?".
                         format(user.hp, user.max_hp, user.money),
                         reply_markup=buttons_generator([SHOP, GO_AHEAD, INVENTORY, STATISTICS, MAIN_MENU]))
        user.menu = GAME_MENU
    elif msg == SHOP:
        shop_menu(user, msg)
        bot.send_sticker(user.id, "CAACAgIAAxkBAAEEmbNibmeymHwNw_LwnwmbL7sC4ifSoAACYRYAApUBeUsatN_ZdOmq6CQE")
    elif msg == GO_AHEAD:
        user.go_ahead_count += 1
        if random.randint(1, 5) == 1:
            events_menu(user, msg)
        else:
            fight_menu(user, msg)
    elif msg == MAIN_MENU:
        main_menu(user, msg)
    elif msg == INVENTORY:
        inventory_menu(user, msg)
    elif msg == STATISTICS:
        bot.send_message(user.id, "Твоя статистика:\n" + repr(user))
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def new_level(user, msg):  # получение нового уровня( условия, кнопки выбора характеристик повышение параметров героя)
    if msg == NEW_LVL:
        bot.send_message(user.id, "🎉Ты получил новый уровень🎉\n\n"
                                  "Твои характеристики:\n\n"
                                  "Сила: {0} 💪\nЗащита: {1} 🛡\nШанс крита: {2} 🎯\nМаксимальное ХП: {3}❤\n\n"
                                  "Выбери какую хар-ку ты хочешь увеличить:".
                         format(user.power, user.defence, user.crit, user.max_hp),
                         reply_markup=buttons_generator([ADD_POWER, ADD_DEFENCE, ADD_CRIT, ADD_HP]))
        user.menu = NEW_LVL
    elif msg == ADD_HP:  # если игрок выбрал поднять макс хп на 10
        user.max_hp += 10  # увеличение макс хп на 10
    elif msg == ADD_POWER:  # если выбран параметр Сила +2
        user.addpower(2)  # повышение силы на 2
    elif msg == ADD_DEFENCE:  # если выбран параметр Защита +2
        user.defence += 2  # повышение защиты персонажа на 2
    elif msg == ADD_CRIT:
        user.crit += 1
    if msg != NEW_LVL:
        user.heal(user.max_hp)  # полное востановление хп игрока
        if user.add_xp(0):
            bot.send_message(user.id, "🎉Ты получил новый уровень🎉\n\n"
                                      "Твои характеристики:\n\n"
                                      "Сила: {0} 💪\nЗащита: {1} 🛡\nШанс крита: {2} 🎯\nМаксимальное ХП: {3}❤\n\n"
                                      "Выбери какую хар-ку ты хочешь увеличить:".
                             format(user.power, user.defence, user.crit, user.max_hp))
        else:
            game_menu(user, GAME_MENU)  # переход в игровое меню


def inventory_menu(user, msg):
    if msg == INVENTORY:
        buttons = []
        a = 1  # счетчик предметов
        message = "У тебя в инвентаре есть:\n\n"
        if len(user.items) == 0:
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
                    message += "{0} ({1} общей ценой {2} 💵) :\n{3}\n\n".\
                        format(i.name, user.items[i.name][1], user.items[i.name][1] * i.price, i.description)
                a += 1
        if len(user.items) % 5 != 0 and len(user.items) > (user.inv_page * 5):
            buttons += [NEXT_PAGE, "", ""]
        if user.inv_page > 1:
            buttons += [BACK_PAGE, "", ""]
        buttons += [BACK, "", ""]
        bot.send_message(user.id, message, reply_markup=buttons_generator(buttons))
        user.menu = INVENTORY_MENU
    elif msg.startswith("💵 Продать"):
        item = ""
        i = 0
        for itm in (msg.split()):
            if 2 <= i < len(msg.split()) - 1:  # для предметов, у которых названия из разного кол-ва слов
                item += itm + " "
            elif i >= 2:
                item += itm
            i += 1
        bot.send_message(user.id, user.items[item][0].sell(user))
        if len(user.items) % 5 == 0 and len(user.items) != 0:
            user.inv_page -= 1
        inventory_menu(user, INVENTORY)
    elif msg in user.items.keys():
        bot.send_message(user.id, user.items[msg][0].use(user))
        if len(user.items) % 5 == 0 and len(user.items) != 0:
            user.inv_page -= 1
        inventory_menu(user, INVENTORY)
    elif msg == NEXT_PAGE:
        user.inv_page += 1
        inventory_menu(user, INVENTORY)
    elif msg == BACK_PAGE:
        user.inv_page -= 1
        inventory_menu(user, INVENTORY)
    elif msg == BACK:
        user.inv_page = 1
        if user.enemy is not None:
            fight_menu(user, msg)
        else:
            game_menu(user, GAME_MENU)
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def shop_menu(user, msg):
    if msg == SHOP:
        shopitems = []
        buttons = [""]
        message = ""
        i = 0
        while i <= 3:
            val = random.choice(list(SHOP_ITEMS))
            if val not in shopitems:
                shopitems.append(SHOP_ITEMS[val].name)
                buttons += [SHOP_ITEMS[val].name]
                message += SHOP_ITEMS[val].shop()
                i += 1
        bot.send_message(user.id, "Лампы, верёвки, бомбы! Тебе всё это нужно? Оно твоё, мой друг… если у тебя "
                                  "достаточно рупий!?\n"
                                  "У тебя есть {0} 💵\n\n".
                         format(user.money) + message, reply_markup=buttons_generator(buttons + ["", BACK]))
        user.menu = SHOP_MENU
    elif msg in SHOP_ITEMS.keys():
        bot.send_message(user.id, SHOP_ITEMS[msg].buy(user))
    elif msg == BACK:
        game_menu(user, GAME_MENU)
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


bot.polling()
