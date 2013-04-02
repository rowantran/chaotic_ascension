"""
Name: items.py
Version: 0.1
Author: BishopBlade

Item classes
"""

import dragonengine, pygame

# HELMETS
class BaseballCap(dragonengine.Item):
    name = "Baseball Cap"
    image = pygame.image.load("art/items/baseball-cap.png")
    wdef = 0.2
class Beanie(dragonengine.Item):
    name = "Beanie"
    image = pygame.image.load("art/items/beanie.png")