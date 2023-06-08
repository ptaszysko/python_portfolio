import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 480
TILE_SIZE = 64
TILE_HEIGHT = TILE_SIZE // 2
TILE_WIDTH = TILE_SIZE
ISO_TILE_WIDTH = TILE_WIDTH
ISO_TILE_HEIGHT = TILE_HEIGHT

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define game objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE/2, TILE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
        self.image.fill(random.choice(["blue", "yellow"]))
        self.rect = self.image.get_rect()
        self.rect.x = ((x - y) * TILE_WIDTH // 2) + TILE_WIDTH * 5
        self.rect.y = ((x + y) * TILE_HEIGHT // 2) + TILE_HEIGHT * 2

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the sprites
all_sprites = pygame.sprite.Group()
tiles = pygame.sprite.Group()
for x in range(10):
    for y in range(10):
        tile = Tile(x, y)
        tiles.add(tile)
        all_sprites.add(tile)

player = Player()
all_sprites.add(player)

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.rect.x -= TILE_WIDTH // 2
                player.rect.y += TILE_HEIGHT // 2
            elif event.key == pygame.K_UP:
                player.rect.x += TILE_WIDTH // 2
                player.rect.y -= TILE_HEIGHT // 2
            elif event.key == pygame.K_LEFT:
                player.rect.x -= TILE_WIDTH // 2
                player.rect.y -= TILE_HEIGHT // 2
            elif event.key == pygame.K_RIGHT:
                player.rect.x += TILE_WIDTH // 2
                player.rect.y += TILE_HEIGHT // 2

    # Draw the scene
    screen.fill(BLACK)
    for tile in tiles:
        screen.blit(tile.image, tile.rect)
    screen.blit(player.image, player.rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
