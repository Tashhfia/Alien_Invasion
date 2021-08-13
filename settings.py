
class Settings:
    def __init__(self):
        # screen settings
        self.screen_width = 1300
        self.screen_height = 800
        self.bg_color = (1, 1, 59)

        # space ship settings
        self.spaceShip_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 112, 3)
        self.bullets_allowed = 4

        self.speed_up = 1.1
        self.score_increment = 1.5
        self.initialize_dynamic_settings

        # Alien settings
        self.fleet_drop_speed = 10

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.spaceShip_speed = 1.75
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.spaceShip_speed *= self.speed_up
        self.bullet_speed *= self.speed_up
        self.alien_speed *= self.speed_up
        # increase score with speed
        self.alien_points = int(self.alien_points * self.score_increment)

