from pets.pet import Pet


class AlphaWolf(Pet):
    def __init__(self):
        super().__init__()
        self.name = "Альфа волк"
        self.description = "Он как волк только альфа, главный типо, ну вы поняли"
        self.power = 1.7
        self.defence = 1.6
        self.damage = 2
