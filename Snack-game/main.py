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
snack_body = [(snack_x, snack_y)]

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
            new_x = snack_body[0][0] + pos_x
            new_y = snack_body[0][1] + pos_y

            snack_body.insert(0, (new_x, new_y))

            if new_x == food_x and new_y == food_y:
                food_x, food_y = get_random_food_pos()
            else:
                snack_body.pop()

    food = pygame.Rect(grid[food_y][food_x][0], grid[food_y][food_x][1], 25, 25)
    pygame.draw.rect(screen, 'yellow', food)

    for parts in snack_body:
        part = pygame.Rect(grid[parts[1]][parts[0]][0], grid[parts[1]][parts[0]][1], 25, 25)
        pygame.draw.rect(screen, 'Red', part)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()
