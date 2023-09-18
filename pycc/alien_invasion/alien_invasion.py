#!/usr/bin/python

import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


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

        self.run_count = 0

        # Set window title
        pygame.display.set_caption("Alien Invasion!")

        # Create stats
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Add the ship
        self.ship = Ship(self)

        # Create a bullet list
        self.bullets = pygame.sprite.Group()

        # Create an alien list
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main gameplay loop"""
        while True:
            self._check_events()

            if self.stats.game_active:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()

    def _check_keyup_events(self, event):
        """Method to respond to key releases"""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        """Start the game when the user clicks Play"""
        if not self.stats.game_active and self.play_button.rect.collidepoint(
            mouse_pos
        ):
            self._start_game()

    def _start_game(self):
        self.run_count += 1
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

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
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Check for bullets that have hit aliens
        # If True, remove bullet and alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        # Check for empty fleet, if so, create a new one
        if not self.aliens:
            # Destroy existing bullets, then create a new fleet
            self.bullets.empty()
            self._create_fleet()

            # Increase the level and difficulty
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

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

    def _check_aliens_bottom(self):
        """Check for aliens hitting the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # The same thing happens as a ship hit
                self._ship_hit()
                break

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # See if any aliens hit the bottom
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit"""
        if self.stats.ships_left > 0:
            # Decrement ships remaining
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Remove aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause for a moment
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

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

        # Draw the scoreboard
        self.sb.show_score()

        # Draw button if needed
        if not self.stats.game_active:
            self.play_button.draw_button()

        if not self.stats.game_active and self.run_count > 0:
            self.sb.show_game_over()
        # Make the most recently drawn screen visible (screen update)
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance then run the game
    ai = AlienInvasion()
    ai.run_game()
