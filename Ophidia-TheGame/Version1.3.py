import pygame
x = pygame.init()
# print(x)
gamewindow = pygame.display.set_mode((1000, 500)) # Creates the game window
pygame.display.set_caption("My First Game") # Gives title
# Game Specific Variables
gameover = False
exitgame = False
# Creating Game loop
while not exitgame:
    pass # This will create an infinite loop. Don't run it, it is just for tutorial
pygame.quit()
exit()