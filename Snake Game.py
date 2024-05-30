#Pygame is important
import pygame
import random
pygame.init()

snake_speed = 15

#Set the size of the "window"
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((800,700))
pygame.display.set_caption('Snake game by David de Pear.H')

#Set name of colors : )
GREY = (120, 120, 120)
GREEN = (0,128,0)
RED = (255, 0, 0)
WHITE = (255,255,255)
BLACK = (0,0,0)

#Set "game_over" turn on first : )
game_over = False

#Start running the program : )
while not game_over:
	screen.fill(GREY)

	#DEVELOPER only
	mouse_x, mouse_y = pygame.mouse.get_pos()

#Event while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True

	pygame.draw.rect(screen, GREEN, (377,304,35,35))
	pygame.display.update()
pygame.quit()