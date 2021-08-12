import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.spaceShip.rect.midtop

        # store bullet's position as decimal value
        self.y = float(self.rect.y)

    def update(self):
        """moving the bullet"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullets"""
        pygame.draw.rect(self.screen, self.color, self.rect)