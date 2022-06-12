from Items.Item import Item


class Golden_Sword(Item):
    def __init__(self):
        super().__init__()
        self.name = "Золотой меч"
        self.description = "С ним в аду бродят все свинозомби"
        self.price = 600
        self.is_used = True
        self.damage = 25
