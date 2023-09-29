import sys
import pygame

from settings import Settings
from player import Player
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        # Start the main loop for the game.
        while True:
            self._check_events()
            self.player.update()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)

    
    def _check_events(self): 
        # Respond to keypresses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_a:
            self.player.moving_left = False

    def _update_screen(self): 
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.player.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    ss = StellarSentry()
    ss.run_game()