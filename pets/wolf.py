from pets.pet import Pet


class Wolf(Pet):
    def __init__(self):
        super().__init__()
        self.name = "Взрослый волк"
        self.description = "Здесь должна быть цитата из пацанского паблика но кто сейчас сидит в пабликах."
        self.power = 1.4
        self.defence = 1.3
        self.damage = 1.7
