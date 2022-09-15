from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__(self):
        self.robot = Robot("Robo Cop")
        self.dinosaur = Dinosaur("T-Rex", 10)

    def run_game(self):
        self.robot.attack()
        self.dinosaur.attack()
        
    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur! Get ready to fight!")

    def battle_phase(self):
        pass

    def display_winner(self):
        pass