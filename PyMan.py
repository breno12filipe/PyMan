import pygame, sys
from scenes.menu import Menu, GameDifficultyLevels
from scenes.stageSelector import StageSelector, GameScenes
from scenes.stageProgressHandler import StageProgressHandler
from scenes.airMan import AirMan

pygame.init()


# NOTE: Forward declaring functions
def play_main_menu():
    play_main_menu()


def play_stage_selector():
    play_stage_selector()


def play_air_man_stage():
    play_air_man_stage()


game_stage_progress = {
    "main_menu": [True, play_main_menu],
    "stage_selector": [False, play_stage_selector],
}

game_scenes_functions = {
    GameScenes.bubbleMan: ["bubbleMan", None],
    GameScenes.airMan: ["airMan", play_air_man_stage],
    GameScenes.quickMan: ["quickMan", None],
    GameScenes.heatMan: ["heatMan", None],
    GameScenes.drWilly: ["drWilly", None],
    GameScenes.woodMan: ["woodMan", None],
    GameScenes.metalMan: ["metalMan", None],
    GameScenes.flashMan: ["flashMan", None],
    GameScenes.crashMan: ["crashMan", None],
}
game_difficulty = None
selected_scene = None
clock = pygame.time.Clock()
main_menu = Menu(pygame)
stage_selector = StageSelector(pygame)
air_man = AirMan(pygame)
stage_progress_handler = StageProgressHandler(game_stage_progress)


def play_main_menu():
    global main_menu
    global game_difficulty
    global stage_progress_handler

    if main_menu.run_events():
        game_difficulty = main_menu.get_game_difficulty()
        del main_menu
        stage_progress_handler.flip_game_stage_progress_forward()


def play_stage_selector():
    global stage_selector
    global selected_scene
    global stage_progress_handler

    if stage_selector.run_events():
        selected_scene = stage_selector.get_selected_game_scene()
        del stage_selector


def play_air_man_stage():
    global air_man
    global selected_scene

    # If user won the scene...
    if air_man.run_events():
        selected_scene = None
        del air_man


def play_selected_scene():
    global selected_scene

    game_scenes_functions[selected_scene][1]()


while True:
    if selected_scene is None:
        stage_progress_handler.play_current_scene()
    else:
        play_selected_scene()
    pygame.display.update()
    clock.tick(60)
