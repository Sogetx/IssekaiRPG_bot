from Items import *
from config import TELEGRAM_TOKEN
from telebot import *
#from Events.Pets import *

bot = telebot.TeleBot(TELEGRAM_TOKEN)
# # # # # # # # # #   Стикеры   # # # # # # # # # #
HELLO_STICKER = "CAACAgIAAxkBAAEEmbFibmcM88jMUQhItJWitmTQeBjFdgACSRYAAsOLeEs1cJYvU2PfdyQE"
SHOP_STICKER = "CAACAgIAAxkBAAEEmbNibmeymHwNw_LwnwmbL7sC4ifSoAACYRYAApUBeUsatN_ZdOmq6CQE"
DEATH_STICKER = "CAACAgIAAxkBAAEEms1ibridDAOemzBFkVXyS8LUmExOVgACRxcAAvuxcEvbmQyQSCSazyQE"
# # # # # # # # # #   Действия   # # # # # # # # # #
RUN = "Сбежать 🏃‍♂"
START_NEW_GAME = "Начать свое приключение 🕹"
SUPPORT = "Поддержка ☎"
SHOP = "Магазин 🏪"
GO_AHEAD = "Продолжить путь 🚶‍♂"
TO_DAMAGE = "Нанести урон 💥"
CONTINUE_GAME = "Продолжить приключение 🕹"
STATISTICS = "Статистика 👤"
ADD_POWER = "Сила 💪 +2"
ADD_DEFENCE = "Защита 🛡 +2"
ADD_CRIT = "Шанс крита 🎯 +1"
ADD_HP = "Максимальное ХП ❤ +10"
BACK = "◀ Назад ◀"
INVENTORY = "Инвентарь 🎒"
TORY = "Максимальное ХП ❤ +10"
NEXT_PAGE = "▶Следующая страничка▶"
BACK_PAGE = "◀Предидущая страничка◀"
# # # # # # # # # #   меню игрока   # # # # # # # # # #
MAIN_MENU = "◀ В главное меню ◀"
GAME_MENU = 1
FIGHT_MENU = 2
DEATH = 3
NEW_LVL = 4
EVENTS_MENU = 5
SHOP_MENU = 6
INVENTORY_MENU = 7
# # # # # # # # # #   меню кнопок   # # # # # # # # # #
MAIN_MENU_BUTTONS = [START_NEW_GAME, SUPPORT]
MAIN_MENU_BUTTONS2 = [CONTINUE_GAME, SUPPORT]
GAME_MENU_BUTTONS = [SHOP, GO_AHEAD, INVENTORY, STATISTICS, MAIN_MENU]
FIGHT_MENU_BUTTONS = [RUN, TO_DAMAGE, INVENTORY]
NEW_LVL_BUTTONS = [ADD_POWER, ADD_DEFENCE, ADD_CRIT, ADD_HP]
EVENTS_MENU_BUTTONS = []
SHOP_ITEMS = {Scroll_of_power().name: Scroll_of_power(),
              Scroll_of_defence().name: Scroll_of_defence(),
              Scroll_of_crit().name: Scroll_of_crit(),
              Small_hp_potion().name: Small_hp_potion(),
              Medium_hp_potion().name: Medium_hp_potion(),
              Big_hp_potion().name: Big_hp_potion()}
