from pets.pet import Pet


class Puppy(Pet):
    def __init__(self):
        super().__init__()
        self.name = "Щенок"
        self.description = "Знаете брать в такое опасное приключение щенка возможно не стоило"
        self.power = 1.2
        self.defence = 1
        self.damage = 1.4
