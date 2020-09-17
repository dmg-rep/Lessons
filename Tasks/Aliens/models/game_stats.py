class GameStats:
    """Game statistics"""
    def __init__(self, settings):
        self._settings = settings
        self._game_active = False
        self.reset_stats()

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def reset_stats(self):
        self._ships_left = self._settings.SHIP_LIMIT
        self._score = 0