from events.event import Event


class ActiveEvent(Event):

    def __init__(self, stats):
        super().__init__(stats[1])
        self.name = stats[0]
        self.buttons = stats[2]

    def active_action(self, user, msg):  # если с ивентом нужно взаимодействовать
        return True
