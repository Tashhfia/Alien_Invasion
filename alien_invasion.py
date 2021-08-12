import sys
import pygame


class AlienInvasion:
    # initialize background settings
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1300, 900))
        pygame.display.set_caption("Attack of the Aliens")

    def run(self):
        while True:
            # checking for the events
            for event in pygame.event.get():
                # exits the game
                if event.type == pygame.QUIT:
                    sys.exit()