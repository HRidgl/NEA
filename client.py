import pygame

#constants
WIDTH = 500
HEIGHT = 500

#colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

#screen
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Client")

#global varibales
clientNumber = 0

#creating the player
class Player():
    def __init__(self,x,y,width,height,colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self,win):
        pygame.draw.rect(win,self.colour,self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x,self.y,self.width,self.height)

#redraws the screen
def redrawWindow(win,player):
    win.fill(white)
    player.draw(win)
    pygame.display.update()

#main game loop
def main():
    run = True
    p = Player(50,50,100,100,green)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quite()

        p.move()
        redrawWindow(win,p)

main()