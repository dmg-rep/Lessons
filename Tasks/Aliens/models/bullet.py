import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, ship, speed, width, height, color):
        super().__init__()
        self._screen = screen
        self._rect = pygame.Rect(0, 0, width, height)
        self._rect.centerx = ship._rect.centerx
        self._rect.top = ship._rect.top
        self._y = float(self._rect.y)
        self._color = color
        self._speed = speed
    
    @property
    def rect(self):
        return self._rect
        
    def update(self):
        """Move the bullet to top"""
        self._y -= self._speed
        self._rect.y = self._y
    
    def draw(self):
        """Drow the bullet to a screen"""
        pygame.draw.rect(self._screen, self._color, self._rect)