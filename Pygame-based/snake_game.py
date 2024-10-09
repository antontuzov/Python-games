import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set display dimensions
WIDTH = 600
HEIGHT = 400

# Set up display
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Set game clock
clock = pygame.time.Clock()

# Snake properties
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Function to display score
def your_score(score):
    value = score_font.render(f"Your Score: {score}", True, YELLOW)
    dis.blit(value, [0, 0])


# Function to draw the snake
def our_snake(SNAKE_BLOCK, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], SNAKE_BLOCK, SNAKE_BLOCK])


# Message function
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [WIDTH / 6, HEIGHT / 3])


# The main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Snake movement
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # If the snake hits the boundaries of the game screen
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLUE)

        # Draw food
        pygame.draw.rect(dis, RED, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])

        # Add the new head of the snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for collision with self
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw snake and score
        our_snake(SNAKE_BLOCK, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


# Run the game loop
gameLoop()
