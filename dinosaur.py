
class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        robot.health -= self.attack_power

T_Rex = Dinosaur("T-Rex", 10)
# print(T_Rex.name, T_Rex.attack_power, T_Rex.health)