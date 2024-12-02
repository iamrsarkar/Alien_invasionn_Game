import pygame
from settings import Settings
from pygame.sprite import Sprite
import random
# class Missile(Sprite):

#     "a class to manage the ship"
#     def __init__(self, ai_game, position):
#         self.screen = ai_game.screen
#         self.settings = ai_game.settings  # Assuming settings has a cloud speed.

#         self.screen_rect = ai_game.screen.get_rect()
#         # Load the cloud and get its rect.
#         self.image = pygame.image.load('missile.bmp')
#         self.rect = self.image.get_rect()
#         self.rect.x = self.rect.width
#         self.rect.y = self.rect.height
#         self.y = float(self.rect.y)

#         # Start each new ship at the bottom center of the screen.
#         if position == 'midleft':
#             self.rect.midleft = self.screen_rect.midleft
#         elif position == 'midright':
#             self.rect.midright = self.screen_rect.midright
#         elif position == 'topright':
#             self.rect.topright = self.screen_rect.topright
#         elif position == 'topleft':
#             self.rect.topleft = self.screen_rect.topleft

#     def update(self):
#         self.y += self.settings.missile_speed
#         self.rect.y = self.y
#         if self.rect.top > self.screen_rect.bottom:
#             self.reset_position()
#     def reset_position(self):
#         """Reset the cloud's position to the top of the screen."""
#         # Reset the cloud's y position back to the top and randomize its horizontal position.
#         self.y = -self.rect.height  # Move the cloud just above the screen
#         self.rect.y = self.y
#         self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)

#         # Optionally, reset the speed for variation.
#         #self.speed = random.uniform(1.0, 3.0)
    
#     def blitme(self):
#         """Draw the ship at its current location."""
#         self.screen.blit(self.image, self.rect)



# import pygame
# from pygame.sprite import Sprite

# class Missile(Sprite):
#     """A class to manage missiles fired from the clouds in Alien Invasion."""

#     def __init__(self, ai_game, position='topleft'):
#         """Initialize the missile and set its starting position."""
#         super().__init__()
#         self.screen = ai_game.screen
#         self.settings = ai_game.settings
#         self.color = (255, 0, 0)  # Red missile for visibility
        
#         # Load the missile image or create a simple rectangle for it
#         self.rect = pygame.Rect(0, 0, 3, 15)  # Width 3, height 15
#         self.speed = self.settings.missile_speed

#         # Set initial position based on the cloud position
#         if position == 'topleft':
#             self.rect.midtop = ai_game.cloud_topleft.rect.midbottom
#         elif position == 'topright':
#             self.rect.midtop = ai_game.cloud_topright.rect.midbottom
        
#         # Store the missile's vertical position as a float for fine movement.
#         self.y = float(self.rect.y)
    
#     def update(self):
#         """Move the missile down the screen."""
#         self.y += self.speed
#         self.rect.y = self.y

#     def blitime(self):
#         """Draw the missile to the screen."""
#         pygame.draw.rect(self.screen, self.color, self.rect)


class Missile:
    def __init__(self, ai_game, position):
        """Initialize the missile at a specific position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the missile image and set its rect.
        self.image = pygame.image.load('missile.bmp')
        self.rect = self.image.get_rect()

        # Fix the missile at a specific position.
        if position == 'topleft':
            self.rect.topleft = ai_game.screen.get_rect().topleft
        elif position == 'topright':
            self.rect.topright = ai_game.screen.get_rect().topright

    def blitime(self):
        """Draw the missile at its fixed location."""
        self.screen.blit(self.image, self.rect)
