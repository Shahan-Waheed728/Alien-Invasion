import sys 
import pygame 
def check_events(ship):
    """Respond to key pressess and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                # Move ship to the right
                ship.rect.centerx += 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
def update_screen(ai_settings,screen,ship):
    """Update image on screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #Make the most recently drawn display visible
    pygame.display.flip()