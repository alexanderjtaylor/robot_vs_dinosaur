from robot_vs_dinosaur.robot import Robot
from robot_vs_dinosaur.dinosaur import Dinosaur


class Battlefield:

    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def run_game(self):
        pass
        
    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur! Get ready to fight!")

    def battle_phase(self):
        pass

    def display_winner(self):
        pass