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
    for event in pygame.event.get(): #This will show all the movements, or in technical terms, events taking place inside the game window
        print(event)
pygame.quit()
exit()