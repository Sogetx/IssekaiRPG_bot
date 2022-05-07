from buttons_generator import buttons_generator
from telebot import *
from constants import *
import shop
import User
import config
import random
from Enemys.fight_system import enemy_create, bot_fight
from Events.events_sys import events_create

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
users = {}  # словарь(масив ключ-значение) пользователей


@bot.message_handler(commands=['start'])
def start(msg):  # обработчик команды /start
    users[msg.chat.id] = User.User(msg.chat.id)  # добавление пользователя в словарь при начале игры
    user = users[msg.chat.id]
    # удаление моба, если игрок ввел /start в процессе боя, иначе будет продолжатся прерваный бой
    if user.enemy is not None:
        user.enemy = None
    bot.send_sticker(user.id, HELLO_STICKER)  # приветственный стикер
    bot.send_message(user.id, "Добро пожаловать, {0.first_name}!\n"
                          "Я - {1.first_name}, бот который будет вести тебя по вымышленому, "
                          "созданому по больной фантазии авторов, фэнтези мире".
                     format(msg.from_user, bot.get_me()), reply_markup=buttons_generator(MAIN_MENU_BUTTONS))


@bot.message_handler(commands=['help'])
def settings(msg):  # обработчик команды /help
    bot.send_message(msg.chat.id, 'Вот мой список команд:\n /start \n /help')


@bot.message_handler(content_types=['text'])
def bot_message(msg):  # обработчик текста
    user = users[msg.chat.id]
    try:  # возможна ошибка KeyError
        if user.id.menu == GAME_MENU:
            game_menu(user, msg.text)
        elif user.id.menu == FIGHT_MENU:
            fight_menu(user, msg.text)
        elif user.id.menu == MAIN_MENU:
            main_menu(user, msg.text)
        elif user.id.menu == NEW_LVL:
            new_level(user, msg.text)
        elif user.id.menu == DEATH:  # если пользователь пишет сообщение боту, но он уже мертв
            bot.send_message(user.id, 'Ты же уже мертв, куда тебе идти то?\n\n'
                                      '         --> /start <--')
            bot.send_message(user.id, "⚰️")
    except KeyError:
        bot.send_message(user.id, 'Произошли какие-то траблы, нужно перезапустить бота',
                         reply_markup=buttons_generator(["/start"]))


def fight_menu(user, msg):  # Все что связано с взаимодействием в бою
    if msg == GO_AHEAD:
        bot.send_message(user.id, "Ты встретил моба\n\n" + enemy_create(user),
                         reply_markup=buttons_generator(FIGHT_MENU_BUTTONS))
        bot.send_sticker(user.id, user.enemy.sticker)
        user.menu = FIGHT_MENU
    elif msg == RUN:  # сбежать
        user.enemy = None
        game_menu(user.id, GAME_MENU)  # переход в игровое меню
        bot.send_message(user.id, 'Ты сбежал')
    elif msg == TO_DAMAGE:  # Ударить врага
        bot_fight(user.id, user, game_menu, new_level)
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def events_menu(user, msg):  # Все что связано с взаимодействием c ивентом
    if msg == GO_AHEAD:
        bot.send_message(user.id, "{1}\n\nРезультат: {0}".format(events_create(user), user.event.description))
        bot.send_message(user.id, 'Вы пережили еще одно событие')
        game_menu(user.id, GAME_MENU)
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def main_menu(user, msg):
    if msg == MAIN_MENU:  # Если было выбрано главное меню
        bot.send_message(user.id, "Ты вернулся в главное меню", reply_markup=buttons_generator(MAIN_MENU_BUTTONS2))
        user.menu = MAIN_MENU
    elif msg == CONTINUE_GAME or msg == START_NEW_GAME:
        game_menu(user.id, GAME_MENU)  # переход в игровое меню
    elif msg == SUPPORT:
        bot.send_message(user.id, "@Dimasik333 - Telegram Дима\nlevstepanenko@gmail.com - Gmail Лев")
    else:
        bot.send_message(user.id, 'Я не знаю что ответить 😢😢😢')


def game_menu(user, msg):  # игровое меню: статистика, магазин, пойти в бой и возврат в главное меню
    if msg == GAME_MENU:
        bot.send_message(user.id, "У тебя:\n{0}❤ {1}💵\n\nЧе дальше будеш делать?".
                         format(user.hp, user.money), reply_markup=buttons_generator(GAME_MENU_BUTTONS))
        user.menu = GAME_MENU
    elif msg == SHOP:
        # # # переход в меню магазина # # #
        bot.send_sticker(user.id, SHOP_STICKER)
        bot.send_message(user.id, 'Тут должен был быть магаз, но он еще в разработке, сарян')
    elif msg == GO_AHEAD:
        user.go_ahead_count += 1
        go = random.randint(1, 5)
        if go == 1:
            events_menu(user.id, msg)
        else:
            fight_menu(user.id, msg)
    elif msg == MAIN_MENU:
        main_menu(user.id, MAIN_MENU)
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
                         reply_markup=buttons_generator(NEW_LVL_BUTTONS))
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
            game_menu(user.id, GAME_MENU)  # переход в игровое меню


bot.polling()
