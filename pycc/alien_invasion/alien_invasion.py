#!/usr/bin/python

import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Primary class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        # Create the game screen
        # =============================================================================
        #         self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #         self.settings.screen_width = self.screen.get_rect().width
        #         self.settings.screen_height = self.screen.get_rect().height
        # =============================================================================
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Set window title
        pygame.display.set_caption("Alien Invasion!")

        # Add the ship
        self.ship = Ship(self)

        # Create a bullet list
        self.bullets = pygame.sprite.Group()

        # Create an alien list
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start the main gameplay loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Method to respond to keypresses"""
        if event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_d:
            # Move the ship right
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            # Move the ship left
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Method to respond to key releases"""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the list"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create a fleet of aliens"""
        # Make one alien, use it to find the
        # number of aliens for one row.
        alien = Alien(self)
        # self.aliens.add(alien)

        # Dimensions for a row of aliens
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        available_space_y = (
            self.settings.screen_height
            - (3 * alien_height)
            - self.ship.rect.height
        )
        number_rows = available_space_y // (2 * alien_height)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Create the full fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_bullets(self):
        """Update the position of the bullets and trim old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Remove off-screen bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens reach the edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet and change direction variable"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen(self):
        # Redraw the screen on each loop, set background color
        self.screen.fill(self.settings.bg_color)

        # Draw the ship
        self.ship.blitme()

        # Draw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw aliens
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible (screen update)
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance then run the game
    ai = AlienInvasion()
    ai.run_game()
