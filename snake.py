import pygame
import random

pygame.init()

# setup display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# colors 
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRID_COLOR = (40, 40, 40)

# snake and food
snake = [(width // 2, height // 2)]
direction = (0, 0)
food = (random.randint(0, width // 10 - 1) * 10, random.randint(0, height // 10 - 1) * 10)

# clock
clock = pygame.time.Clock()

# setup game loop
running = True
while running:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 10):
                direction = (0, -10)
            elif event.key == pygame.K_DOWN and direction != (0, -10):
                direction = (0, 10)
            elif event.key == pygame.K_LEFT and direction != (10, 0):
                direction = (-10, 0)
            elif event.key == pygame.K_RIGHT and direction != (-10, 0):
                direction = (10, 0)

    # move snake 
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    # check collision food
    if head == food:
        food = (random.randint(0, width // 10 - 1) * 10, random.randint(0, height // 10 - 1) * 10)
    else:
        snake.pop()

    # check collision itself
    if (
        head[0] < 0 or head[0] >= width or
        head[1] < 0 or head[1] >= height or
        head in snake[1:]
    ):
        running = False

    # clear window
    window.fill(BLACK)

    # draws grid
    for x in range(0, width, 10):
        pygame.draw.line(window, GRID_COLOR, (x, 0), (x, height))
    for y in range(0, height, 10):
        pygame.draw.line(window, GRID_COLOR, (0, y), (width, y))

    # draws snake
    for segment in snake:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], 10, 10))

    # draws food
    pygame.draw.rect(window, RED, (food[0], food[1], 10, 10))

    pygame.display.update()

    # limits framerate
    clock.tick(15)

pygame.quit()
