from settings import *

class FRUIT:
    def __init__(self):
        # check the new_fruit method to understand the purpose of these variables
        self.x = 0
        self.y = 0
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.new_fruit()

    def draw_fruit(self):
        # create rectangle and draw the rectangle of the fruit
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 0, 0), fruit_rect)

    def new_fruit(self):
        # create an x and y position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        # create 2D vector
        self.pos = pygame.math.Vector2(self.x, self.y)
        # if the fruit y pos is above the score line, call the function again
        if self.pos.y * cell_size < cell_size * 2:
            self.new_fruit()
