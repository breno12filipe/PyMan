from .stageSelector import GameScenes


class StageProgressHandler:
    def __init__(self, game_stage_progress):
        self._game_stage_progress = game_stage_progress
        self._game_stage_progress_list = list(self._game_stage_progress)

    def _get_next_scene(self, current_key):
        try:
            next_value = self._game_stage_progress_list[
                self._game_stage_progress_list.index(current_key) + 1
            ]
        except (ValueError, IndexError):
            next_value = None

        return next_value

    def flip_game_stage_progress(self):
        for game_stage in self._game_stage_progress:
            if self._game_stage_progress[game_stage][0] is True:
                next_value = self._get_next_scene(game_stage)
                if next_value is not None:
                    self._game_stage_progress[game_stage][0] = False
                    # fmt: off
                    self._game_stage_progress[self._get_next_scene(game_stage)][0] = True
                    break

    def play_current_scene(self):
        for game_stage in self._game_stage_progress:
            if self._game_stage_progress[game_stage][0] is True:
                self._game_stage_progress[game_stage][1]()
