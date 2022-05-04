import types
from telebot import *
from constants import *
import User
import config
import random
from fight_system import enemy_create, bot_fight
from events_sys import events_create

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
users = {}  # словарь(масив ключ-значение) пользователей
enemys = {}  # словарь мобов
events = {}

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
    if msg == GO_AHEAD:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        run = types.KeyboardButton(RUN)
        to_damage = types.KeyboardButton(TO_DAMAGE)
        markup.add(run, to_damage)
        bot.send_message(uid, "Ты встретил моба\n\n" + enemy_create(uid, enemys), reply_markup=markup)
        users[uid].enemy_met_count += 1  # счетчик встреченых мобов будет выводиться потом в статистике
        users[uid].menu = FIGHT_MENU
    elif msg == RUN:  # сбежать
        enemys.pop(uid)
        game_menu(uid, GAME_MENU)  # переход в игровое меню
        bot.send_message(uid, 'Ты сбежал')
    elif msg == TO_DAMAGE:  # Ударить врага
        bot_fight(uid, users[uid], enemys, bot, game_menu, new_level)
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')


def events_menu(uid, msg):  # Все что связано с взаимодействием c ивентом
    if msg == GO_AHEAD:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        continue_game = types.KeyboardButton(CONTINUE_GAME)
        markup.add(continue_game)
        bot.send_message(uid, events_create(uid, events, users[uid]),
                         reply_markup=markup)
        # events_traits(users[uid], events)
        # users[uid].go_ahead_count += 1
        # users[uid].menu = FIGHT_MENU
        bot.send_message(uid, 'Вы пережили еще одно событие')
        game_menu(uid, GAME_MENU)
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')

def main_menu(uid, msg):
    if msg == MAIN_MENU:  # Если было выбрано главное меню
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(CONTINUE_GAME)  # продолжить игру
        item2 = types.KeyboardButton(SUPPORT)  # написать разрабам(виведется телеграм и почта)
        markup.add(item1, item2)
        bot.send_message(uid, "Ты вернулся в главное меню", reply_markup=markup)
        users[uid].menu = MAIN_MENU
    elif msg == START_NEW_GAME or msg == CONTINUE_GAME:
        game_menu(uid, GAME_MENU)  # переход в игровое меню
    elif msg == SUPPORT:
        bot.send_message(uid, "@Dimasik333 - Telegram Дима\nlevstepanenko@gmail.com - Gmail Лев")
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')


def game_menu(uid, msg): # игровое меню: статистика, магазин, пойти в бой и возврат в главное меню
    if msg == GAME_MENU:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton(SHOP)
        item6 = types.KeyboardButton(GO_AHEAD)
        back = types.KeyboardButton(MAIN_MENU)
        statistics = types.KeyboardButton(STATISTICS)
        markup.add(item5, item6, statistics, back)
        bot.send_message(uid, "У тебя:\n{0}❤ {1}💵\n\nЧе дальше будеш делать?".
                         format(users[uid].hp, users[uid].money), reply_markup=markup)
        users[uid].menu = GAME_MENU
    elif msg == SHOP:
        # # # переход в меню магазина # # #
        bot.send_sticker(uid, SHOP_STICKER)
        bot.send_message(uid, 'Тут должен был быть магаз, но он еще в разработке, сарян')

    elif msg == MAIN_MENU:
        main_menu(uid, MAIN_MENU)
    elif msg == STATISTICS:
        bot.send_message(uid, "Твоя статистика:\n" + repr(users[uid]))
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')


def new_level(uid, msg): # получение нового уровня( условия, кнопки выбора характеристик повышение параметров героя)
    if msg == NEW_LVL:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        hp = types.KeyboardButton("Макс. ХП ❤ +10")
        power = types.KeyboardButton("Сила 💪 +1")
        defence = types.KeyboardButton("Защита 🛡 +1")
        markup.add(hp, power, defence)
        bot.send_message(uid, "🎉Ты получил новый уровень🎉"
                              "\n\nТвои характеристики:"
                              "\n\nМаксимальное ХП: {0}❤\nСила: {1} 💪\nЗащита: {2} 🛡"
                              "\n\nВыбери какую хар-ку ты хочешь увеличить:".
                         format(users[uid].max_hp, users[uid].power, users[uid].defence), reply_markup=markup)
        users[uid].menu = NEW_LVL
    elif msg == "Макс. ХП ❤ +10":  # если игрок выбрал поднять макс хп на 10
        users[uid].max_hp += 10  # увеличение макс хп на 10
        users[uid].hp = users[uid].max_hp  # Установление параметра хп на уровень текущего максимума
        if users[uid].next_lvl():
            bot.send_message(uid, "🎉Ты получил новый уровень🎉"
                                  "\n\nТвои характеристики:"
                                  "\n\nМаксимальное ХП: {0}❤\nСила: {1} 💪\nЗащита: {2} 🛡"
                                  "\n\nВыбери какую хар-ку ты хочешь увеличить:".
                             format(users[uid].max_hp, users[uid].power, users[uid].defence))
        else:
            game_menu(uid, GAME_MENU)  # переход в игровое меню
    elif msg == "Сила 💪 +1": # если выбран параметр Сила +1
        users[uid].addpower(1) # повышение силы на 1
        users[uid].hp = users[uid].max_hp # полное востановление хп игрока 
        if users[uid].next_lvl():
            bot.send_message(uid, "🎉Ты получил новый уровень🎉"
                                  "\n\nТвои характеристики:"
                                  "\n\nМаксимальное ХП: {0}❤\nСила: {1} 💪\nЗащита: {2} 🛡"
                                  "\n\nВыбери какую хар-ку ты хочешь увеличить:".
                             format(users[uid].max_hp, users[uid].power, users[uid].defence))
        else:
            game_menu(uid, GAME_MENU)  # переход в игровое меню
    elif msg == "Защита 🛡 +1": # если выбран параметр Защита +1
        users[uid].defence += 1 # повышение защиты персонажа на 1
        users[uid].hp = users[uid].max_hp # полное востановление хп игрока  
        if users[uid].next_lvl():
            bot.send_message(uid, "🎉Ты получил новый уровень🎉"
                                  "\n\nТвои характеристики:"
                                  "\n\nМаксимальное ХП: {0}❤\nСила: {1} 💪\nЗащита: {2} 🛡"
                                  "\n\nВыбери какую хар-ку ты хочешь увеличить:".
                             format(users[uid].max_hp, users[uid].power, users[uid].defence))
        else:
            game_menu(uid, GAME_MENU)  # переход в игровое меню
    else:
        bot.send_message(uid, 'Я не знаю что ответить 😢😢😢')


bot.polling()
