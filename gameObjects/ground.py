import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, ground_sprite, display_surface):
        super().__init__()
        # "assets/backgrounds/Ground.png"
        self.image = pygame.image.load(ground_sprite)
        self.rect = self.image.get_rect(center=(350, 350))
        self.bgX1 = 0
        self.bgY1 = 285
        self.display_surface = display_surface

    def render(self):
        self.display_surface.blit(self.image, (self.bgX1, self.bgY1))
