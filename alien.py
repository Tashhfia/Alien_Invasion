import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # loading image of alien
        self.image = pygame.image.load('Images/alien1.bmp')
        self.rect = self.image.get_rect()

        # start every alien in the top position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store horizontal position of alien
        self.x = float(self.rect.x)

    def update(self):
        """Moving the alien"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """True when alien is at edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

