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
WHITE = (255,255,255)
BLACK = (0,0,0)

#Set "is_running" turn on first : )
is_running = True

#Start running the program : )
while is_running:
	screen.fill(GREY)

	pygame.draw.rect(screen, GREEN, (100,50,35,35))
	pygame.draw.rect(screen, RED, (200,100,20,20))

#Event while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				#Get positon (DEVELOPER only)
				pos = pygame.mouse.get_pos()
				print(pos)

	pygame.display.flip()
pygame.quit()