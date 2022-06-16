class Pet:
    def __init__(self, stats):
        self.name = stats[0]  # имя питомца
        self.description = stats[1]  # описание питомца
        self.power = stats[2]  # модификатор силы
        self.defence = stats[3]  # модификатор защиты
        self.damage = stats[4]  # модификатор атаки

    def __repr__(self):
        return "{0}\n\n{1}\nx{2} 💥, x{3} 💪, x{4} 🛡".\
            format(self.name, self.description, self.damage, self.power, self.defence)
