import pygame
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
running = True

grid = [[pygame.Rect(i, j, 25, 25) for i in range(0, 2000, 25)] for j in range(0, 1000, 25)]
snack_x = randint(5, 35)
snack_y = randint(5, 16)
pos_x = 0
pos_y = 0

snack_timer = pygame.USEREVENT + 1
pygame.time.set_timer(snack_timer, 300)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == snack_timer:
            snack_x += pos_x
            snack_y += pos_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pos_y = -1
        pos_x = 0
    elif keys[pygame.K_a]:
        pos_y = 0
        pos_x = -1
    elif keys[pygame.K_s]:
        pos_y = 1
        pos_x = 0
    elif keys[pygame.K_d]:
        pos_y = 0
        pos_x = 1
    else:
        pass

    pygame.draw.rect(screen, 'Red', grid[snack_y][snack_x])

    pygame.display.update()
    screen.fill('Black')
    clock.tick(60)

pygame.quit()
exit()
