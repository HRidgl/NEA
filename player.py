### This file is used to store all player functionality separately from the rest of the system for easy access.

# Importing all the modules from main
from main import *

# Class for creating player objects
class Player:
    
    def __init__(self,name,x,y,width,height,colour):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    # Method for drawing players to the screen
    def draw(self,screen):
        player_square = pygame.Rect(self.x, self.y, 50, 50)
        pygame.draw.rect(screen, self.colour, player_square)

    # Changing the x coordinate of the characters
    def set_x(self,new_x):
        self.x = new_x

    # Changing the x coordinate of the characters
    def set_y(self,new_y):
        self.y = new_y
