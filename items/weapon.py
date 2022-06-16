from items.item import Item

class Weapon(Item):
    def __init__(self,stats):
        super().__init__(stats),
        self.damage = stats[4]