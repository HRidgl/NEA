from main import *
from client import *

class Game():
    def __init__(self,c):

        self.WIDTH = 800
        self.HEIGHT = 600
        self.RESOLUTION = (self.WIDTH, self.HEIGHT)

        self.network = c

        # Initialising pygame, setting up the screen and setting up the clock
        self.screen = pygame.display.set_mode(self.RESOLUTION)
        
    def draw(self):
        self.screen.fill((0,0,0))
    
    def update_screen(self):
        pygame.display.flip()
        clock.tick(80)

c = Client()
g = Game(c)

while True:
    c = Client()
    g.draw()
    g.update_screen()
    c.send_object(c.player1)
    c.client.close()

pygame.quit()
