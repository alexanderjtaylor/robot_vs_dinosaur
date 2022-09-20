from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = [Weapon("Kitchen Knife", 10), Weapon("Ray Gun", 25), Weapon("Lead Pipe", 5)]

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon[1].attack_power
        print(f"{self.name} attacked {dinosaur.name} with {self.active_weapon[1].name} and did {self.active_weapon[1].attack_power} damage, leaving {dinosaur.name} with {dinosaur.health} health left!")