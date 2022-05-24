# Boundary Limit imposed
import pygame
import random
pygame.init()
width = 1366
height = 768
gamewindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

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
velocity_counter = 5
fps = 60
food_x = random.randint(100, width - 100)
food_y = random.randint(100, height - 100)
score = 0
# We will make two variables “snake_list” and “snake_length”.
# “snake_list” will be a list of list.
# It will have co-ordinates of the snake’s rectangles.
# “snake_length” will have an integer and we will increment it’s value everytime our snake eats food.
snake_list = []
snake_length = 1
def plot_snake(gamewindow, color, snake_list, snake_size):
    i = 0
    for x,y in snake_list:
        if i == 0:
            pygame.draw.rect(gamewindow, white, [x, y, snake_init_length, snake_init_length])
            i = 1
        else:
            pygame.draw.rect(gamewindow, color, [x, y, snake_init_length, snake_init_length])

while not exitgame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_init_velocity_x = velocity_counter
                snake_init_velocity_y = 0
            if event.key == pygame.K_LEFT:
                snake_init_velocity_x = -velocity_counter
                snake_init_velocity_y = 0
            if event.key == pygame.K_UP:
                snake_init_velocity_y = -velocity_counter
                snake_init_velocity_x = 0
            if event.key == pygame.K_DOWN:
                snake_init_velocity_y = velocity_counter
                snake_init_velocity_x = 0
    snake_init_x += snake_init_velocity_x
    snake_init_y += snake_init_velocity_y
    if abs(snake_init_x - food_x) < 20 and abs(snake_init_y - food_y) < 20:
        food_x = random.randint(100, width - 100)
        food_y = random.randint(100, height - 100)
        score = score + 1
        velocity_counter *= 1.002
        snake_length = snake_length + 5
    gamewindow.fill(black)
    text_screen("Score: " + str(score), white, 5, 5)
    # text_screen("FPS: " + str(fps + random.randint(1, 100)/random.randint(1, 100)), white, width - 500, 5)
    text_screen("Velocity: " + str(velocity_counter), white, width - 500, 5)
    pygame.draw.rect(gamewindow, white, [food_x, food_y, 20, 20])
    head = []
    head.append(snake_init_x)
    head.append(snake_init_y)
    snake_list.append(head)
    if snake_init_x < 0:
        gameover = True
        break
    if snake_init_y < 0:
        gameover = True
        break
    if snake_init_y > height:
        gameover = True
        break
    if snake_init_x > width:
        gameover = True
        break
    if len(snake_list) > snake_length:
        del snake_list[0]
    plot_snake(gamewindow, red, snake_list, snake_length)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
exit()