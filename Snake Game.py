import pygame

pygame.init()

screen = pygame.display.set_mode((800,700))

GREY = (120, 120, 120)

is_running = True

while is_running:
	screen.fill(GREY)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False

	pygame.display.flip()
pygame.quit()