# from main import users, enemys, bot, game_menu
#
# import random
# import Enemys
# import main
#
#
# def bot_fight(user_id):
#     user = users[user_id]
#     enemy = enemys[user_id]
#     user.take_damage(enemy.to_damage())
#     enemy.take_damage(user.to_damage())
#     if enemy.hp > 0:
#         bot.send_message(user_id, "У врага осталось: " + repr(enemy))
#         bot.send_message(user_id, "У тебя осталось: " + repr(user))
#     else:
#         enemys.pop(user_id)
#         bot.send_message(user_id, "враг отправился на тот мир")
#         game_menu(user_id)
#
#
# def enemy_create(user_id):
#     if user_id not in enemys.keys():
#         enm = random.randint(1, 2)
#         if enm == 1:
#             enemys[user_id] = Enemys.GiantCockroach.GiantCockroach()
#         elif enm == 2:
#             enemys[user_id] = Enemys.Rat.Rat()
#         bot.send_message(user_id, enemys[user_id].description)