### This file is used to set up the main screen for the game

# Importing all my modules from main
from main import *

# Class for my main game
class Game():
    
    def __init__(self):
        self.WIDTH = 400
        self.HEIGHT = 400
        self.RESOLUTION = (self.WIDTH, self.HEIGHT)

        # Initialising pygame, setting up the screen and setting up the clock
        self.screen = pygame.display.set_mode(self.RESOLUTION)

    # Drawing the background of the screen
    def draw(self):
        self.screen.fill((255,255,255))

    # Updating the screen
    def update_screen(self):
        pygame.display.flip()
