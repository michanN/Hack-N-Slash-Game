import random
from combat import Combat
from weapons import Sword, Axe, Bow


class Character(Combat, Sword, Axe, Bow):
    attack_limit = 10
    exp = 0
    base_hit_points = 10


    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if isinstance(self.weapon, Sword):
            roll += 1
        elif isinstance(self.weapon, Axe):
        #elif 'Axe' in str(self.weapon):
            roll += 2
        return roll > 4
    
    def get_weapon(self):
        weapon_choice = input('Weapon ([S]word, [A]xe), [B]ow').lower()
        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return Sword()
            elif weapon_choice == 'a':
                return Axe()
            else:
                return Bow()
        else:
            return self.get_weapon()

    def __init__(self, **kwargs):
        self.name = input('Name: ')
        self.weapon = self.get_weapon()
        self.hit_points = self.base_hit_points
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{}, HP: {}, XP: {}'.format(self.name, self.hit_points, self.exp)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1

    def leveled_up(self):
        return self.exp >= 5
