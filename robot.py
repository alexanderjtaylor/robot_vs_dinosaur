from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Kitchen Knife", 10)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f"{self.name} attacked {dinosaur.name} and did {self.active_weapon.attack_power} damage, leaving {dinosaur.name} with {dinosaur.health} health left!")