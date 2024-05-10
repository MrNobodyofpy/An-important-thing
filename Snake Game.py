#Pygame is important
import pygame
import random
pygame.init()

#Set the size of the "window"
screen = pygame.display.set_mode((800,700))

#Set name of colors : )
GREY = (120, 120, 120)
GREEN = (0,128,0)
RED = (255, 0, 0)

#Set "is_running" turn on first : )
is_running = True

#Start running the program : )
while is_running:
	screen.fill(GREY)

#Event while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False

	pygame.display.flip()
pygame.quit()
#Snake defualt position
snake_position = [0, 0]
#First snake body
#Snake's body
pygame.draw.rect(screen, GREEN, (100,50,50,50))