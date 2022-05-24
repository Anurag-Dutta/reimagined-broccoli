import pygame
x = pygame.init()
# print(x)
gamewindow = pygame.display.set_mode((1000, 1000)) # Creates the game window
pygame.display.set_caption("My First Game") # Gives title
# Game Specific Variables
gameover = False
exitgame = False