from Events.Event import Event


class Church(Event):
    def __init__(self):
        super().__init__()
        self.description = "Вы заходите в небольшое святилище, оно аккуратное, чистое хотя никого в нем нету. " \
                           "Постояв у алтаря вам становиться легче а раны затягиваються"

    def action(self, user):
        result = user.max_hp - user.hp
        user.heal(user.max_hp)
        return "+" + str(result) + " ❤"
