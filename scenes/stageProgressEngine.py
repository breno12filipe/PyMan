class StageProgressEngine:
    def __init__(self, game_stage_progress):
        self._game_stage_progress = game_stage_progress

    def _get_next_value(self, current_key):
        temp = list(self._game_stage_progress)
        try:
            res = temp[temp.index(current_key) + 1]
        except (ValueError, IndexError):
            res = None

        return res

    def flip_game_stage_progress(self):
        for game_stage in self._game_stage_progress:
            if self._game_stage_progress[game_stage][0] is True:
                next_value = self._get_next_value(game_stage)
                if next_value is not None:
                    self._game_stage_progress[game_stage][0] = False
                    # fmt: off
                    self._game_stage_progress[self._get_next_value(game_stage)][0] = True

    def play_current_scene(self):
        for game_stage in self._game_stage_progress:
            if self._game_stage_progress[game_stage][0] is True:
                self._game_stage_progress[game_stage][1]()
