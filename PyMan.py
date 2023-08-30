import pygame
from scenes.menu import Menu, gameDifficultyLevels
from scenes.stageSelector import StageSelector

pygame.init()

mainMenuIsShown = False
gameDifficulty = None
clock = pygame.time.Clock()
mainMenu = Menu(pygame)


def showMainMenu():
    global mainMenuIsShown
    global mainMenu
    if mainMenuIsShown == False:
        mainMenuIsShown = True
    else:
        return mainMenu.run()


def setGameDifficulty():
    global mainMenu
    global gameDifficulty
    gameDifficulty = mainMenu.getGameDifficulty()


def showSceneSelectorMenu():
    ...


def playSelectedScene():
    ...


while True:
    showMainMenu()
    setGameDifficulty()
    showSceneSelectorMenu()
    playSelectedScene()

    pygame.display.update()

    clock.tick(60)
