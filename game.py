# Importing all my modules from main
from main import *
from client import *

# Class for my main game
class Game():
    
    def __init__(self,c):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.RESOLUTION = (self.WIDTH, self.HEIGHT)

        # Calling the client class and setting it as an attribute in this class
        self.network = c

        # Initialising pygame, setting up the screen and setting up the clock
        self.screen = pygame.display.set_mode(self.RESOLUTION)

    # Drawing the background of the screen
    def draw(self):
        self.screen.fill((0,0,0))

    # Updating the screen
    def update_screen(self):
        pygame.display.flip()

# Calling my classes and creating instances of them
c = Client()
print(c)
g = Game(c)

# Main loop for the game
while True:

    # Checking if the quit button has been pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c.client.close()
            pygame.quit()
            sys.exit()

        # Moving the characters
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                c.player1.x += 10
            if event.key == pygame.K_LEFT:
                c.player1.x -= 10
            if event.key == pygame.K_DOWN:
                c.player1.y += 10
            if event.key == pygame.K_UP:
                c.player1.y -= 10

    # Drawing the screen
    g.draw()
    c.player1.draw_player(g.screen)

    # Sending player coordinates to the server
    c.send_object(c.player1)

    # Updating the screen
    g.update_screen()

    # Clockspeed
    clock.tick(80)
