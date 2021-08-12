import sys
import pygame
from settings import Settings
from spaceShip import SpaceShip
from bullet import Bullet


class BattleOfTheGalaxies:
    # initialize background settings
    def __init__(self):
        pygame.init()
        # getting screen size from settings module
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        # full screen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        # setting the title of the game
        pygame.display.set_caption("BATTLE OF THE GALAXIES")
        self.spaceShip = SpaceShip(self)
        self.bullets = pygame.sprite.Group()
        self.isFullScreen = False

    def run(self):
        while True:
            # checking for the events
            self._check_events()
            self.spaceShip.update()
            self.bullets.update()
            self._update_screen()

            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _update_screen(self):
        """Updates the images on the screen and flips to new screen"""

        # redraw screen through each pass of loop
        self.screen.fill(self.settings.bg_color)
        self.spaceShip.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # making the most recent screen visible
        pygame.display.flip()

    def _check_events(self):
        """"Respond to keyboard and mouse events"""
        for event in pygame.event.get():
            # exits the game
            if event.type == pygame.QUIT:
                sys.exit()
            # Key is pressed
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            # key is released
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self,event):
        """"responding to key presses"""
        if event.key == pygame.K_RIGHT:
            self.spaceShip.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.spaceShip.moving_left = True
        # pressing q to exit
        elif event.key == pygame.K_q:
            sys.exit()
        # firing bullets with space
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

        # enter full screen
        elif event.key == pygame.K_f:
            if not self.isFullScreen:
                self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                self.settings.screen_width = self.screen.get_rect().width
                self.settings.screen_height = self.screen.get_rect().height
                self.isFullScreen = True
            # if self.isFullScreen:
            #     self.settings = Settings()
            #     self.screen = pygame.display.set_mode((self.settings.screen_width,
            #                                            self.settings.screen_height))
            #     self.isFullScreen = False

    def fire_bullet(self):
        """creating new bullet"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def check_keyup_events(self,event):
        """responding to key releases"""
        if event.key == pygame.K_RIGHT:
            self.spaceShip.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.spaceShip.moving_left = False


if __name__ == '__main__':
    ai = BattleOfTheGalaxies()
    ai.run()
