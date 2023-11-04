import pygame

pygame.init()
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('A beautiful sunset')
done = False

background = pygame.image.load('img.png')
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))
    pygame.display.update()
pygame.quit()
