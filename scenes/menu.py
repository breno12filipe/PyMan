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

        # Configurações de tela
        self.screen_width = 800
        self.screen_height = 600
        self.screenSize = (self.screen_width, self.screen_height)
        self.screen = self.pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )

        # Setting window Title
        self.pygame.display.set_caption("Megaman II")

        self.icon_path = self.pygame.image.load(
            "./assets/sprites/megaman/megaman_jumping.png"
        )

        # Setting background image
        self.bg_img = self.pygame.image.load("./assets/background_menu.png")
        self.bg_img = self.pygame.transform.scale(self.bg_img, self.screenSize)

        # Setting window icon
        self.pygame.display.set_icon(self.icon_path)

        # Setting menu song
        self.pygame.mixer.init()
        self.pygame.mixer.music.load(
            "./assets/sounds/Mega_Man_2_IntroTheme_Metal_Guitar_Cover_FamilyJules.mp3"
        )
        self.pygame.mixer.music.set_volume(0.5)
        self.pygame.mixer.music.play(-1)

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
        self.screen.blit(self.bg_img, (0, 0))
        self.screen.blit(self.normal_btn, (400, 475))
        self.screen.blit(self.arrow_btn, (375, 470))
        self.screen.blit(self.difficult_btn, (400, 500))

        self.gameDifficulty = gameDifficultyLevels.normal

    def setGameDifficulty(self, gameDifficulty):
        if self.gameDifficulty != gameDifficulty:
            self.pygame.mixer.Sound.play(self.cursor_move_sound)
            self.gameDifficulty = gameDifficulty

    def getGameDifficulty(self):
        return self.gameDifficulty

    def drawBackgroundImage(self):
        self.screen.blit(self.bg_img, (0, 0))

    def drawNormalDifficultyButtons(self):
        self.screen.blit(self.normal_btn, (400, 475))

    def drawMenuArrowButtonAccordingToDifficulty(self):
        if self.gameDifficulty == gameDifficultyLevels.normal:
            self.screen.blit(self.arrow_btn, (375, 470))
        else:
            self.screen.blit(self.arrow_btn, (375, 500))

    def drawDifficultButton(self):
        self.screen.blit(self.difficult_btn, (400, 500))

    def runEvents(self):
        self.drawBackgroundImage()
        self.drawNormalDifficultyButtons()
        self.drawMenuArrowButtonAccordingToDifficulty()
        self.drawDifficultButton()

        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.pygame.quit()
                sys.exit()

            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_DOWN:
                    self.setGameDifficulty(gameDifficultyLevels.hard)

                elif event.key == self.pygame.K_UP:
                    self.setGameDifficulty(gameDifficultyLevels.normal)

            if event.type == self.pygame.KEYUP:
                if event.key == self.pygame.K_RETURN:
                    return True
