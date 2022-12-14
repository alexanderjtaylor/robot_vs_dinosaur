from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__(self):
        self.robot = Robot("Robo Cop")
        self.dinosaur = Dinosaur("T-Rex", 10)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        
    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur! Get ready to fight!")

    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)

    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f"The battle is over! {self.robot.name} is the winner!")
        else:
             print(f"The battle is over! {self.dinosaur.name} is the winner!")