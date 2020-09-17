import sys
import pygame
from time import sleep
from utils import Direction, Keys
from models import Bullet, Alien
from settings import Settings

move_directions = {
        Keys.UP:    Direction.UP,
        Keys.DOWN:  Direction.DOWN,
        Keys.RIGHT: Direction.RIGHT,
        Keys.LEFT:  Direction.LEFT
    }

key_codes = [Keys.UP, Keys.SPACE, Keys.DOWN, Keys.RIGHT, Keys.LEFT]

def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key in key_codes:
        #ship.direction = move_directions[event.key]
        if event.key == Keys.UP:
            ship.direction_up = 1
        elif event.key == Keys.DOWN:
            ship.direction_down = 1
        elif event.key == Keys.RIGHT:
            ship.direction_right = 1
        elif event.key == Keys.LEFT:
            ship.direction_left = 1
        elif event.key == Keys.SPACE:
            fire_bullet(settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key in key_codes:
        #ship.direction = Direction.NONE
        if event.key == Keys.UP:
            ship.direction_up = 0
        elif event.key == Keys.DOWN:
            ship.direction_down = 0
        elif event.key == Keys.RIGHT:
            ship.direction_right = 0
        elif event.key == Keys.LEFT:
            ship.direction_left = 0


def check_events(settings, screen, sb, play_button, stats, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, sb, play_button, mouse_x, mouse_y, stats, ship, aliens, bullets)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            if event.key == Keys.ESC:
                sys.exit()
            else:
                check_keyup_events(event, ship)

def check_play_button(settings, screen, sb, play_button, mouse_x, mouse_y, stats, ship, aliens, bullets):
    """Start new game whin button clicked"""
    button_clicked = play_button._rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats._game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats._game_active = True
        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        sb.prep_score()
        sb.prep_ships()

def update_screen(settings, screen, sb, stats, ship, aliens, bullets, play_button):
    """Reset screen"""

    screen.fill(settings.BG_COLOR)

    sb.draw()

    if stats._game_active:
        for bullet in bullets.sprites():
            bullet.draw()

        ship.draw()
        aliens.draw(screen)
    else:
        play_button.draw()

    pygame.display.flip()


def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.BULLET_MAX_NUM:
                new_bullet = Bullet(screen, ship, settings.BULLET_SPEED, settings.BULLET_WIDTH, settings.BULLET_HEIGHT, settings.BULLET_COLOR)
                bullets.add(new_bullet)

def update_bullets(settings: Settings, screen, stats, sb, ship, aliens, bullets):
    """Update bullets"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet._rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets):
    # Check if a bullet hits an alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.ALIEN_POINTS * len(aliens)

        sb.prep_score()
        
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)
    #print(f"Bullets: {len(bullets)}")

def create_fleet(settings: Settings, screen, ship, aliens):
    """Create aliens fleet"""

    alien = Alien(screen, settings.ALIEN_SPEED_X, settings.ALIEN_DIRECTION)
    number_aliens_x = get_number_aliens_x(settings, alien._rect.width)
    number_rows = get_number_rows(settings, ship._rect.height, alien._rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(settings: Settings, alien_width):
    available_space_x = settings.SCREEN_WIDTH - 2 * alien_width
    return int(available_space_x / (2 * alien_width))


def get_number_rows(settings: Settings, ship_height, alien_height):
    available_space_y = (settings.SCREEN_HEIGHT - (5 * alien_height) - ship_height)
    return int(available_space_y / (2 * alien_height))


def create_alien(settings: Settings, screen, aliens, alien_number, row_number):
    alien = Alien(screen, settings.ALIEN_SPEED_X, settings.ALIEN_DIRECTION)
    alien_width = alien._rect.width
    alien._x = alien_width + 2 * alien_width * alien_number
    alien._rect.x = alien._x
    alien._rect.y = alien._rect.height + 2 * alien._rect.height * row_number
    aliens.add(alien)

def update_aliens(settings, screen, sb, stats, ship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()

    # Check if an alien hits a ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, screen, sb, stats, ship, aliens, bullets)

    check_aliens_bottom(settings, screen, sb, stats, ship, aliens, bullets)

def check_fleet_edges(settings: Settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien._rect.y += settings.ALIEN_SPEED_Y
        alien._move_direction *= -1

def ship_hit(settings: Settings, screen, sb, stats, ship, aliens, bullets):
    """Check if an alien hits the ship"""

    if stats._ships_left > 0:
        stats._ships_left -= 1

        sb.prep_ships()

        # Clear list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create new fleet and reset the ship at center of screen
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats._game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(settings: Settings, screen, sb, stats, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien._rect.bottom >= screen_rect.bottom:
            ship_hit(settings, screen, sb, stats, ship, aliens, bullets)
            break