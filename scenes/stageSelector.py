import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Sheet Example")

windowInfoObject = pygame.display.Info()
windowSize = (windowInfoObject.current_w, windowInfoObject.current_h)
window = pygame.display.set_mode(windowSize)

# Carregando a imagem de sprite sheet
stageSelectMenu = pygame.image.load("./assets/sprites/stageSelect/StageSelectMenu.png")

# Redimensionar a imagem de menu de seleção de estágio
stageSelectMenu = pygame.transform.scale(stageSelectMenu, windowSize)

scenes = {
    "bubbleMan": pygame.Rect(120, 60, 150, 110),
    "airMan": pygame.Rect(325, 60, 150, 110),
    "quickMan": pygame.Rect(525, 60, 150, 110),
    "heatMan": pygame.Rect(120, 210, 150, 110),
    "drWilly": pygame.Rect(325, 210, 150, 110),
    "woodMan": pygame.Rect(525, 210, 150, 110),
    "metalMan": pygame.Rect(120, 360, 150, 110),
    "flashMan": pygame.Rect(325, 360, 150, 110),
    "crashMan": pygame.Rect(530, 360, 150, 110),
}


# Lógicas relacionadas à seleção de cena...
# Cena atual
currentSelectedScene = scenes["drWilly"]
selectedSceneRow = 1
selectedSceneCol = 1

# fmt: off
scenesMatrix = [[scenes["bubbleMan"], scenes["airMan"], scenes["quickMan"],],
                [scenes["heatMan"], scenes["drWilly"], scenes["woodMan"],],
                [scenes["metalMan"], scenes["flashMan"], scenes["crashMan"],]]

# Funções relacionadas ao calculo da matriz de cenas...
def findUpperNeighbor():
    global currentSelectedScene
    global selectedSceneRow
    global selectedSceneCol

    if selectedSceneRow - 1 >= 0:
        currentSelectedScene = scenesMatrix[selectedSceneRow - 1][selectedSceneCol]
        selectedSceneRow = selectedSceneRow - 1
        selectedSceneCol = selectedSceneCol
    else:
        currentSelectedScene = None
        selectedSceneRow = None
        selectedSceneCol = None

def findBelowNeighbor():
    global currentSelectedScene
    global selectedSceneRow
    global selectedSceneCol

    if selectedSceneRow + 1 < len(scenesMatrix):
        currentSelectedScene = scenesMatrix[selectedSceneRow + 1][selectedSceneCol]
        selectedSceneRow = selectedSceneRow + 1
        selectedSceneCol = selectedSceneCol
    else:
        currentSelectedScene = None
        selectedSceneRow = None
        selectedSceneCol = None

def findRightNeighbor():
    global currentSelectedScene
    global selectedSceneRow
    global selectedSceneCol

    if selectedSceneCol + 1 < len(scenesMatrix[selectedSceneRow]):
        currentSelectedScene = scenesMatrix[selectedSceneRow][selectedSceneCol + 1]
        selectedSceneRow = selectedSceneRow
        selectedSceneCol = selectedSceneCol + 1
    else:
        currentSelectedScene = None
        selectedSceneRow = None
        selectedSceneCol = None

def findLeftNeighbor():
    global currentSelectedScene
    global selectedSceneRow
    global selectedSceneCol

    if selectedSceneCol - 1 >= 0:
        currentSelectedScene = scenesMatrix[selectedSceneRow][selectedSceneCol - 1]
        selectedSceneRow = selectedSceneRow
        selectedSceneCol = selectedSceneCol - 1
    else:
        currentSelectedScene = None
        selectedSceneRow = None
        selectedSceneCol = None

# Variáveis de controle do piscar
visible = True
blink_interval = 500  # Intervalo de piscar em milissegundos
last_blink_time = pygame.time.get_ticks()


# Loop principal
running = True
while running:
    # Limpa a tela
    screen.fill((0, 0, 0))

    # Desenha o Menu de seleção de estágio
    screen.blit(stageSelectMenu, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                findUpperNeighbor()
            elif event.key == pygame.K_DOWN:
                findBelowNeighbor()
            elif event.key == pygame.K_RIGHT:
                findRightNeighbor()
            elif event.key == pygame.K_LEFT:
                findLeftNeighbor()

        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()

    # Verifica se é hora de piscar novamente
    if current_time - last_blink_time >= blink_interval:
        visible = not visible  # Inverte a visibilidade
        last_blink_time = current_time  # Atualiza o tempo do último piscar

    if visible:
        pygame.draw.rect(screen, (255, 0, 0), currentSelectedScene, width=5)

    pygame.display.flip()  # Atualiza a tela
    pygame.time.Clock().tick(60)  # Limita a taxa de quadros

pygame.quit()
sys.exit()
