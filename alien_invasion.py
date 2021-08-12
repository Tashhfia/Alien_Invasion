import sys
import pygame


class AlienInvasion:
    # initialize background settings
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1300, 900))
        pygame.display.set_caption("Attack of the Aliens")
