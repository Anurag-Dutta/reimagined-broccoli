import pygame
import random
pygame.init()
width = 1366
height = 768
gamewindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
gameover = False
exitgame = False
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snake_init_x = 40
snake_init_y = 50
snake_init_length = 20
snake_init_width = 20
snake_init_velocity_x = 0
snake_init_velocity_y = 0
fps = 10
food_x = random.randint(20, width / 2)
food_y = random.randint(20, height / 2)
score = 0

while not exitgame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_init_velocity_x = 20
                snake_init_velocity_y = 0
            if event.key == pygame.K_LEFT:
                snake_init_velocity_x = -20
                snake_init_velocity_y = 0
            if event.key == pygame.K_UP:
                snake_init_velocity_y = -20
                snake_init_velocity_x = 0
            if event.key == pygame.K_DOWN:
                snake_init_velocity_y = 20
                snake_init_velocity_x = 0
    snake_init_x += snake_init_velocity_x
    snake_init_y += snake_init_velocity_y

    if abs(snake_init_x - food_x) < 20 and abs(snake_init_y - food_y) < 20:
        food_x = random.randint(20, width / 2)
        food_y = random.randint(20, height / 2)
        score = score + 1
        fps = 1.002 * fps
        print(score, fps)

    gamewindow.fill(black)
    pygame.draw.rect(gamewindow, white, [food_x, food_y, 20, 20])
    pygame.draw.rect(gamewindow, red, [snake_init_x, snake_init_y, snake_init_length, snake_init_width])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
exit()