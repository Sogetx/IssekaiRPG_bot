from Items.Item import Item


class Sock(Item):
    def __init__(self):
        super().__init__()
        self.name = "🧦"
        self.description = "Этот носок может кому-то помочь стать свободным"
        self.price = 100
