import pygame.font

class Button:
    def __init__(self, settings, screen, msg):
        """Init button attributes"""
        self._screen = screen
        self._screen_rect = screen.get_rect()

        self._width, self._height = 200, 50
        self._button_color = (0, 255, 0)
        self._text_color = (255, 255, 255)
        self._font = pygame.font.SysFont(None, 48)

        self._rect = pygame.Rect(0, 0, self._width, self._height)
        self._rect.center = self._screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self._msg_image = self._font.render(msg, True, self._text_color, self._button_color)
        self._msg_image_rect = self._msg_image.get_rect()
        self._msg_image_rect.center = self._rect.center
    
    def draw(self):
        self._screen.fill(self._button_color, self._rect)
        self._screen.blit(self._msg_image, self._msg_image_rect)