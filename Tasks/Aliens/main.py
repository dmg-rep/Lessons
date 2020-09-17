import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from models import Ship, GameStats, Scoreboard
from controls import Button

def setup_screen():
    return pygame.display.set_mode((0, 0), pygame.FULLSCREEN) \
            if Settings.IS_FULL_SCREEN \
            else pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))

def main():
    pygame.init()
    
    screen = setup_screen()

    pygame.display.set_caption(Settings.APP_NAME)

    play_button = Button(Settings, screen, "Play")

    stats = GameStats(Settings)
    sb = Scoreboard(Settings, screen, stats)
    ship = Ship(screen, Settings.SHIP_SPEED)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(Settings, screen, ship, aliens)

    while 1:
        gf.check_events(Settings, screen, sb, play_button, stats, ship, aliens, bullets)

        if stats._game_active:
            ship.update()
            gf.update_bullets(Settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(Settings, screen, sb, stats, ship, aliens, bullets)

        gf.update_screen(Settings, screen, sb, stats, ship, aliens, bullets, play_button)

if __name__ == "__main__":
    main()