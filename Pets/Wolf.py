from Pets.Pet import Pet


class Wolf(Pet):
    def __init__(self):
        super().__init__()
        self.name = "волк"
        self.description = "волчара"
        self.power = 1.2  # модификатор силы
        self.defence = 1  # модификатор защиты
        self.damage = 1.4  # модификатор атаки
        self.sticker = "CAACAgIAAxkBAAEEvo5igm2RJlk3whxblNP7bhJAW2Zk4wACuhwAAkJZEEhoXmwwkIotEyQE"
