import pygame
import time
import random

pygame.init()

snake_speed = 15

# Set the size of the window
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake game by David de Pear.H')

# Define colors
GREY = (120, 120, 120)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Snake default position
snake_position = [100, 50]

# Fruit position
fruit_position = [random.randrange(1, (screen_width//10)) * 10,
                  random.randrange(1, (screen_height//10)) * 10]

create_fruit = True

# Snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]

# Initial score
Score = 0

# Function to display the score
def see_your_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(Score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

# Default direction
snake_direction = 'right'
change_to = snake_direction

# Game over function
def game_over():
    over_font = pygame.font.SysFont('times new roman', 50)
    over_surface = over_font.render('Your score is: ' + str(Score) + '. Game Over!', True, WHITE)
    over_rect = over_surface.get_rect()
    over_rect.midtop = (screen_width/2, screen_height/4)
    screen.blit(over_surface, over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

# Main loop
while True:
    screen.fill(GREY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'up'
            if event.key == pygame.K_DOWN:
                change_to = 'down'
            if event.key == pygame.K_LEFT:
                change_to = 'left'
            if event.key == pygame.K_RIGHT:
                change_to = 'right'

    # Update the direction of the snake
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

    # Snake eats the fruit
    if snake_position == fruit_position:
        create_fruit = False
        fruit_position = [random.randrange(1, (screen_width//10)) * 10,
                          random.randrange(1, (screen_height//10)) * 10]
        create_fruit = True
        Score += 1
        snake_body.insert(0, list(snake_position))
    else:
        snake_body.insert(0, list(snake_position))
        snake_body.pop()

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the fruit
    if create_fruit:
        pygame.draw.rect(screen, RED, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Display the score
    see_your_score(None, WHITE, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    pygame.time.Clock().tick(snake_speed)

    #Snake touched itself?
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # Check for game over condition
    if snake_position[0] < 0 or snake_position[0] > screen_width-10 or \
       snake_position[1] < 0 or snake_position[1] > screen_height-10:
        game_over()
