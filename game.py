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

c = Client()
g = Game(c)

while True:
    
    g.draw()
    c.player1.draw_player(g.screen)
    g.update_screen()

    c.send_object(c.player1.x)
    c.send_object(c.player1.y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c.client.close()
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                c.player1.x += 10
            if event.key == pygame.K_LEFT:
                c.player1.x -= 10
            if event.key == pygame.K_DOWN:
                c.player1.y += 10
            if event.key == pygame.K_UP:
                c.player1.y -= 10

    clock.tick(80)
