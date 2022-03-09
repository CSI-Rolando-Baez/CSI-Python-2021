import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
# Names the created window the specified name.
pygame.display.set_caption('Snake game by Edureka')
# The game_over variable helps for later itirations of the code so that the game closes or restarts when lost. 
# For now it will be used so that the window does not close
game_over=False
#This loop makes it so the game does not close once it's opened
while not game_over:
    for event in pygame.event.get():
        print(event)   #prints out all the actions that take place on the screen
 
pygame.quit()
quit()