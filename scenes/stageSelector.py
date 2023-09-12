import sys
from .gameScenes import GameScenes


class StageSelector:
    def __init__(self, pygame):
        self._pygame = pygame

        self._screen_width = 800
        self._screen_height = 600
        self._screen = self._pygame.display.set_mode(
            (self._screen_width, self._screen_height)
        )
        self._pygame.display.set_caption("Stage Selector")

        self._stage_select_menu = pygame.image.load(
            "./assets/sprites/stageSelect/StageSelectMenu.png"
        )

        self._stage_select_menu = self._pygame.transform.scale(
            self._stage_select_menu, (self._screen_width, self._screen_height)
        )

        self._scene_border_coordinates = {
            "bubbleMan": (self._pygame.Rect(120, 60, 150, 110), GameScenes.bubbleMan),
            "airMan": (self._pygame.Rect(325, 60, 150, 110), GameScenes.airMan),
            "quickMan": (self._pygame.Rect(525, 60, 150, 110), GameScenes.quickMan),
            "heatMan": (self._pygame.Rect(120, 210, 150, 110), GameScenes.heatMan),
            "drWilly": (self._pygame.Rect(325, 210, 150, 110), GameScenes.drWilly),
            "woodMan": (self._pygame.Rect(525, 210, 150, 110), GameScenes.woodMan),
            "metalMan": (self._pygame.Rect(120, 360, 150, 110), GameScenes.metalMan),
            "flashMan": (self._pygame.Rect(325, 360, 150, 110), GameScenes.flashMan),
            "crashMan": (self._pygame.Rect(530, 360, 150, 110), GameScenes.crashMan),
        }

        self._selected_scene = self._scene_border_coordinates["drWilly"]
        self._selected_scene_row = 1
        self._selected_scene_col = 1

        # fmt: off
        self._scene_border_coordinates_matrix = [[self._scene_border_coordinates["bubbleMan"], self._scene_border_coordinates["airMan"], self._scene_border_coordinates["quickMan"],],
                                                 [self._scene_border_coordinates["heatMan"], self._scene_border_coordinates["drWilly"], self._scene_border_coordinates["woodMan"],],
                                                 [self._scene_border_coordinates["metalMan"], self._scene_border_coordinates["flashMan"], self._scene_border_coordinates["crashMan"],]]

        self._is_selected_scene_border_visible = True
        self._scene_border_blink_interval = 500
        self._scene_border_last_blink_time = self._pygame.time.get_ticks()

    def _find_upper_matrix_neighbor(self):
        if self._selected_scene_row - 1 >= 0:
            # fmt: off
            self._selected_scene = self._scene_border_coordinates_matrix[self._selected_scene_row - 1][self._selected_scene_col]
            self._selected_scene_row = self._selected_scene_row - 1
            self._selected_scene_col = self._selected_scene_col

    def _find_below_matrix_neighbor(self):
        if self._selected_scene_row + 1 < len(self._scene_border_coordinates_matrix):
            # fmt: off
            self._selected_scene = self._scene_border_coordinates_matrix[self._selected_scene_row + 1][self._selected_scene_col]
            self._selected_scene_row = self._selected_scene_row + 1
            self._selected_scene_col = self._selected_scene_col

    def _find_right_matrix_neighbor(self):
        # fmt: off
        if self._selected_scene_col + 1 < len(self._scene_border_coordinates_matrix[self._selected_scene_row]):
            # fmt: off
            self._selected_scene = self._scene_border_coordinates_matrix[self._selected_scene_row][self._selected_scene_col + 1]
            self._selected_scene_row = self._selected_scene_row
            self._selected_scene_col = self._selected_scene_col + 1

    def _find_left_matrix_neighbor(self):
        if self._selected_scene_col - 1 >= 0:
            # fmt: off
            self._selected_scene = self._scene_border_coordinates_matrix[self._selected_scene_row][self._selected_scene_col - 1]
            self._selected_scene_row = self._selected_scene_row
            self._selected_scene_col = self._selected_scene_col - 1

    def _draw_stage_select_menu(self):
        self._screen.blit(self._stage_select_menu, (0, 0))

    def _blink_selected_scene_border(self):
        current_time = self._pygame.time.get_ticks()

        # Check if its time to blink again
        # fmt: off
        if (current_time - self._scene_border_last_blink_time >= self._scene_border_blink_interval):
            # inverts visibility
            self._is_selected_scene_border_visible = (
                not self._is_selected_scene_border_visible
            )
            # Update the last blink time
            self._scene_border_last_blink_time = current_time

        if self._is_selected_scene_border_visible:
            self._pygame.draw.rect(
                self._screen, (255, 0, 0), self._selected_scene[0], width=5
            )

    def get_selected_game_scene(self):
        return self._selected_scene[1]

    def run_events(self):
        self._draw_stage_select_menu()

        for event in self._pygame.event.get():
            if event.type == self._pygame.QUIT:
                self._pygame.quit()
                sys.exit()

            if event.type == self._pygame.KEYDOWN:
                if event.key == self._pygame.K_UP:
                    self._find_upper_matrix_neighbor()
                elif event.key == self._pygame.K_DOWN:
                    self._find_below_matrix_neighbor()
                elif event.key == self._pygame.K_RIGHT:
                    self._find_right_matrix_neighbor()
                elif event.key == self._pygame.K_LEFT:
                    self._find_left_matrix_neighbor()
                elif event.key == self._pygame.K_RETURN:
                    return True

        self._blink_selected_scene_border()

        self._pygame.display.flip()

        self._pygame.time.Clock().tick(60)
