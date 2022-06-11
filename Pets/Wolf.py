from Pets.Pet import Pet


class Wolf(Pet):
    def __init__(self):
        super().__init__()
        self.name = "Взрослый волк"
        self.description = ""
        self.power = 1.4  # модификатор силы
        self.defence = 1.3  # модификатор защиты
        self.damage = 1.7  # модификатор атаки
