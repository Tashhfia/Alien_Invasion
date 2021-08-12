import sys
import pygame
from settings import Settings
from spaceShip import SpaceShip


class BattleOfTheGalaxies:
    # initialize background settings
    def __init__(self):
        pygame.init()
        # screen size
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        # title
        pygame.display.set_caption("BATTLE OF THE GALAXIES")
        self.spaceShip = SpaceShip(self)


    def run(self):
        while True:
            # checking for the events
            for event in pygame.event.get():
                # exits the game
                if event.type == pygame.QUIT:
                    sys.exit()

                # redraw screen through each pass of loop
                self.screen.fill(self.settings.bg_color)
                self.spaceShip.blitme()

                # making the most recent screen visible
                pygame.display.flip()


if __name__ == '__main__':
    ai = BattleOfTheGalaxies()
    ai.run()
