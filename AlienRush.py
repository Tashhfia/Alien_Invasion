import sys
from time import sleep

import pygame

from settings import Settings
from spaceShip import SpaceShip
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


class AlienRush:
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
        pygame.display.set_caption("Alien Rush")
        # game stats instance
        self.stats = GameStats(self)
        # adding spaceship
        self.spaceShip = SpaceShip(self)
        # adding bullets
        self.bullets = pygame.sprite.Group()
        # adding aliens
        self.aliens = pygame.sprite.Group()
        self.create_alien_fleet()

        self.isFullScreen = False

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

    def check_keyup_events(self,event):
        """responding to key releases"""
        if event.key == pygame.K_RIGHT:
            self.spaceShip.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.spaceShip.moving_left = False

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

    def run(self):
        while True:
            # checking for the events
            self._check_events()
            if self.stats.game_active:
                self.spaceShip.update()
                self.update_bullets()
                self.update_aliens()

            self._update_screen()

    def _update_screen(self):
        """Updates the images on the screen and flips to new screen"""

        # redraw screen through each pass of loop
        self.screen.fill(self.settings.bg_color)
        self.spaceShip.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # making the most recent screen visible
        pygame.display.flip()

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_bullet_alien_collision()

    def check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self.create_alien_fleet()

    def fire_bullet(self):
        """creating new bullet"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def create_alien_fleet(self):
        """Creates a fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width\
                            - (2 * alien_width)
        total_aliens_x = available_space_x \
                       // (2 * alien_width)

        # determining number of rows
        spaceShip_height = self.spaceShip.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - spaceShip_height)
        total_rows = available_space_y // (2 * alien_height)

        # creating row of aliens
        for row_num in range(total_rows):
            for alien_num in range(total_aliens_x):
                self.alien_fleet(alien_num, row_num)

    def alien_fleet(self, alien_num, row_num):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.x = alien_width + (2 * alien_width * alien_num)
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
        self.aliens.add(alien)

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """change fleet direction and descend"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def update_aliens(self):
        """checks edges first and then updates position"""
        self.check_fleet_edges()
        self.aliens.update()

        # Looking for alien and spaceship collision
        if pygame.sprite.spritecollideany(self.spaceShip, self.aliens):
            self.spaceShip_hit()
        self.check_aliens_bottom()

    def spaceShip_hit(self):
        if self.stats.spaceShips_left > 0:
            self.stats.spaceShips_left -= 1
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            self.create_alien_fleet()
            self.spaceShip.center_spaceShip()
            sleep(.6)  # pause
        else:
            self.stats.game_active = False

    def check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.spaceShip_hit()
                break


if __name__ == '__main__':
    ai = AlienRush()
    ai.run()
