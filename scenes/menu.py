import pygame
from pygame.locals import *
from pygame import mixer
pygame.init()

width, height = 1280, 720
icon_path = pygame.image.load('../assets/sprites/megaman/megaman_jumping.png')
window = pygame.display.set_mode((width, height))

# Setting background image
bg_img = pygame.image.load('../assets/background_menu.png')
bg_img = pygame.transform.scale(bg_img, (width, height))

# Setting window Title
pygame.display.set_caption('Megaman II')

# Setting window icon
pygame.display.set_icon(icon_path)

# Setting menu song
mixer.init()
mixer.music.load(
    '../assets/sounds/Mega_Man_2_IntroTheme_Metal_Guitar_Cover_FamilyJules.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# Setting buttons images variables
difficult_btn = pygame.image.load('../assets/buttons/difficult.png')
normal_btn = pygame.image.load('../assets/buttons/normal.png')
arrow_btn = pygame.image.load('../assets/buttons/arrow.png')

# Other variables
transparent = (0, 0, 0, 0)
cursor_move_sound = pygame.mixer.Sound("../assets/sounds/cursor_move.wav")

running = True
# Render game objects
window.blit(bg_img, (0, 0))
window.blit(normal_btn, (400, 475))
window.blit(arrow_btn, (375, 470))
window.blit(difficult_btn, (400, 500))
# Game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # Switch beetwen menu options, when selected redraws
        # all scenario
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                window.fill(0)
                window.blit(bg_img, (0, 0))
                window.blit(normal_btn, (400, 475))
                window.blit(arrow_btn, (375, 500))
                window.blit(difficult_btn, (400, 500))
                pygame.mixer.Sound.play(cursor_move_sound)
            elif event.key == pygame.K_UP:
                window.fill(0)
                window.blit(bg_img, (0, 0))
                window.blit(normal_btn, (400, 475))
                window.blit(arrow_btn, (375, 470))
                window.blit(difficult_btn, (400, 500))
                pygame.mixer.Sound.play(cursor_move_sound)

    pygame.display.update()
pygame.quit()
