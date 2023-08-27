import sys
from pygame.locals import *
from pygame import mixer
from enum import Enum


class gameDifficultyLevels(Enum):
    normal = 1
    hard = 2


class Menu:
    def __init__(self, pygame):
        self.pygame = pygame

        self.icon_path = self.pygame.image.load(
            "./assets/sprites/megaman/megaman_jumping.png"
        )

        self.windowInfoObject = self.pygame.display.Info()
        self.windowSize = (
            self.windowInfoObject.current_w,
            self.windowInfoObject.current_h,
        )
        self.window = pygame.display.set_mode(self.windowSize)

        # Setting background image
        self.bg_img = self.pygame.image.load("./assets/background_menu.png")
        self.bg_img = self.pygame.transform.scale(self.bg_img, self.windowSize)

        # Setting window Title
        self.pygame.display.set_caption("Megaman II")

        # Setting window icon
        self.pygame.display.set_icon(self.icon_path)

        # Setting menu song
        mixer.init()
        mixer.music.load(
            "./assets/sounds/Mega_Man_2_IntroTheme_Metal_Guitar_Cover_FamilyJules.mp3"
        )
        mixer.music.set_volume(0.5)
        mixer.music.play(-1)

        # Setting buttons images variables
        self.difficult_btn = self.pygame.image.load("./assets/buttons/difficult.png")
        self.normal_btn = self.pygame.image.load("./assets/buttons/normal.png")
        self.arrow_btn = self.pygame.image.load("./assets/buttons/arrow.png")

        # Other variables
        self.transparent = (0, 0, 0, 0)
        self.cursor_move_sound = self.pygame.mixer.Sound(
            "./assets/sounds/cursor_move.wav"
        )

        # Render game objects
        self.window.blit(self.bg_img, (0, 0))
        self.window.blit(self.normal_btn, (400, 475))
        self.window.blit(self.arrow_btn, (375, 470))
        self.window.blit(self.difficult_btn, (400, 500))

        self.gameDifficulty = gameDifficultyLevels.normal

    def run(self):
        for event in self.pygame.event.get():
            # Switch beetwen menu options, when selected redraws
            # all scenario
            if event.type == self.pygame.QUIT:
                self.pygame.quit()
                sys.exit()
            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_DOWN:
                    self.window.fill(0)
                    self.window.blit(self.bg_img, (0, 0))
                    self.window.blit(self.normal_btn, (400, 475))
                    self.window.blit(self.arrow_btn, (375, 500))
                    self.window.blit(self.difficult_btn, (400, 500))

                    # call setGameDifficulty()
                    if self.gameDifficulty != gameDifficultyLevels.hard:
                        self.pygame.mixer.Sound.play(self.cursor_move_sound)
                        self.gameDifficulty = gameDifficultyLevels.hard

                elif event.key == self.pygame.K_UP:
                    self.window.fill(0)
                    self.window.blit(self.bg_img, (0, 0))
                    self.window.blit(self.normal_btn, (400, 475))
                    self.window.blit(self.arrow_btn, (375, 470))
                    self.window.blit(self.difficult_btn, (400, 500))

                    # call setGameDifficulty()
                    if self.gameDifficulty != gameDifficultyLevels.normal:
                        self.pygame.mixer.Sound.play(self.cursor_move_sound)
                        self.gameDifficulty = gameDifficultyLevels.normal

                elif event.key == self.pygame.K_RETURN:
                    return True

    def setGameDifficulty(self):
        ...

    def getGameDifficulty(self):
        return self.gameDifficulty
