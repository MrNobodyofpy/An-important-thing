import pygame

pygame.init()

# Set the size of the "window"
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Kim Jong Un Simulator by David de Pear.H")

# Set name of colors
GREY = (120, 120, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

button_image = pygame.image.load("Nuclear Button.png")

# Game variables
Click_score = 0
Clicks = 0

# Set "is_running" turn on first
is_running = True

# Define button_rect before the loop
button_rect = button_image.get_rect()
button_rect.center = (window_width // 2, window_height // 2)

# Start running the program
while is_running:
    screen.fill(GREY)

    # Event while running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Button click
            if button_rect.collidepoint(event.pos):
                Click_score += 1
                Clicks += 1

    # Draw time
    screen.blit(button_image, button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {Click_score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()