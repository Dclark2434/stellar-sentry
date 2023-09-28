import sys
import pygame

from settings import Settings
from player import Player

class StellarSentry:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stellar Sentry")

        self.player = Player(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.player.blitme()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ss = StellarSentry()
    ss.run_game()