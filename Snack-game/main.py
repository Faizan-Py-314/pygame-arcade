import pygame
from sys import exit
from random import randint

def get_random_food_pos():
    food_x = randint(0, 39)
    food_y = randint(0, 19)

    return food_x, food_y

pygame.init()
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
running = True

grid = [[(i, j) for i in range(0, 2000, 25)] for j in range(0, 1000, 25)]
snack_x = randint(5, 35)
snack_y = randint(5, 15)
pos_x = 0
pos_y = 0

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 200)

food_x, food_y = get_random_food_pos()

while running:
    screen.fill('Black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and pos_y == 0:
                pos_y = -1
                pos_x = 0
            elif event.key == pygame.K_a and pos_x == 0:
                pos_y = 0
                pos_x = -1
            elif event.key == pygame.K_s and pos_y == 0:
                pos_y = 1
                pos_x = 0
            elif event.key == pygame.K_d and pos_x == 0:
                pos_y = 0
                pos_x = 1

        if event.type == timer:
            snack_x += pos_x
            snack_y += pos_y

    snack_head = pygame.Rect(grid[snack_y][snack_x][0], grid[snack_y][snack_x][1], 25, 25)
    pygame.draw.rect(screen, 'Red', snack_head)

    food = pygame.Rect(grid[food_y][food_x][0], grid[food_y][food_x][1], 25, 25)
    pygame.draw.rect(screen, 'yellow', food)

    if snack_x == food_x and snack_y == food_y:
        food_x, food_y = get_random_food_pos()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()
