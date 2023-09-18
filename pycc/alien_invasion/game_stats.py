#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:55:24 2023

@author: matthew
"""


class GameStats:
    """Track stats for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize the statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        self.high_score = 0  # this should never be reset

        # Start the game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Re-initialize statistics that change throughout a game"""
        self.score = 0
        self.ships_left = self.settings.ship_limit
        self.level = 1
