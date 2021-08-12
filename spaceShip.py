import pygame


class SpaceShip:
    """"A class to manage the behaviour of the player's space-ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # loading image of spaceship
        self.image = pygame.image.load('Images/2.bmp')
        self.rect = self.image.get_rect()

        # setting the starting point of the spaceship
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """"Function to draw the spaceship at its current location"""
        self.screen.blit(self.image, self.rect)
