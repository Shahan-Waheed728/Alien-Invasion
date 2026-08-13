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
