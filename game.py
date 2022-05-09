from settings import *
from snake import SNAKE
from fruit import FRUIT

class GAME:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.over = False
        self.menu = False

    def update(self):
        if self.over is False and self.menu is False:
            self.snake.move_snake()
            self.check_collision()
            self.check_gamestate()
        elif self.over is False and self.menu is True:
            screen.fill((0, 0, 0))

    def draw(self):
        if self.menu is True:
            self.draw_text('PLAY AGAIN', cell_size, screen_width / 2, screen_height / 2)
        elif self.menu is False and self.over is False:
            screen.fill((0, 0, 0))
            self.snake.draw_snake()
            self.fruit.draw_fruit()
            self.draw_score()
            self.draw_line()
        elif self.over is True:
            self.draw_gameover()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # snake movement timer
            if event.type == SCREEN_UPDATE:
                self.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if self.over is True:
                    if event.key == pygame.K_r:
                        self.restart()

                # snake movement input
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if game.snake.direction.y != 1:
                        game.snake.direction = pygame.math.Vector2(0, -1)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if game.snake.direction.x != 1:
                        game.snake.direction = pygame.math.Vector2(-1, 0)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if game.snake.direction.y != -1:
                        game.snake.direction = pygame.math.Vector2(0, 1)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if game.snake.direction.x != -1:
                        game.snake.direction = pygame.math.Vector2(1, 0)

            # draw everything
            self.draw()

            # update everything
            pygame.display.update()

            # how many times the while loop runs per second
            clock.tick(60)

    def check_collision(self):
        # checks if the snake ate the fruit and creates a new fruit if true
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.new_fruit()
            self.snake.new_block()

        # checks if the position of the fruit is equal to the position of the body parts of the snake
        # and if this is true, the fruits is respawned
        for part in self.snake.body[1:]:
            x_pos = int(part.x * cell_size)
            y_pos = int(part.y * cell_size)
            if x_pos == self.fruit.pos.x * cell_size and y_pos == self.fruit.pos.y * cell_size:
                self.fruit.new_fruit()

    def check_gamestate(self):
        # check if snake hits the line
        if self.snake.body[0].y * cell_size < cell_size * 2:
            self.over = True

        # check if snake hits the walls
        if not 0 <= self.snake.body[0].x < cell_number:
            self.over = True
        if not 0 <= self.snake.body[0].y < cell_number:
            self.over = True
        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.over = True

    def restart(self):
        self.snake.body = [pygame.math.Vector2(5, 10), pygame.math.Vector2(4, 10), pygame.math.Vector2(3, 10)]
        self.over = False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font('fonts/Minecraft.ttf', size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    def draw_line(self):
        line_ypos = cell_size * 2
        score_line = pygame.Rect(0, line_ypos, screen_width, 5)
        pygame.draw.rect(screen, (255, 255, 255), score_line)

    def draw_score(self):
        snake_length = len(self.snake.body) - 3
        score_text = str(f"SCORE: {snake_length}")
        score_surf = score_font.render(score_text, True, (255, 255, 255))
        score_xpos = int(cell_size)
        score_ypos = int(cell_size)
        score_rect = score_surf.get_rect(topleft=(score_xpos, score_ypos))

        screen.blit(score_surf, score_rect)

    def draw_gameover(self):
        gameover_text = 'GAME OVER'
        gameover_surf = game_font.render(gameover_text, True, (255, 255, 255))
        xpos = int(cell_size * cell_number / 2)
        ypos = int(cell_size * cell_number / 2)
        gameover_rect = gameover_surf.get_rect(center=(xpos, ypos))

        escape_text = 'PRESS ESCAPE TO EXIT'
        escape_surf = game_font.render(escape_text, True, (255, 255, 255))
        escape_rect = escape_surf.get_rect(center=(xpos, ypos + cell_size * 2))

        restart_text = 'PRESS R TO PLAY AGAIN'
        restart_surf = game_font.render(restart_text, True, (255, 255, 255))
        restart_rect = restart_surf.get_rect(center=(xpos, ypos + cell_size * 4))

        screen.fill((0, 0, 0))
        screen.blit(gameover_surf, gameover_rect)
        screen.blit(escape_surf, escape_rect)
        screen.blit(restart_surf, restart_rect)


# game object which includes the player(snake) and the fruit
game = GAME()
