import pygame
from enum import Enum


# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
BLOCK_SIZE = 40
GRID_WIDTH = 10
GRID_HEIGHT = 16

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Block Renderer")


# Function to render the grid
def render_grid():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            # Calculate block position
            x = col * BLOCK_SIZE
            y = row * BLOCK_SIZE

            # Get block color based on row number
            if col % 2 == 0:
                if row % 2 == 0:
                    block_color = (255, 0, 0)
                else:
                    block_color = (0, 255, 0)
            else:
                if row % 2 == 0:
                    block_color = (0, 255, 0)
                else:
                    block_color = (255, 0, 0)

            # Draw block
            pygame.draw.rect(window, block_color, (x, y, BLOCK_SIZE, BLOCK_SIZE))


# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill((255, 255, 255))

    # Render the grid
    render_grid()

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
