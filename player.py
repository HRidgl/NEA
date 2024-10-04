from main import *

class Player:
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = (255,255,255)

    def draw_player(self,screen):
        player_square = pygame.Rect(self.x, self.y, 50, 50)
        pygame.draw.rect(screen, (255, 0, 0), player_square)

    def set_x(self,new_x):
        self.x = new_x

    def set_y(self,new_y):
        self.y = new_y
