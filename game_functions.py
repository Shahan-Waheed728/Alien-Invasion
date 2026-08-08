import sys 
import pygame 
def check_keydown_events(event,ship):
    """Respond to key pressess"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        # Move ship to the right
        ship.rect.centerx += 1
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        #Moving ship to the left
        ship.rect.centerx -= 1
def check_keyup_events(event,ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_events(ship):
    """Respond to key pressess and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)       
def update_screen(ai_settings,screen,ship):
    """Update image on screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #Make the most recently drawn display visible
    pygame.display.flip()