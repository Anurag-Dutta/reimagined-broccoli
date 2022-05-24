import pygame
pygame.init()
gamewindow = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
gameover = False
exitgame = False
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snake_init_x = 40
snake_init_y = 50
snake_init_length = 10
snake_init_width = 10
snake_init_velocity_x = 0
snake_init_velocity_y = 0
fps = 30

while not exitgame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_init_velocity_x = 10
                snake_init_velocity_y = 0
            if event.key == pygame.K_LEFT:
                snake_init_velocity_x = -10
                snake_init_velocity_y = 0
            if event.key == pygame.K_UP:
                snake_init_velocity_y = -10
                snake_init_velocity_x = 0
            if event.key == pygame.K_DOWN:
                snake_init_velocity_y = 10
                snake_init_velocity_x = 0
    snake_init_x += snake_init_velocity_x
    snake_init_y += snake_init_velocity_y
    gamewindow.fill(black)
    pygame.draw.circle(gamewindow, red, [snake_init_x, snake_init_y], snake_init_length)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
exit()