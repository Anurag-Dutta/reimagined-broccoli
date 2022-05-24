# Game Over Concept Improved
# Graphics Revamped
import pygame
import random
pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
width = 1366
height = 768
snake_init_length = 20
snake_init_width = 20
gamewindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

clock = pygame.time.Clock()

def plot_snake(gamewindow, color, snake_list, snake_size):
    i = 0
    for x,y in snake_list:
        if i % 2 == 0:
            pygame.draw.rect(gamewindow, white, [x, y, snake_init_length, snake_init_length])
            i = i + 1
        else:
            pygame.draw.rect(gamewindow, red, [x, y, snake_init_length, snake_init_length])
            i = i + 1
def game_loop():
    gameover = False
    exitgame = False

    snake_init_x = 40
    snake_init_y = 50

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
    while not exitgame:
        if gameover:
            gamewindow.fill(black)
            text_screen("GAME OVER!", red, 100, 100)
            font = pygame.font.SysFont(None, 25)
            screen_text = font.render("Press Enter to HEAL the Ophidia", True, white)
            gamewindow.blit(screen_text, [100, 200])
            screen_text = font.render("Close to Window to push the Ophidia to HELL", True, white)
            gamewindow.blit(screen_text, [100, 300])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameover = False
                        game_loop()
        else:
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
            text_screen("FPS: " + str(round(fps + random.randint(1, 100)/random.randint(1, 100), 5)), red, width - 800, 5)
            text_screen("Velocity: " + str(round(velocity_counter, 3)), white, width - 280, 5)
            pygame.draw.circle(gamewindow, white, [food_x, food_y], 10)
            head = []
            head.append(snake_init_x)
            head.append(snake_init_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            if snake_init_x < 0:
                gameover = True
            if snake_init_y < 0:
                gameover = True
            if snake_init_y > height:
                gameover = True
            if snake_init_x > width:
                gameover = True
            if head in snake_list[:-1]:
                gameover = True
            plot_snake(gamewindow, red, snake_list, snake_length)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    exit()
game_loop()