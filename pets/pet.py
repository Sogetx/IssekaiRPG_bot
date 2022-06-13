class Pet:
    def __init__(self):
        self.name = None  # имя питомца
        self.description = None  # описание питомца
        self.power = 1  # модификатор силы
        self.defence = 1  # модификатор защиты
        self.damage = 1  # модификатор атаки

    def __repr__(self):
        return "{0}\n\n{1}\nx{2} 💥, x{3} 💪, x{4} 🛡".\
            format(self.name, self.description, self.damage, self.power, self.defence)
