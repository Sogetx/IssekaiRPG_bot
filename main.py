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
        if msg.text == START_NEW_GAME or msg.text == CONTINUE_GAME:
            game_menu(uid)
        elif msg.text == RUN:
            enemys.pop(uid)
            game_menu(uid)
            bot.send_message(uid, 'Ты сбежал')
        elif msg.text == SHOP:
            bot.send_sticker(uid, SHOP_STICKER)
            bot.send_message(uid, 'Тут должен был быть магаз, но он еще в разработке, сарян')
        elif msg.text == GO_AHEAD:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            run = types.KeyboardButton(RUN)
            to_damage = types.KeyboardButton(TO_DAMAGE)
            markup.add(run, to_damage)
            bot.send_message(uid, "Ты встретил моба\n\n" + enemy_create(uid, enemys), reply_markup=markup)
        elif msg.text == MAIN_MENU:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton(CONTINUE_GAME)  # продолжить игру
            item2 = types.KeyboardButton(SUPPORT)  # написать разрабам(виведется телеграм и почта)
            markup.add(item1, item2)
            bot.send_message(uid, "Ты вернулся в главное меню", reply_markup=markup)
        elif msg.text == SUPPORT:
            bot.send_message(uid, "@Dimasik333 - Telegram Дима\nlevstepanenko@gmail.com - Gmail Лев")
        elif msg.text == TO_DAMAGE:  # Урон
            bot_fight(uid, users[uid], enemys, bot, game_menu)
        elif msg.text == STATISTICS:
            bot.send_message(uid, "Твоя статистика:\n" + repr(users[uid]))
        else:
            bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')
    except KeyError:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        restart = types.KeyboardButton('/start')
        markup.add(restart)
        bot.send_message(uid, 'Произошли какие-то траблы, нужно перезапустить бота', reply_markup=markup)


def game_menu(msg_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item5 = types.KeyboardButton(SHOP)
    item6 = types.KeyboardButton(GO_AHEAD)
    back = types.KeyboardButton(MAIN_MENU)
    statistics = types.KeyboardButton(STATISTICS)
    markup.add(item5, item6, statistics, back)
    bot.send_message(msg_id, "{0}❤ {1}💵".format(users[msg_id].hp, users[msg_id].money), reply_markup=markup)


bot.polling()
