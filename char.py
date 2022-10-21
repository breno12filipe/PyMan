import pygame, sys, math
from pygame.locals import *
# pyganim is still on testing, we're not sure if we are going
# to use it for the first version of the game
import pyganim

pygame.init()
windowSurface = pygame.display.set_mode((320, 240), 0, 32)
pygame.display.set_caption('Pyganim Basic Demo')

boltAnim = pyganim.PygAnimation([('assets\sprites\megaman\megaman_stand1.png', 900),
                                 ('assets\sprites\megaman\megaman_stand2.png', 900)])
boltAnim.play()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill((255, 255, 255))
    boltAnim.blit(windowSurface, (100, 50))
    pygame.display.update()
    #------------------------------------------------------------------------

    #------------------------------------------------------------------------

"""
import pygame, random
from pygame.locals import *
pygame.init()

# Global Variables
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
RED = (255, 0, 0)
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")

# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        #pygame.draw.rect(self.image,
        #                 color,
        #                 pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveBack(self, speed):
        self.rect.y -= speed * speed/10

all_sprites_list = pygame.sprite.Group()

playerCar = Sprite(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300


all_sprites_list.add(playerCar)

exit = True
clock = pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(10)
    # if keys[pygame.K_UP]:
    #     playerCar.moveBack(10)

    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
"""
