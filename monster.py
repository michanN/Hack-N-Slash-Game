# Monster Class

# __init__ also called dunder init lets us control what happens when we create an instance, like values


import random
from combat import Combat

COLORS = ['green', 'black', 'gray', 'orange']


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_exp = 1
    max_exp = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.exp
                                              )


    def battlecry(self): # Every method on a class must at least take the self argument. Self always represent the instance that you are calling the method on
        return self.sound.upper()


class Goblin(Monster):
    max_hit_points = 3
    max_exp = 2
    sound = 'squeak'


class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_exp = 2
    max_exp = 6
    sound = 'growl'


class Undead(Monster):
    min_hit_points = 2
    max_hit_points = 4
    min_exp = 2
    max_exp = 3
    sound = 'death to the living'

class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_exp = 6
    max_exp = 10
    sound = 'raaaaaa'

