import pygame.font
from pygame.sprite import Group
from models import Ship

class Scoreboard:
    def __init__(self, settings, screen, stats):
        self._screen = screen
        self._screen_rect = screen.get_rect()
        self._settings = settings
        self._stats = stats

        self._text_color = (30, 30, 30)
        self._font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self._stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self._score_image = self._font.render(score_str, True, self._text_color, self._settings.BG_COLOR)

        self._score_rect = self._score_image.get_rect()
        self._score_rect.right = self._screen_rect.right - 20
        self._score_rect.top = 20

    def prep_ships(self):
        self._ships = Group()
        for ship_number in range(self._stats._ships_left):
            ship = Ship(self._screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self._ships.add(ship)

    def draw(self):
        self._screen.blit(self._score_image, self._score_rect)
        self._ships.draw(self._screen)