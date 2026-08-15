import pygame 
from pygame.sprite import Sprite
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self,ai_settings,screen):
        super().__init__()
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
    def blitme(self):
        # Draw the ship at it's current location 
        self.screen.blit(self.image,self.rect)
    def check_edges(self):
        """Return True if an alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
            """Move the aliens right or left."""
            self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
            self.rect.x = self.x