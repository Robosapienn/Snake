import pygame
import sys
import random

# initialize pygame modules
pygame.init()

# width and height variables for the window
cell_size = 40
cell_number = 20
screen_width = cell_size * cell_number
screen_height = cell_size * cell_number

# display surface
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('SNAKE')

# clock object
clock = pygame.time.Clock()

# event variables
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# sound

# fonts
score_font = pygame.font.Font('fonts/Minecraft.ttf', 25)
game_font = pygame.font.Font('fonts/Minecraft.ttf', 50)
