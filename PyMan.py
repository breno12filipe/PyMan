import pygame
from scenes.menu import Menu, GameDifficultyLevels
from scenes.stageSelector import StageSelector, GameScenes

pygame.init()

is_main_menu_shown = True
game_difficulty = None
selected_scene = None
clock = pygame.time.Clock()
main_menu = Menu(pygame)
stage_selector = StageSelector(pygame)

while True:
    if is_main_menu_shown is not False:
        if main_menu.run_events():
            game_difficulty = main_menu.get_game_difficulty()
            is_main_menu_shown = False
            del main_menu

    if is_main_menu_shown is False:
        stage_selector.run_events()
        selected_scene = stage_selector.get_selected_game_scene()

    pygame.display.update()

    clock.tick(60)
