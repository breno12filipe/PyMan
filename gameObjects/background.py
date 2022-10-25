import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, ground_sprite, display_surface):
        super().__init__()
        # "assets/backgrounds/Background.png"
        self.bgimage = pygame.image.load(ground_sprite)
        self.rectBGimg = self.bgimage.get_rect()
        self.bgY = 0
        self.bgX = 0
        self.display_surface = display_surface

    def render(self):
        self.display_surface.blit(self.bgimage, (self.bgX, self.bgY))
