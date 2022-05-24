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

# Handling Events
# Types of event in PyGame:
# QUIT              none
# ACTIVEEVENT       gain, state
# KEYDOWN           key, mod, unicode, scancode
# KEYUP             key, mod, unicode, scancode
# MOUSEMOTION       pos, rel, buttons, touch
# MOUSEBUTTONUP     pos, button, touch
# MOUSEBUTTONDOWN   pos, button, touch
# JOYAXISMOTION     joy (deprecated), instance_id, axis, value
# JOYBALLMOTION     joy (deprecated), instance_id, ball, rel
# JOYHATMOTION      joy (deprecated), instance_id, hat, value
# JOYBUTTONUP       joy (deprecated), instance_id, button
# JOYBUTTONDOWN     joy (deprecated), instance_id, button
# VIDEORESIZE       size, w, h
# VIDEOEXPOSE       none
# USEREVENT         code

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("->")
            if event.key == pygame.K_LEFT:
                print("<-")
pygame.quit()
exit()