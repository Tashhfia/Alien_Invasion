import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # loading image of alien
        self.image = pygame.image.load('Images/alien1.bmp')
        self.rect = self.image.get_rect()

        # start every alien in the top position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store horizontal position of alien
        self.x = float(self.rect.x)
