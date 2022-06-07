import random
import sys
import pygame
from pygame.locals import *


FPS = 60
SCREENWIDTH = 1920
SCREENHEIGHT = 1080
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/flappybird_test.png'
BACKGROUND = 'gallery/sprites/WinterSunrise.jpg'
OBSTACLE = 'gallery/sprites/RRR.png'


def welcomeScreen():

    player_x = int(SCREENWIDTH / 5)
    player_y = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2)
    message_x = int(SCREENWIDTH / 2 - 100)
    message_y = int(SCREENHEIGHT / 2 - 50)

    while True:

        for event in pygame.event.get():

            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.QUIT()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_UP or event.key == K_SPACE):
                return

            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (player_x, player_y))
                SCREEN.blit(GAME_SPRITES['message'], (message_x, message_y))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def mainGame():
    score = 0
    player_x = int(SCREENWIDTH / 5)
    player_y = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2)

    # Create 2 obstacles for blitting on the screen
    obstacle1 = getRandomObs()
    obstacle2 = getRandomObs()

    # List of Upper Obstacles
    upper_obs = [{'x': SCREENWIDTH + 200, 'y': obstacle1[0]['y']},
                 {'x': SCREENWIDTH + 200 + SCREENWIDTH / 2, 'y': obstacle2[0]['y']}]

    # List of Lower Obstacles
    lower_obs = [{'x': SCREENWIDTH + 200, 'y': obstacle1[1]['y']},
                 {'x': SCREENWIDTH + 200 + SCREENWIDTH / 2, 'y': obstacle2[1]['y']}]

    # Now, the Environment Dynamics
    obstacle_velocity_x = -4  # Taken negative to make it move along left.
    player_velocity_y = -9  # Initial thrust upwards
    player_max_velocity_y = 10  # Downward Acceleration during motion
    player_acceleration_y = 1  # Initial Downward Acceleration

    player_velocity_flap = -10  # Velocity increment on each flap
    player_flapped = False  # It is true only when the bird is flapping

    while True:
        for event in pygame.event.get():

            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.QUIT()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_UP or event.key == K_SPACE):

                if player_y > 0:  # Denotes that the player is within screen
                    player_velocity_y = player_velocity_flap
                    player_flapped = True
                    GAME_SOUNDS['wing'].play()

        crashTest = isCollide(player_x, player_y, upper_obs, lower_obs)
        if crashTest:
            return

        # Check for Score
        playerMidPos = player_x + GAME_SPRITES['player'].get_width() / 2  # Middle Position Coordinate of the Player
        for obstacle in upper_obs:
            obsMidPos = obstacle['x'] + GAME_SPRITES['obstacle'][
                0].get_width() / 2  # Middle Position Coordinate of the Obstacle
            if obsMidPos <= playerMidPos < obsMidPos + 4:
                score = score + 1
                print(f"Your score is {score}")  # f string
                GAME_SOUNDS['point'].play()  # Once, score is incremented, play the sound

        if player_velocity_y < player_max_velocity_y and player_flapped == False:  # If the player velocity is within the bounded max_velocity range, and the bird isn't flapping, let the bird fall freely with predefined graient of descent, i.e, player_velocity_flap
            player_velocity_y = player_velocity_y + player_acceleration_y

        if player_flapped:  # This function makes sure that the effect of flap extends upto one iteration only
            player_flapped = False

        player_height = GAME_SPRITES['player'].get_height()
        player_y = player_y + min(player_velocity_y, SCREENHEIGHT - player_y - player_height)  # This function makes sure that the bird don't gravitate completely to the ground

        # Now, we will move the obstacles to the left
        for upperobs, lowerobs in zip(upper_obs, lower_obs):  # if a = [1, 2, 3] and b = [4, 5, 6], zip(a, b) = [(1, 4), (2, 5), (3, 6)]
            upperobs['x'] += obstacle_velocity_x
            lowerobs['x'] += obstacle_velocity_x
        # Now, since the obstacles are not motile, and all of them are moving towards the left (<-), at some instant of time, lets say, t, obstacle that was blitted at the first will find it's way out of the screen. In that case, we will have to give birth to a new obstacle, and pop off, or in simple words, remove the obstacle that went off the screen.
        if 0 < upper_obs[0]['x'] < 5:  # When the obstacle is about to depart, give birth to a new obstacle.....
            new_obs = getRandomObs()
            upper_obs.append(new_obs[0])
            lower_obs.append(new_obs[1])

        if upper_obs[0]['x'] < -GAME_SPRITES['obstacle'][0].get_width():  # When the obstacle has departed, pop it
            upper_obs.pop(0)
            lower_obs.pop(0)

        # Lets blit our sprites Now
        # the order, we will follow for blitting, is
        # 1. Background
        # 2. Obstacles
        # 3. Player, i.e, the Motu Bird :-)
        # 4. and finally, the numbers from 0 to 9 to display the score
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))  # Blitting the background
        for upperobs, lowerobs in zip(upper_obs, lower_obs):  # Blitting the obstacles
            SCREEN.blit(GAME_SPRITES['obstacle'][0], (upperobs['x'], upperobs['y']))
            SCREEN.blit(GAME_SPRITES['obstacle'][1], (lowerobs['x'], lowerobs['y']))

        SCREEN.blit(GAME_SPRITES['player'], (player_x, player_y))  # Blitting the player
        myDigits = [int(x) for x in list(str(score))]  # Blitting the digits
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        X_offset = (SCREENWIDTH - width) / 2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (X_offset, SCREENHEIGHT * 0.12))
            X_offset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(player_x, player_y, upper_obs, lower_obs):

    if player_y > SCREENHEIGHT or player_y < 0:
        GAME_SOUNDS['hit'].play()
        return True

    for obstacle in upper_obs:
        obstacle_height  = GAME_SPRITES['obstacle'][0].get_height()
        if (player_y < obstacle_height + obstacle['y'] - 115 and abs(player_x - obstacle['x'] * 10) < GAME_SPRITES['obstacle'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True

    for obstacle in lower_obs:
        if (player_y + GAME_SPRITES['player'].get_height() > obstacle['y']  + 115 and abs(player_x - obstacle['x'] * 10) < GAME_SPRITES['obstacle'][1].get_width()):
            GAME_SOUNDS['hit'].play()
            return True
    return False
def getRandomObs():
    # NOTE: In pygame, the coordinate system is different from what we are familiar with in Mathematics
    # O --------------------------------------------------- x
    # |
    # |
    # |
    # |
    # |
    # |
    # |
    # |
    # |
    # |
    # |
    # Y
    OBSHEIGHT = GAME_SPRITES['obstacle'][0].get_height()
    offset = SCREENHEIGHT / 3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT) - 1.2 * offset)  # Height of Lower Obstacle
    OBSTACLEWIDTH = SCREENWIDTH + 15
    y1 = OBSHEIGHT - y2 + offset  # Height of Upper Obstacle
    obstacle = [{'x': OBSTACLEWIDTH, 'y': -y1},
                {'x': OBSTACLEWIDTH, 'y': y2}]  # Note that, here the ObstacleHeight for Upper Obs is taken negative
    return obstacle


if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("FlappyBird")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )
    GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/banner.png').convert_alpha()
    GAME_SPRITES['obstacle'] = (pygame.transform.rotate(pygame.image.load(OBSTACLE).convert_alpha(), 180),
                                pygame.image.load(OBSTACLE).convert_alpha()
                                )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()  # Shows welcome screen to the user until he presses a button
        mainGame()  # This is the main game function
