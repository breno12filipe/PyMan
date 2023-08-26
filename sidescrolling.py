import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Side Scroller")

# Cores
white = (255, 255, 255)

# Jogador
player_width = 50
player_height = 50
player_x = 50
player_y = screen_height - player_height
player_speed = 5

# Clock para controle de frames
clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Atualiza a tela
    screen.fill(white)
    pygame.draw.rect(
        screen, (0, 0, 255), (player_x, player_y, player_width, player_height)
    )
    pygame.display.flip()

    # Limita a taxa de atualização
    clock.tick(60)
