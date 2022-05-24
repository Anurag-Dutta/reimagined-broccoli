import pygame
pygame.init()
gamewindow = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Snake Game")
gameover = False
exitgame = False
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snake_x = 40
snake_y = 50
snake_length = 60
snake_width = 10

while not exitgame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True

    gamewindow.fill(white)
    pygame.draw.rect(gamewindow, red, [snake_x, snake_y, snake_length, snake_width])
    pygame.display.update()

pygame.quit()
exit()