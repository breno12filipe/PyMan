import sys
from pygame.locals import *
from pygame import mixer
from enum import Enum


class GameDifficultyLevels(Enum):
    normal = 1
    hard = 2


class Menu:
    def __init__(self, pygame):
        self._pygame = pygame

        self._screen_width = 800
        self._screen_height = 600
        self._screen_size = (self._screen_width, self._screen_height)
        self._screen = self._pygame.display.set_mode(
            (self._screen_width, self._screen_height)
        )

        self._icon_path = self._pygame.image.load(
            "./assets/sprites/megaman/megaman_jumping.png"
        )

        self._background_image = self._pygame.image.load("./assets/background_menu.png")
        self._background_image = self._pygame.transform.scale(
            self._background_image, self._screen_size
        )

        self._difficult_button = self._pygame.image.load(
            "./assets/buttons/difficult.png"
        )
        self._normal_button = self._pygame.image.load("./assets/buttons/normal.png")
        self._arrow_button = self._pygame.image.load("./assets/buttons/arrow.png")
        self._cursor_move_sound = self._pygame.mixer.Sound(
            "./assets/sounds/cursor_move.wav"
        )
        self._game_difficulty = GameDifficultyLevels.normal

        # Setting pygame configurations and rendering images
        self._pygame.display.set_caption("Megaman II")
        self._pygame.display.set_icon(self._icon_path)

        self._pygame.mixer.init()
        self._pygame.mixer.music.load(
            "./assets/sounds/Mega_Man_2_IntroTheme_Metal_Guitar_Cover_FamilyJules.mp3"
        )
        self._pygame.mixer.music.set_volume(0.5)
        self._pygame.mixer.music.play(-1)

        self._screen.blit(self._background_image, (0, 0))
        self._screen.blit(self._normal_button, (400, 475))
        self._screen.blit(self._arrow_button, (375, 470))
        self._screen.blit(self._difficult_button, (400, 500))

    def __del__(self):
        self._pygame.mixer.quit()

    def _set_game_difficulty(self, game_difficulty):
        if self._game_difficulty != game_difficulty:
            self._pygame.mixer.Sound.play(self._cursor_move_sound)
            self._game_difficulty = game_difficulty

    def _draw_background_image(self):
        self._screen.blit(self._background_image, (0, 0))

    def _draw_normal_difficult_button(self):
        self._screen.blit(self._normal_button, (400, 475))

    def _draw_menu_arrow_button_according_to_difficulty(self):
        if self._game_difficulty == GameDifficultyLevels.normal:
            self._screen.blit(self._arrow_button, (375, 470))
        else:
            self._screen.blit(self._arrow_button, (375, 500))

    def _draw_difficult_difficult_button(self):
        self._screen.blit(self._difficult_button, (400, 500))

    def get_game_difficulty(self):
        return self._game_difficulty

    def run_events(self):
        self._draw_background_image()
        self._draw_normal_difficult_button()
        self._draw_menu_arrow_button_according_to_difficulty()
        self._draw_difficult_difficult_button()

        for event in self._pygame.event.get():
            if event.type == self._pygame.QUIT:
                self._pygame.quit()
                sys.exit()

            if event.type == self._pygame.KEYDOWN:
                if event.key == self._pygame.K_DOWN:
                    self._set_game_difficulty(GameDifficultyLevels.hard)

                elif event.key == self._pygame.K_UP:
                    self._set_game_difficulty(GameDifficultyLevels.normal)

                if event.key == self._pygame.K_RETURN:
                    return True
