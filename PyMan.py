import pygame, sys
from scenes.menu import Menu, GameDifficultyLevels
from scenes.stageSelector import StageSelector, GameScenes
from scenes.stageProgressEngine import StageProgressEngine
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
    "air_man": [False, play_air_man_stage],
}
game_difficulty = None
selected_scene = None
clock = pygame.time.Clock()
main_menu = Menu(pygame)
stage_selector = StageSelector(pygame)
air_man = AirMan(pygame)
stage_progress_engine = StageProgressEngine(game_stage_progress)


def play_main_menu():
    global main_menu
    global game_difficulty
    global stage_progress_engine

    if main_menu.run_events():
        game_difficulty = main_menu.get_game_difficulty()
        del main_menu
        stage_progress_engine.flip_game_stage_progress()


def play_stage_selector():
    global stage_selector
    global selected_scene
    global stage_progress_engine

    if stage_selector.run_events():
        selected_scene = stage_selector.get_selected_game_scene()
        stage_progress_engine.flip_game_stage_progress()
        del stage_selector


def play_air_man_stage():
    global air_man

    air_man.run_events()


while True:
    stage_progress_engine.play_current_scene()
    pygame.display.update()
    clock.tick(60)
