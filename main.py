import types
from telebot import *
from constants import *
import User
import config
from fight_system import enemy_create, bot_fight

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
users = {}  # словарь(масив ключ-значение) пользователей
enemys = {}  # словарь мобов


@bot.message_handler(commands=['start'])
def start(msg):  # обработчик команды /start
    # удаление моба, если игрок ввел /start в процессе боя, иначе будет продолжатся прерваный бой
    if msg.chat.id in enemys.keys():
        enemys.pop(msg.chat.id)
    users[msg.chat.id] = User.User()  # добавление пользователя в словарь при начале игры
    bot.send_sticker(msg.chat.id, HELLO_STICKER)  # приветственный стикер
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Главное меню
    item1 = types.KeyboardButton(START_NEW_GAME)
    item2 = types.KeyboardButton(SUPPORT)  # написать разрабам(виведется почта и телеграм)
    markup.add(item1, item2)
    bot.send_message(msg.chat.id, "Добро пожаловать, {0.first_name}!\n"
                                  "Я - {1.first_name}, бот который будет вести тебя по вымышленому, "
                                  "созданому по больной фантазии авторов, фэнтези мире".
                     format(msg.from_user, bot.get_me()), reply_markup=markup)


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
        elif users[uid].menu == DEATH:
            bot.send_message(uid, 'Ты же уже мертв, куда тебе идти то?\n\nЕсли непонял - то нажми сюда --> /start <--')

    except KeyError:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        restart = types.KeyboardButton('/start')
        markup.add(restart)
        bot.send_message(uid, 'Произошли какие-то траблы, нужно перезапустить бота', reply_markup=markup)


def fight_menu(uid, msg):
    if msg == GO_AHEAD:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        run = types.KeyboardButton(RUN)
        to_damage = types.KeyboardButton(TO_DAMAGE)
        markup.add(run, to_damage)
        bot.send_message(uid, "Ты встретил моба\n\n" + enemy_create(uid, enemys), reply_markup=markup)
        users[uid].menu = FIGHT_MENU
    elif msg == RUN:  # сбежать
        enemys.pop(uid)
        game_menu(uid, GAME_MENU)  # переход в игровое меню
        bot.send_message(uid, 'Ты сбежал')
    elif msg == TO_DAMAGE:  # Ударить врага
        bot_fight(uid, users[uid], enemys, bot, game_menu)
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')


def main_menu(uid, msg):
    if msg == MAIN_MENU:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(CONTINUE_GAME)  # продолжить игру
        item2 = types.KeyboardButton(SUPPORT)  # написать разрабам(виведется телеграм и почта)
        markup.add(item1, item2)
        bot.send_message(uid, "Ты вернулся в главное меню", reply_markup=markup)
        users[uid].menu = MAIN_MENU
    elif msg == START_NEW_GAME or msg == CONTINUE_GAME:
        game_menu(uid, GAME_MENU)   # переход в игровое меню
    elif msg == SUPPORT:
        bot.send_message(uid, "@Dimasik333 - Telegram Дима\nlevstepanenko@gmail.com - Gmail Лев")
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')


def game_menu(uid, msg):
    if msg == GAME_MENU:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton(SHOP)
        item6 = types.KeyboardButton(GO_AHEAD)
        back = types.KeyboardButton(MAIN_MENU)
        statistics = types.KeyboardButton(STATISTICS)
        markup.add(item5, item6, statistics, back)
        bot.send_message(uid, "{0}❤ {1}💵".format(users[uid].hp, users[uid].money), reply_markup=markup)
        users[uid].menu = GAME_MENU
    elif msg == SHOP:
        # # # переход в меню магазина # # #
        bot.send_sticker(uid, SHOP_STICKER)
        bot.send_message(uid, 'Тут должен был быть магаз, но он еще в разработке, сарян')
    elif msg == GO_AHEAD:
        fight_menu(uid, msg)
    elif msg == MAIN_MENU:
        main_menu(uid, MAIN_MENU)
    elif msg == STATISTICS:
        bot.send_message(uid, "Твоя статистика:\n" + repr(users[uid]))
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')


bot.polling()
