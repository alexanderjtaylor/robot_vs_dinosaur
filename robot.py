from weapon import Weapon, Kitchen_Knife
from dinosaur import Dinosaur, T_Rex

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Kitchen_Knife

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power

Robo_Cop = Robot("Robo Cop")
# print(Robo_Cop.name, Robo_Cop.health, Robo_Cop.active_weapon.name, Robo_Cop.active_weapon.attack_power)
# robo_attack_dino = Robo_Cop.attack(Dinosaur("T-Rex", 10))

Robo_Cop.attack(T_Rex)
print(T_Rex.health)