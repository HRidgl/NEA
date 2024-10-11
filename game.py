# Importing all my modules from main
from main import *
from client import *
from server import *

# Class for my main game
class Game():
    
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.RESOLUTION = (self.WIDTH, self.HEIGHT)

        # Calling the client class and setting it as an attribute in this class
        self.network = Client()

        # Initialising pygame, setting up the screen and setting up the clock
        self.screen = pygame.display.set_mode(self.RESOLUTION)

    # Drawing the background of the screen
    def draw(self):
        self.screen.fill((255,255,255))

    # Updating the screen
    def update_screen(self):
        pygame.display.flip()


class S_Game(Game):
    def __init__(self,s):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.RESOLUTION = (self.WIDTH, self.HEIGHT)

        # Calling the client class and setting it as an attribute in this class
        self.network = s

        # Initialising pygame, setting up the screen and setting up the clock
        self.screen = pygame.display.set_mode(self.RESOLUTION)
