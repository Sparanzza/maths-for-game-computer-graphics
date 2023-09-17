import pygame
import random

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)

def to_pygame_coordinates(display, x, y):
    return x, display.get_height() - y


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    rand_x = random.randint(0, screen_width - 10)
    rand_y = random.randint(0, screen_height - 10)

    position = to_pygame_coordinates(screen, rand_x, rand_y)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))

    pygame.display.update()
pygame.quit()