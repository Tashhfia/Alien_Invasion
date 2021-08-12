import pygame


class SpaceShip:
    """"A class to manage the behaviour of the player's space-ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # loading image of spaceship
        self.image = pygame.image.load('Images/4.bmp')
        self.rect = self.image.get_rect()

        # setting the starting point of the spaceship
        self.rect.midbottom = self.screen_rect.midbottom
        # spaceship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.spaceShip_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.spaceShip_speed
        self.rect.x = self.x


    def blitme(self):
        """"Function to draw the spaceship at its current location"""
        self.screen.blit(self.image, self.rect)
