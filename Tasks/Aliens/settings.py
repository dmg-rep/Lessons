class Settings:
    # Application settings
    APP_NAME = "Aliens"

    # Screen settings
    IS_FULL_SCREEN = 0
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    BG_COLOR = (200, 200, 200)

    # Ship settings
    SHIP_SPEED = 1
    SHIP_LIMIT = 3

    # Bullet settings
    BULLET_SPEED = 2
    BULLET_WIDTH = 300
    BULLET_HEIGHT = 15
    BULLET_COLOR = (60, 60, 60)
    BULLET_MAX_NUM = 3

    # Alien settings
    ALIEN_SPEED_X = 1
    ALIEN_SPEED_Y = 10
    ALIEN_DIRECTION = 1 # 1 - right, -1 - left
    ALIEN_POINTS = 50