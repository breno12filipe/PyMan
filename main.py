import pygame
from pygame.locals import *
from gameObjects.player import Player
from gameObjects.ground import Ground
from gameObjects.background import Background
import sys

pygame.init()  # Begin pygame

# Declaring variables to be used through the program
HEIGHT = 350
WIDTH = 700
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

# Create the display, meant to be global variable
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

background = Background("assets/backgrounds/Background.png", displaysurface)

ground = Ground("assets/backgrounds/Ground.png", displaysurface)
ground_group = pygame.sprite.Group()
ground_group.add(ground)

player = Player(WIDTH, ground_group)
Playergroup = pygame.sprite.Group()


# Game loop
while True:
    player.gravity_check()

    for event in pygame.event.get():
        # Will run when the close window button is clicked
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # For events that occur upon clicking the mouse (left click)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        # Event handling for a range of different key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player.image = pygame.image.load(
                    'assets/sprites/megaman/megaman_stand1.png')
                print("cheguei")
    # Player related functions
    player.update()
    player.move()

    # Display and Background related functions
    background.render()
    ground.render()

    # Rendering Player
    displaysurface.blit(player.image, player.rect)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
