class Event:
    def __init__(self, description):
        self.description = description

    def action(self, user):  # действия выполняемые при создании ивента, если он без активного взаимодействия с юзером
        # действия с user
        return "результат"
