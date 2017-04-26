import random


class Weapons(object):
    min_dmg = 1
    max_dmg = 1

    def damage(self):
        damage = random.randint(self.min_dmg, self.max_dmg)
        return damage

    def __str__(self):
        return "{} - Damage: {} - {}".format(self.__class__.__name__, self.min_dmg, self.max_dmg)


class Sword(Weapons):
    def __init__(self):
        self.min_dmg = 1
        self.max_dmg = 2


class Axe(Weapons):
    def __init__(self):
        self.min_dmg = 1
        self.max_dmg = 3


class Bow(Weapons):
    def __init__(self):
        self.min_dmg = 2
        self.max_dmg = 3

