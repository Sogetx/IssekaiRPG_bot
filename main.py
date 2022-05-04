from buttons_generator import buttons_generator
from telebot import *
from constants import *
import User
import config
import random
from Enemys.fight_system import enemy_create, bot_fight
from Events.events_sys import events_create

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
users = {}  # словарь(масив ключ-значение) пользователей


@bot.message_handler(commands=['start'])
def start(msg):  # обработчик команды /start
    # удаление моба, если игрок ввел /start в процессе боя, иначе будет продолжатся прерваный бой
    uid = msg.chat.id
    users[uid] = User.User()  # добавление пользователя в словарь при начале игры
    if users[uid].enemy is not None:
        users[uid].enemy = None
    bot.send_sticker(uid, HELLO_STICKER)  # приветственный стикер
    bot.send_message(uid, "Добро пожаловать, {0.first_name}!\n"
                          "Я - {1.first_name}, бот который будет вести тебя по вымышленому, "
                          "созданому по больной фантазии авторов, фэнтези мире".
                     format(msg.from_user, bot.get_me()), reply_markup=buttons_generator(MAIN_MENU_BUTTONS))


@bot.message_handler(commands=['help'])
def settings(message):  # обработчик команды /help
    bot.send_message(message.chat.id, 'Вот мой список команд:\n /start \n /help')


@bot.message_handler(content_types=['text'])
def bot_message(msg):  # обработчик текста
    uid = msg.chat.id
    try:  # возможна ошибка KeyError
        if users[uid].menu == GAME_MENU:
            game_menu(uid, msg.text)
        elif users[uid].menu == FIGHT_MENU:
            fight_menu(uid, msg.text)
        elif users[uid].menu == MAIN_MENU:
            main_menu(uid, msg.text)
        elif users[uid].menu == NEW_LVL:
            new_level(uid, msg.text)
        elif users[uid].menu == DEATH:  # если пользователь пишет сообщение боту, но он уже мертв
            bot.send_message(uid, 'Ты же уже мертв, куда тебе идти то?\n\n'
                                  '         --> /start <--')
            bot.send_message(uid, "⚰️")
    except KeyError:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        restart = types.KeyboardButton('/start')
        markup.add(restart)
        bot.send_message(uid, 'Произошли какие-то траблы, нужно перезапустить бота', reply_markup=markup)


def fight_menu(uid, msg):  # Все что связано с взаимодействием в бою
    user = users[uid]
    if msg == GO_AHEAD:
        bot.send_message(uid, "Ты встретил моба\n\n" + enemy_create(user),
                         reply_markup=buttons_generator(FIGHT_MENU_BUTTONS))
        user.menu = FIGHT_MENU
    elif msg == RUN:  # сбежать
        user.enemy = None
        game_menu(uid, GAME_MENU)  # переход в игровое меню
        bot.send_message(uid, 'Ты сбежал')
    elif msg == TO_DAMAGE:  # Ударить врага
        bot_fight(uid, user, game_menu, new_level)
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')


def events_menu(uid, msg):  # Все что связано с взаимодействием c ивентом
    user = users[uid]
    if msg == GO_AHEAD:
        bot.send_message(uid, "{1}\n\nРезультат: {0}".format(events_create(user), user.event.description))
        bot.send_message(uid, 'Вы пережили еще одно событие')
        game_menu(uid, GAME_MENU)
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')


def main_menu(uid, msg):
    if msg == MAIN_MENU:  # Если было выбрано главное меню
        bot.send_message(uid, "Ты вернулся в главное меню", reply_markup=buttons_generator(MAIN_MENU_BUTTONS2))
        users[uid].menu = MAIN_MENU
    elif msg == CONTINUE_GAME or msg == START_NEW_GAME:
        game_menu(uid, GAME_MENU)  # переход в игровое меню
    elif msg == SUPPORT:
        bot.send_message(uid, "@Dimasik333 - Telegram Дима\nlevstepanenko@gmail.com - Gmail Лев")
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')


def game_menu(uid, msg):  # игровое меню: статистика, магазин, пойти в бой и возврат в главное меню
    user = users[uid]
    if msg == GAME_MENU:
        bot.send_message(uid, "У тебя:\n{0}❤ {1}💵\n\nЧе дальше будеш делать?".
                         format(user.hp, user.money), reply_markup=buttons_generator(GAME_MENU_BUTTONS))
        user.menu = GAME_MENU
    elif msg == SHOP:
        # # # переход в меню магазина # # #
        bot.send_sticker(uid, SHOP_STICKER)
        bot.send_message(uid, 'Тут должен был быть магаз, но он еще в разработке, сарян')
    elif msg == GO_AHEAD:
        user.go_ahead_count += 1
        go = random.randint(1, 5)
        if go == 1:
            events_menu(uid, msg)
        else:
            fight_menu(uid, msg)
    elif msg == MAIN_MENU:
        main_menu(uid, MAIN_MENU)
    elif msg == STATISTICS:
        bot.send_message(uid, "Твоя статистика:\n" + repr(user))
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')


def new_level(uid, msg):  # получение нового уровня( условия, кнопки выбора характеристик повышение параметров героя)
    user = users[uid]

    if msg == NEW_LVL:
        bot.send_message(uid, "🎉Ты получил новый уровень🎉\n\n"
                              "Твои характеристики:\n\n"
                              "Сила: {0} 💪\nЗащита: {1} 🛡\nШанс крита: {2} 🎯\nМаксимальное ХП: {3}❤\n\n"
                              "Выбери какую хар-ку ты хочешь увеличить:".
                         format(user.power, user.defence, user.crit, user.max_hp),
                         reply_markup=buttons_generator(NEW_LVL_BUTTONS))
        user.menu = NEW_LVL
    elif msg == "Максимальное ХП ❤ +10":  # если игрок выбрал поднять макс хп на 10
        user.max_hp += 10  # увеличение макс хп на 10
    elif msg == "Сила 💪 +1":  # если выбран параметр Сила +1
        user.addpower(1)  # повышение силы на 1
    elif msg == "Защита 🛡 +1":  # если выбран параметр Защита +1
        user.defence += 1  # повышение защиты персонажа на 1
    elif msg == "Шанс крита 🎯 +1":
        user.crit += 1
    if msg != NEW_LVL:
        user.heal(user.max_hp)  # полное востановление хп игрока
        if user.next_lvl():
            bot.send_message(uid, "🎉Ты получил новый уровень🎉\n\n"
                                  "Твои характеристики:\n\n"
                                  "Сила: {0} 💪\nЗащита: {1} 🛡\nШанс крита: {2} 🎯\nМаксимальное ХП: {3}❤\n\n"
                                  "Выбери какую хар-ку ты хочешь увеличить:".
                             format(user.power, user.defence, user.crit, user.max_hp))
        else:
            game_menu(uid, GAME_MENU)  # переход в игровое меню


bot.polling()
