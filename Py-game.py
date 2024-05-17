import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the player
player_width = 50
player_height = 50
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10
player_speed = 5
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = 0
enemy_speed = 3
enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # Move the enemy
    enemy.y += enemy_speed
    if enemy.y > screen_height:
        enemy.y = 0
        enemy.x = random.randint(0, screen_width - enemy_width)

    # Check for collision
    if player.colliderect(enemy):
        running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player and enemy
    pygame.draw.rect(screen, BLACK, player)
    pygame.draw.rect(screen, BLACK, enemy)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
