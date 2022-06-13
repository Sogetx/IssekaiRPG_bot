from enemys.Enemy import Enemy


class Caravan(Enemy):
    def __init__(self):
        super().__init__()
        self.max_hp = 3000
        self.hp = self.max_hp
        self.money = 400
        self.run_att = 1  # чтоб караван не сбежал
        self.name = "Караван"
        self.description = 'Долго бить, но награда стоит того'
        self.death = "Караван ограблен"
        self.sticker = "CAACAgIAAxkBAAEE-BdipLAu9nhDBcOKyMSGHdfsI_Y8_wACAiMAAnrSKUkg1c2NRJYR1yQE"
        self.loot = []

    def __repr__(self):  # Характеристики моба
        return "{0}❤, урон: {1}💥".format(self.hp, self.damage1)
