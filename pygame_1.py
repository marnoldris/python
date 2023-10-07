#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:04:51 2023

@author: matthew
"""

import pygame
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up the window
window_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello World!')

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the fonts
basic_font = pygame.font.SysFont(None, 48)

# Set up the text
text = basic_font.render('Hello world!', True, WHITE, BLUE)
text_rect = text.get_rect()
text_rect.centerx = window_surface.get_rect().centerx
text_rect.centery = window_surface.get_rect().centery

# Draw the white background onto the surface
window_surface.fill(WHITE)

## END BOILERPLATE ?

# Draw a green polygon onto the surface
pygame.draw.polygon(window_surface, GREEN, ((146, 0), (291, 106),
                                            (236, 277), (56, 277), (0, 106))
                    )

# Draw some blue lines onto the surface
pygame.draw.line(window_surface, BLUE, (60, 60), (120, 60)
