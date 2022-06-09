from Items import *
from config import TELEGRAM_TOKEN
from telebot import *

bot = telebot.TeleBot(TELEGRAM_TOKEN)

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

# предметы которые продаются в магазине
SHOP_ITEMS = {Scroll_of_power().name: Scroll_of_power(),
              Scroll_of_defence().name: Scroll_of_defence(),
              Scroll_of_crit().name: Scroll_of_crit(),
              Small_hp_potion().name: Small_hp_potion(),
              Medium_hp_potion().name: Medium_hp_potion(),
              Big_hp_potion().name: Big_hp_potion(),
              Banana().name: Banana(),
              Scrap().name: Scrap(),
              Sock().name: Sock(),
              Candy().name: Candy(),
              Potato().name: Potato()}
