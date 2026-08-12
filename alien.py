import pygame 
from pygame.sprite import Sprite
class Alien():
    """A class to represent a single alien in the fleet."""
    def __init__(self,ai_settings,screen):
        """Initialize the alien and set it's starting position."""
        self.screen = screen 
        self.ai_settings = ai_settings
        # Load the image and get it's rect
        self.image = pygame.image.load("images/alien.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(60,48))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new alien near the top left corner of screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien exact position
        self.x = float(self.rect.x)
        # # Movement Flag 
        # self.moving_right = False
        # self.moving_left = False
    # def update(self):
    #     # Update the ship position based on movement flag 
    #     # Update the ship's center value
    #     if self.moving_right and self.rect.right < self.screen_rect.right:
    #         self.center += self.ai_settings.ship_speed_factor
    #         # self.rect.centerx += 1
    #     if self.moving_left and self.rect.left > 0:
    #         self.center -= self.ai_settings.ship_speed_factor
    #         # self.rect.centerx -= 1
    #     # Update rect objects from self.center 
    #     self.rect.centerx = self.center
    def blitme(self):
        # Draw the ship at it's current location 
        self.screen.blit(self.image,self.rect)
