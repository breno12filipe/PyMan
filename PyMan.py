import pygame
from scenes.menu import Menu, GameDifficultyLevels
from scenes.stageSelector import StageSelector

pygame.init()

mainMenuIsShown = False
gameDifficulty = None
clock = pygame.time.Clock()
mainMenu = Menu(pygame)
# stageSelector = StageSelector(pygame)


def showMainMenu():
    global mainMenuIsShown
    global mainMenu

    if mainMenuIsShown == False:
        mainMenuIsShown = True
    else:
        return mainMenu.run_events()


def setGameDifficulty():
    global mainMenu
    global gameDifficulty
    gameDifficulty = mainMenu.getGameDifficulty()


def showSceneSelectorMenu():
    global stageSelector

    stageSelector.runEvents()


def playSelectedScene():
    ...


while True:
    # showSceneSelectorMenu()
    showMainMenu()
    # if showMainMenu():
    # setGameDifficulty()
    # showSceneSelectorMenu()
    # playSelectedScene()

    pygame.display.update()

    clock.tick(60)
