import sys

from gameObjects.player import Player
from gameObjects.ground import Ground
from gameObjects.background import Background


class AirMan:
    def __init__(self, pygame):
        self._pygame = pygame

        self._screen_width = 800
        self._screen_height = 600
        self._screen = self._pygame.display.set_mode(
            (self._screen_width, self._screen_height)
        )
        self._pygame.display.set_caption("Air Man")

        self._background = Background("assets/backgrounds/Background.png", self._screen)
        self._ground = Ground("assets/backgrounds/Ground.png", self._screen)
        self._ground_group = self._pygame.sprite.Group()
        self._ground_group.add(self._ground)

        self._player = Player(self._screen_width, self._ground_group)
        self._player_group = self._pygame.sprite.Group()

    def run_events(self):
        self._player.gravity_check()

        for event in self._pygame.event.get():
            if event.type == self._pygame.QUIT:
                self._pygame.quit()
                sys.exit()

            if event.type == self._pygame.MOUSEBUTTONDOWN:
                pass

            if event.type == self._pygame.KEYDOWN:
                if event.key == self._pygame.K_SPACE:
                    self._player.jump()
            if event.type == self._pygame.KEYUP:
                if event.key == self._pygame.K_LEFT or self._pygame.K_RIGHT:
                    self._player.image = self._pygame.image.load(
                        "assets/sprites/megaman/megaman_stand1.png"
                    )

        self._player.update()
        self._player.move()

        self._background.render()
        self._ground.render()

        self._screen.blit(self._player.image, self._player.rect)

        self._pygame.display.update()
