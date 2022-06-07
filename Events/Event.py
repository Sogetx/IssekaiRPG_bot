class Event:
    def __init__(self):
        self.description = "описание ивента"
        self.is_active = False

    def action(self, user): # действия выполняемые при создании ивента
        # действия с user
        return "результат"
