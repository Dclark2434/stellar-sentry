import sys
import pygame

from settings import Settings
from player import Player

class StellarSentry:

    def __init__(self):
        # Initialize the game, and create game resources.
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stellar Sentry")

        self.player = Player(self)

    def run_game(self):
        # Start the main loop for the game.
        while True:
            self._check_events()
            self.player.update()
            self._update_screen()
            self.clock.tick(60)

    
    def _check_events(self): 
        # Respond to keypresses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.moving_right = True
                elif event.key == pygame.K_a:
                    self.player.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.moving_right = False
                elif event.key == pygame.K_a:
                    self.player.moving_left = False

    def _update_screen(self): 
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    ss = StellarSentry()
    ss.run_game()