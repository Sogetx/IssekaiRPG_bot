from Events.Pets.Pet import Pet


class Pet1(Pet):
    def __init__(self):
        super().__init__()
        self.name = "питомец111"
        self.description = "описание"
        self.power = 1.3  # модификатор силы
        self.defence = 1.2  # модификатор защиты
        self.damage = 1.1  # модификатор атаки
