from settings import *

class SNAKE:
    def __init__(self):
        # create the body of the snake
        self.body = [pygame.math.Vector2(5, 10), pygame.math.Vector2(4, 10), pygame.math.Vector2(3, 10)]
        self.direction = pygame.math.Vector2(1, 0)
        self.block = False

    def draw_snake(self):
        for part in self.body:
            # create the rectangle and draw the rectangle of the snake
            x_pos = int(part.x * cell_size)
            y_pos = int(part.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (255, 255, 255), block_rect)

    def move_snake(self):
        if self.block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.block = False
        else:
            # copy the first 2 elements of the vector list
            body_copy = self.body[0:-1]
            # increment position
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def new_block(self):
        self.block = True
