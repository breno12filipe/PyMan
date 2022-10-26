import pygame
from pygame.locals import *

vec = pygame.math.Vector2
ACC = 0.3


class Player(pygame.sprite.Sprite):
    def __init__(self, width, ground_group):
        super().__init__()
        self.image = pygame.image.load(
            './assets/sprites/megaman/megaman_stand1.png')
        self.rect = self.image.get_rect()

        # Position and direction
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0, 0)
        self.direction = "RIGHT"

        # Movement
        self.jumping = False
        self.running = False
        self.move_frame = 0

        self.fric = -0.10

        # Run animation for the RIGHT
        self.run_ani_R = [pygame.image.load("./assets/sprites/megaman/megaman_walking1-right.png"),
                          pygame.image.load(
                              "./assets/sprites/megaman/megaman_walking2-right.png"),
                          pygame.image.load("./assets/sprites/megaman/megaman_walking3-right.png")]

        # Run animation for the LEFT
        self.run_ani_L = [pygame.image.load("./assets/sprites/megaman/megaman_walking1-left.png"),
                          pygame.image.load(
                              "./assets/sprites/megaman/megaman_walking2-left.png"),
                          pygame.image.load("./assets/sprites/megaman/megaman_walking3-left.png")]

        self.width = width
        self.ground_group = ground_group

    def move(self):
        # Keep a constant acceleration of 0.5 in the downwards direction (gravity)
        self.acc = vec(0, 0.5)

        # Will set running to False if the player has slowed down to a certain extent
        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        # Returns the current key presses
        pressed_keys = pygame.key.get_pressed()

        # Accelerates the player in the direction of the key press
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        # Formulas to calculate velocity while accounting for friction
        self.acc.x += self.vel.x * self.fric
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values

        # This causes character warping from one point of the screen to the other
        if self.pos.x > self.width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.width

        self.rect.midbottom = self.pos  # Update rect with new pos

    def gravity_check(self):
        hits = pygame.sprite.spritecollide(self, self.ground_group, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False

    def update(self):
        # Return to base frame if at end of movement sequence
        if self.move_frame > 2:
            self.move_frame = 0
            return

        # Move the character to the next frame if conditions are met
        if self.jumping == False and self.running == True:
            if self.vel.x > 0:
                self.image = self.run_ani_R[self.move_frame]
                self.direction = "RIGHT"
            else:
                self.image = self.run_ani_L[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1

        # Returns to base frame if standing still and incorrect frame is showing
        if abs(self.vel.x) < 0.2 and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = pygame.image.load(
                    './assets/sprites/megaman/megaman_stand1.png')
            elif self.direction == "LEFT":
                self.image = pygame.image.load(
                    './assets/sprites/megaman/megaman_stand1.png')

    def attack(self):
        pass

    def jump(self):
        self.rect.x += 1

        # Check to see if payer is in contact with the ground
        hits = pygame.sprite.spritecollide(self, self.ground_group, False)

        self.rect.x -= 1

        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12
