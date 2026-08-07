import pygame 
class Ship():
    """Initialize the ship and set it's starting position."""
    def __init__(self,screen):
        self.screen = screen 
        # Load the image and get it's rect
        self.image = pygame.image.load("images/ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(60,48))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of screen 
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        # Draw the ship at it's current location 
        self.screen.blit(self.image,self.rect)
