import pygame
import random
pygame.init()

snake_speed = 15

# Set the size of the "window"
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake game by David de Pear.H')

# Set name of colors
GREY = (120, 120, 120)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Snake default position
snake_position = [100, 50]

#fruit position
fruit_position = [random.randrange(1, (screen_width//10)) * 10,
				  random.randrange(1, (screen_height//10)) * 10]

create_fruit = True
#Fruit from Geeks for Geeks:)

# Snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]

#We have SCORE
Score = 0

# Show Score for you
def see_your_score(choice, color, font, size):

	#font object
	score_font = pygame.font.SysFont(font, size)

	#display surface object
	score_surface = score_font.render('Score: ' + str(Score), True, color)

	#rectangle object for the text
	score_rect = score_surface.get_rect()

	#read this text
	game_window.blit(score_surface, score_rect)

# Default direction
snake_direction = 'right'
change_to = snake_direction

# Set "game_over" turn on first
game_over = False

# Start running the program
while not game_over:
    screen.fill(GREY)

    # Event while running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Key events (Up, Down, Left, Right)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'up'
            if event.key == pygame.K_DOWN:
                change_to = 'down'
            if event.key == pygame.K_LEFT:
                change_to = 'left'
            if event.key == pygame.K_RIGHT:
                change_to = 'right'

    # Only one direction ok?
    if change_to == 'up' and snake_direction != 'down':
        snake_direction = 'up'
    if change_to == 'down' and snake_direction != 'up':
        snake_direction = 'down'
    if change_to == 'left' and snake_direction != 'right':
        snake_direction = 'left'
    if change_to == 'right' and snake_direction != 'left':
        snake_direction = 'right'

    # Move the snake
    if snake_direction == 'up':
        snake_position[1] -= 10
    if snake_direction == 'down':
        snake_position[1] += 10
    if snake_direction == 'left':
        snake_position[0] -= 10
    if snake_direction == 'right':
        snake_position[0] += 10

    #Draw fruits
    if create_fruit:
        pygame.draw.rect(screen, RED, pygame.rect(fruit_position[0], fruit_position[1], 10, 10))

    #Did he eat fruits?
    if snake_position == fruit_position:
        create_fruit = False
        fruit_position = [random.randrange(1, (screen_width//10)) * 10,
						  random.randrange(1, (screen_height//10)) * 10]
        create_fruit = True
        Score += 1

    #You have another head
        snake_body.insert(0, list(snake_position))

    # Update snake body
    snake_body.insert(0, list(snake_position))
    snake_body.pop()

	# Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    pygame.time.Clock().tick(snake_speed)

pygame.quit()