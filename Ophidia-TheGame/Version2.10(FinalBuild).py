# Audio added
import pygame
from pygame.locals import *
from pygame import mixer
import random
mixer.init()
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
def text_screen_credits(text, color, x, y):
    font = pygame.font.SysFont('arial', 15)
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
def welcome_scr():
    exitgame = False
    while not exitgame:
        gamewindow.fill(black)
        text_screen("Ophidia - The Game", red, 100, 100)
        text_screen("Press Space to kickstart the Ophidia", white, 100, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mixer.music.load('music/bgm.wav')
                    mixer.music.play(100)
                    game_loop()
        pygame.display.update()
        clock.tick(60)
def game_loop():

    exitgame = False
    gameover = False

    snake_init_x = 100
    snake_init_y = 100

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
    with open("high_score.txt", "r") as f:
        highscore = f.read()
    while not exitgame:
        if gameover:
            with open("high_score.txt", "w") as f:
                f.write(str(highscore))
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
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        snake_init_velocity_x = velocity_counter
                        snake_init_velocity_y = 0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        snake_init_velocity_x = -velocity_counter
                        snake_init_velocity_y = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        snake_init_velocity_y = -velocity_counter
                        snake_init_velocity_x = 0
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        snake_init_velocity_y = velocity_counter
                        snake_init_velocity_x = 0
                    # CHEAT CODES
                    if event.key == pygame.K_1:
                        score += 1
                    # Score made using CHEAT CODE can't be added appended in the High Score data
            snake_init_x += snake_init_velocity_x
            snake_init_y += snake_init_velocity_y
            if abs(snake_init_x - food_x) < 20 and abs(snake_init_y - food_y) < 20:
                food_x = random.randint(100, width - 100)
                food_y = random.randint(100, height - 100)
                score = score + 1
                if score > int(highscore):
                    highscore = score
                velocity_counter *= 1.002
                snake_length = snake_length + 5
            gamewindow.fill(black)
            text_screen("Score: " + str(score), white, 5, 5)
            text_screen("Highest Score: " + str(highscore), white, 5 + 280, 5)
            text_screen("FPS: " + str(round(fps + random.randint(1, 100)/random.randint(1, 100), 5)), red, width - 650, 5)
            text_screen("Velocity: " + str(round(velocity_counter, 3)), white, width - 280, 5)
            text_screen_credits(" © Anurag Dutta", white, 1270, 750)
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

welcome_scr()