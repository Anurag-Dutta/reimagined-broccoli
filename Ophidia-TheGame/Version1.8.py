import pygame
pygame.init()
gamewindow = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
gameover = False
exitgame = False
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snake_x = 40
snake_y = 50
snake_length = 10
snake_width = 10
fps = 60

while not exitgame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10
    gamewindow.fill(white)
    pygame.draw.rect(gamewindow, red, [snake_x, snake_y, snake_length, snake_width])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
exit()