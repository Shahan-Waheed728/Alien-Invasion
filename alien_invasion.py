import pygame 
from settings import Settings
from ship import Ship 
import game_functions as gf 
def run_game():
    pygame.init()
    """Initialize pygame,settings and screen objects."""
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(("Alien Invasion"))
    # # set the background color 
    # bg_color = ((24,24,43))
    # Make a ship 
    ship = Ship(screen)
    # Start the loop for game 
    while True:
        gf.check_events(ship)  
        ship.update()      
        gf.update_screen(ai_settings,screen,ship)   
run_game()

        