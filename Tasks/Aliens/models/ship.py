import pygame
from pygame.sprite import Sprite
from utils.enums import Direction

class Ship(Sprite):

    def __init__(self, screen, speed = 1):
        """Init ship and its position"""
        super().__init__()
        self._screen = screen

        # Load a ship image and set rectangle
        self._image = pygame.image.load("images/ship.bmp")
        self._rect = self._image.get_rect()
        self._screen_rect = screen.get_rect()
        self._rect.centerx = self._screen_rect.centerx
        self._rect.bottom = self._screen_rect.bottom
        self._direction = Direction.NONE
        self._center_x = float(self._rect.centerx)
        self._center_y = float(self._rect.bottom)
        self._speed = speed
        self.direction_up = 0
        self.direction_down = 0
        self.direction_right = 0
        self.direction_left = 0
    
    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self, direction: Direction):
        if isinstance(direction, Direction):
            self._direction = direction
        else:
            self._direction = Direction.NONE

    @property
    def rect(self):
        return self._rect
        
    @property
    def image(self):
        return self._image

    def draw(self):
        """Draw a ship in position"""
        self._screen.blit(self._image, self._rect)
    
    def update(self):
        """Update a ship position"""
        #print(f"update: {self._direction}")
        """
        if self._direction == Direction.RIGHT:
            self.move_right()
        elif self._direction == Direction.LEFT:
            self.move_left()
        elif self._direction == Direction.UP:
            self.move_up()
        elif self._direction == Direction.DOWN:
            self.move_down()
        """
        if self.direction_up:
            self.move_up()
        if self.direction_down:
            self.move_down()
        if self.direction_left:
            self.move_left()
        if self.direction_right:
            self.move_right()
        
        self._rect.centerx = self._center_x
        self._rect.bottom = self._center_y

    def move_right(self):
        """Move ship to right"""
        if self._rect.right < self._screen_rect.right:
            self._center_x += self._speed

    def move_left(self):
        """Move ship to left"""
        if self._rect.left > self._screen_rect.left:
            self._center_x -= self._speed

    def move_up(self):
        """Move ship to up"""
        if self._rect.top > self._screen_rect.top:
            self._center_y -= self._speed

    def move_down(self):
        """Move ship to down"""
        if self._rect.bottom < self._screen_rect.bottom:
            self._center_y += self._speed

    def center_ship(self):
        """Set the ship to center and bottom of screen"""
        #self._rect.centerx = self._screen_rect.centerx
        #self._rect.bottom = self._screen_rect.bottom
        
        self._center_x = self._screen_rect.centerx
        self._center_y = float(self._screen_rect.bottom)