class Pet:
    def __init__(self):
        self.name = None
        self.description = None
        self.power = 1  # модификатор силы
        self.defence = 1  # модификатор защиты
        self.damage = 1  # модификатор атаки
        self.sticker = None

    def __repr__(self):
        return "{0}\n\n{1}".format(self.name, self.description)
