import sys


class StageSelector:
    def __init__(self, pygame):
        self.pygame = pygame

        # Configurações da tela
        self.screen_width = 800
        self.screen_height = 600
        self.screen = self.pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )
        self.pygame.display.set_caption("Stage Selector")

        # Carregando a imagem do menu de seleção de estágio
        self.stageSelectMenu = pygame.image.load(
            "./assets/sprites/stageSelect/StageSelectMenu.png"
        )

        # Redimensiona a imagem de menu de seleção de estágio
        self.stageSelectMenu = self.pygame.transform.scale(
            self.stageSelectMenu, (self.screen_width, self.screen_height)
        )

        # Dicionário de cenas e coordenadas para desenho da borda de cada cena
        self.scenes = {
            "bubbleMan": self.pygame.Rect(120, 60, 150, 110),
            "airMan": self.pygame.Rect(325, 60, 150, 110),
            "quickMan": self.pygame.Rect(525, 60, 150, 110),
            "heatMan": self.pygame.Rect(120, 210, 150, 110),
            "drWilly": self.pygame.Rect(325, 210, 150, 110),
            "woodMan": self.pygame.Rect(525, 210, 150, 110),
            "metalMan": self.pygame.Rect(120, 360, 150, 110),
            "flashMan": self.pygame.Rect(325, 360, 150, 110),
            "crashMan": self.pygame.Rect(530, 360, 150, 110),
        }

        # Lógicas relacionadas à seleção de cena...

        # Cena atual
        self.currentSelectedScene = self.scenes["drWilly"]
        self.selectedSceneRow = 1
        self.selectedSceneCol = 1

        # Matriz de cenas mapeando e descrevendo corretamente o menu de seleção de cena
        # fmt: off
        self.scenesMatrix = [[self.scenes["bubbleMan"], self.scenes["airMan"], self.scenes["quickMan"],],
                            [self.scenes["heatMan"], self.scenes["drWilly"], self.scenes["woodMan"],],
                            [self.scenes["metalMan"], self.scenes["flashMan"], self.scenes["crashMan"],]]

        # Variáveis de controle do piscar da borda de seleção de cena
        self.visible = True
        # Intervalo de piscar em milissegundos
        self.blink_interval = 500
        self.last_blink_time = self.pygame.time.get_ticks()

    # Metodos relacionadas ao calculo da matriz de cenas...
    def findUpperNeighbor(self):
        if self.selectedSceneRow - 1 >= 0:
            self.currentSelectedScene = self.scenesMatrix[self.selectedSceneRow - 1][
                self.selectedSceneCol
            ]
            self.selectedSceneRow = self.selectedSceneRow - 1
            self.selectedSceneCol = self.selectedSceneCol

    def findBelowNeighbor(self):
        if self.selectedSceneRow + 1 < len(self.scenesMatrix):
            self.currentSelectedScene = self.scenesMatrix[self.selectedSceneRow + 1][
                self.selectedSceneCol
            ]
            self.selectedSceneRow = self.selectedSceneRow + 1
            self.selectedSceneCol = self.selectedSceneCol

    def findRightNeighbor(self):
        if self.selectedSceneCol + 1 < len(self.scenesMatrix[self.selectedSceneRow]):
            self.currentSelectedScene = self.scenesMatrix[self.selectedSceneRow][
                self.selectedSceneCol + 1
            ]
            self.selectedSceneRow = self.selectedSceneRow
            self.selectedSceneCol = self.selectedSceneCol + 1

    def findLeftNeighbor(self):
        if self.selectedSceneCol - 1 >= 0:
            self.currentSelectedScene = self.scenesMatrix[self.selectedSceneRow][
                self.selectedSceneCol - 1
            ]
            self.selectedSceneRow = self.selectedSceneRow
            self.selectedSceneCol = self.selectedSceneCol - 1

    def drawStageSelectMenu(self):
        self.screen.blit(self.stageSelectMenu, (0, 0))

    def blinkSelectedSceneBorder(self):
        current_time = self.pygame.time.get_ticks()

        # Verifica se é hora de piscar novamente
        if current_time - self.last_blink_time >= self.blink_interval:
            # Inverte a visibilidade
            self.visible = not self.visible
            # Atualiza o tempo do último piscar
            self.last_blink_time = current_time

        if self.visible:
            self.pygame.draw.rect(
                self.screen, (255, 0, 0), self.currentSelectedScene, width=5
            )

    def runEvents(self):
        self.drawStageSelectMenu()

        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.pygame.quit()
                sys.exit()

            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_UP:
                    self.findUpperNeighbor()
                elif event.key == self.pygame.K_DOWN:
                    self.findBelowNeighbor()
                elif event.key == self.pygame.K_RIGHT:
                    self.findRightNeighbor()
                elif event.key == self.pygame.K_LEFT:
                    self.findLeftNeighbor()
                elif event.key == self.pygame.K_RETURN:
                    return True

        self.blinkSelectedSceneBorder()

        self.pygame.display.flip()

        self.pygame.time.Clock().tick(60)
