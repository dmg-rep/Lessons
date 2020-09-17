import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Alien"""

    def __init__(self, screen, speed, move_direction):
        super().__init__()
        self._screen = screen
        self._speed = speed
        self._move_direction = move_direction
        self._image = pygame.image.load("images/alien1.bmp")
        self._rect = self.image.get_rect()

        self._rect.x = self._rect.width
        self._rect.y = self._rect.height

        self._x = float(self._rect.x)

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect

    def draw(self):
        """Draw an alien"""
        self._screen.blit(self._image, self._rect)

    def set_move_direction(self, move_direction):
        self._move_direction = move_direction
        
    def update(self):
        """Move alien"""
        self._x += (self._speed * self._move_direction)
        self._rect.x = self._x

    def check_edges(self):
        """Returns True when an alien at the edge of screen"""
        screen_rect = self._screen.get_rect()
        if self._rect.right >= screen_rect.right:
            return True
        elif self._rect.left <= 0:
            return True
        return False