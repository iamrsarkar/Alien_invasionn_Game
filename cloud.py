import pygame
from settings import Settings
from pygame.sprite import Sprite
import random
class Cloud(Sprite):

    "a class to manage the ship"
    def __init__(self, ai_game, position):
        self.screen = ai_game.screen
        self.settings = ai_game.settings  # Assuming settings has a cloud speed.

        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship cloud and get its rect.
        self.image = pygame.image.load('cloud.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

        # Start each new ship at the bottom center of the screen.
        if position == 'midleft':
            self.rect.midleft = self.screen_rect.midleft
        elif position == 'midright':
            self.rect.midright = self.screen_rect.midright
        elif position == 'topright':
            self.rect.topright = self.screen_rect.topright
        elif position == 'topleft':
            self.rect.topleft = self.screen_rect.topleft

    def update(self):
        self.y += self.settings.cloud_speed
        self.rect.y = self.y
        if self.rect.top > self.screen_rect.bottom:
            self.reset_position()
    def reset_position(self):
        """Reset the cloud's position to the top of the screen."""
        # Reset the cloud's y position back to the top and randomize its horizontal position.
        self.y = -self.rect.height  # Move the cloud just above the screen
        self.rect.y = self.y
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)

        # Optionally, reset the speed for variation.
        self.speed = random.uniform(1.0, 3.0)
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)