import pygame

class Player:
    # A class to manage the player.
    def __init__(self, ss_game):
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()
        

        self.image = pygame.image.load('art/player.bmp')
        self.rect = self.image.get_rect()

        # Start each new player at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.x += self.settings.player_speed
        if self.moving_left:
            self.x -= self.settings.player_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)