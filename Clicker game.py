import pygame
pygame.init()

#Set the size of the "window"
window_width = 800
window_height = 700
screen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Clicker Game by David de Pear.H")

#Set name of colors : )
GREY = (120, 120, 120)
WHITE = (255,255,255)
BLACK = (0,0,0)

#game variables
Click_score = 0
Clicks = 0

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