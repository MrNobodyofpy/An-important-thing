import pygame
pygame.init()

#Set the size of the "window"
screen = pygame.display.set_mode((800,700))

#Set name of colors : )
GREY = (120, 120, 120)
WHITE = (255,255,255)
BLACK = (0,0,0)

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

#Now this project will be completed by me.