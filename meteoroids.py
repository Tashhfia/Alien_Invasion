import pygame
from pygame.sprite import Sprite


class Meteoroid(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # loading image of meteoroid
        self.image = pygame.image.load('Images/meteroid1.bmp')
        self.rect = self.image.get_rect()

        # start every meteoroid in the top position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store horizontal position of meteoroid
        self.x = float(self.rect.x)
