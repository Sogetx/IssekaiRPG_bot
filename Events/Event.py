class Event:
    def __init__(self):
        self.description = "описание ивента"
        self.is_active = False

    def action(self, user): # действия выполняемые при создании ивента
        # действия с user
        return "результат"

    def active_action(self, user, msg):
        #если с ивентом нужно взаимодействовать
        return True
