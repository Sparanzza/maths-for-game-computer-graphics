import pygame

pygame.init()
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('A beautiful sunset')
done = False

background = pygame.image.load('../images/sunset.png')
sprite = pygame.image.load('../images/ryu.png')
sprite = pygame.transform.scale(sprite, (sprite.get_width() // 2, sprite.get_height() // 2))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))
    screen.blit(sprite, (400, 400))
    pygame.display.update()
pygame.quit()
