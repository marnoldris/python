#!/usr/bin/python

import pygame
import sys
from settings import Settings
from ship import Ship


class AlienInvasion:
    """ Primary class to manage game assets and behavior """

    def __init__(self):
        """ Initialize the game and create game resources """
        pygame.init()
        self.settings = Settings()

        # Create the game screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )

        # Set window title
        pygame.display.set_caption('Alien Invasion!')

        # Add the ship
        self.ship = Ship(self)

    def run_game(self):
        """ Start the main gameplay loop """
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_d:
                    # Move the ship right
                    self.ship.moving_right = True
                elif event.key == pygame.K_a:
                    # Move the ship left
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False

    def _update_screen(self):
        # Redraw the screen on each loop, set background color
        self.screen.fill(self.settings.bg_color)

        # Draw the ship
        self.ship.blitme()

        # Make the most recently drawn screen visible (screen update)
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance then run the game
    ai = AlienInvasion()
    ai.run_game()
