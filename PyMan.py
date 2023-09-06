import pygame
from scenes.menu import Menu, GameDifficultyLevels
from scenes.stageSelector import StageSelector, GameScenes
from scenes.stageProgressEngine import StageProgressEngine

pygame.init()


# NOTE: Forward declaring functions
def play_main_menu():
    play_main_menu()


def play_stage_selector():
    play_stage_selector()


game_stage_progress = {
    "main_menu": [True, play_main_menu],
    "stage_selector": [False, play_stage_selector],
}
game_difficulty = None
selected_scene = None
clock = pygame.time.Clock()
main_menu = Menu(pygame)
stage_selector = StageSelector(pygame)
stage_progress_engine = StageProgressEngine(game_stage_progress)


def play_main_menu():
    global main_menu
    global game_difficulty
    global stage_progress_engine
    if main_menu.run_events():
        game_difficulty = main_menu.get_game_difficulty()
        stage_progress_engine.flip_game_stage_progress()
        del main_menu


def play_stage_selector():
    global stage_selector
    global selected_scene

    stage_selector.run_events()
    selected_scene = stage_selector.get_selected_game_scene()
    # del stage_selector


while True:
    stage_progress_engine.play_current_scene()

    pygame.display.update()

    clock.tick(60)
