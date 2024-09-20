# In this file my code generates a random map each time the code is ran using the recursive backtracking algorithm.

# Importing modules from the main file
from main import *

# Predeclaing constants at the start of the program
WIDTH = 800
HEIGHT = 600
RESOLUTION = (WIDTH, HEIGHT)
TILE = 50
columns = WIDTH // TILE 
rows = HEIGHT // TILE

# Initialising pygame, setting up the screen and setting up the clock
pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

# Creating a class with all colours so that they can be easily accessed
class Colours:
    
    def __init__(self):
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)

        self.SAGE = (4, 99, 56)
        self.ORANGE = (237, 151, 2)
        self.MAGENTA = (214, 0, 129)

        self.LIGHT_BROWN = (166, 114, 0)
        self.SANDY = (252, 206, 106)
        self.BROWN = (189, 132, 0)
        

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        self.thickness = 2

    def draw_current_cell(self):
        x = self.x * TILE
        y = self.y * TILE
        pygame.draw.rect(screen, colours.MAGENTA, (x+2, y+2, TILE-2, TILE-2))

    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        if self.visited:
            pygame.draw.rect(screen, (colours.SANDY), (x,y,TILE,TILE))

        if self.walls['top']:
            pygame.draw.line(screen, colours.LIGHT_BROWN , (x, y), (x + TILE, y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(screen, colours.LIGHT_BROWN , (x + TILE, y), (x + TILE, y + TILE), self.thickness)
        if self.walls['bottom']:
            pygame.draw.line(screen, colours.LIGHT_BROWN , (x + TILE, y + TILE), (x , y + TILE), self.thickness)
        if self.walls['left']:
            pygame.draw.line(screen, colours.LIGHT_BROWN , (x, y + TILE), (x, y), self.thickness)

    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * columns
        if x < 0 or x > columns - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x, y)]
    
    def check_neighbours(self):
        neighbours = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbours.append(top)
        if right and not right.visited:
            neighbours.append(right)
        if bottom and not bottom.visited:
            neighbours.append(bottom)
        if left and not left.visited:
            neighbours.append(left)
        return choice(neighbours) if neighbours else False
    
def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False

# Initialising my colours class
colours = Colours()

# Creating the cells in the grid for the maze
grid_cells = [Cell(col,row) for row in range(rows) for col in range(columns)]
current_cell = grid_cells[0]

# Creating a stack so my algorithm can backtrack
stack = []

while True:
    screen.fill(colours.BROWN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [cell.draw() for cell in grid_cells]
    current_cell.visited = True
    current_cell.draw_current_cell()

    next_cell = current_cell.check_neighbours()
    if next_cell:
        next_cell.visited = True
        stack.append(current_cell)
        remove_walls(current_cell, next_cell)
        current_cell = next_cell
    elif stack:
        current_cell = stack.pop()

    pygame.display.flip()
    clock.tick(80)
