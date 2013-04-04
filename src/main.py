"""
Name: main.py
Version: 0.1
Author: BishopBlade

Main executable file for Chaotic Ascension
"""

# Imports
import sys

import pygame
from pygame.locals import *

import dragonengine
from items import *
from maps import *
from monsters import *


# Initialize basic things for Pygame
pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(0)


# Set constants
FPS = 60
WINDOWSIZE = [1280, 800]


# Level code
class MenuClass(pygame.sprite.Sprite):
    def __init__(self):
        self.bg = pygame.image.load("art/backgrounds/menu.png")
        self.id = "Menu"
        self.newpressed = False
        self.loadpressed = False
        self.ngbutton = pygame.image.load("art/misc/newgame.png")
        self.ngpressedbutton = pygame.image.load("art/misc/newgamepressed.png")
        self.lgbutton = pygame.image.load("art/misc/loadgame.png")
        self.lgpressedbutton = pygame.image.load("art/misc/loadgamepressed.png")

    def play(self):
        global current_map
        screen.blit(menu.bg, (0, 0))
        screen.blit(logo, (360, 50))
        if self.newpressed is True:
            screen.blit(self.ngpressedbutton, (600, 400))
        else:
            screen.blit(self.ngbutton, (600, 400))
        if self.loadpressed is True:
            screen.blit(self.lgpressedbutton, (600, 500))
        else:
            screen.blit(self.lgbutton, (600, 500))
        pygame.display.flip()


clock = pygame.time.Clock()
font1 = pygame.font.SysFont("Open Sans Light", 60)      # Create font object
cursor = pygame.image.load("art/misc/cursor.png")       # Load cursor file
logo = pygame.image.load("art/misc/logo.png")       # Load logo file for menu


# Create instances of level classes
menu = MenuClass()
#newgame = NewGameClass()
#tut1 = Tut1Class()


# Render text
header1 = font1.render("Press ENTER to begin the game.", 1, (255, 255, 255))


# Initialize display
fullscreen = True
screen = pygame.display.set_mode(WINDOWSIZE, FULLSCREEN)
pygame.display.set_caption("Chaotic Ascension")
current_map = menu


# Start event loop
while True:
    newpressed = False
    loadpressed = False
    clock.tick(FPS)         # Run main loop 60 times every second
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

        elif event.type == KEYDOWN:
            if event.key == pygame.K_F11:
                if fullscreen is True:
                    pygame.display.set_mode([1280, 800])        # Set to windowed mode
                    fullscreen = False
                else:
                    pygame.display.set_mode([1280, 800], FULLSCREEN)        # Set to fullscreen
                    fullscreen = True

        elif event.type == MOUSEBUTTONDOWN:
            if current_map == menu:
                x, y = pygame.mouse.get_pos()
                if x >= 600 and x <= 696 and y >= 400 and y <= 425:
                    menu.newpressed = True
                    current_map = newgame
                if x >= 600 and x <= 696 and y >= 500 and y <= 525:
                    menu.loadpressed = True
                    current_map = loadgame
    current_map.play()
    x, y = pygame.mouse.get_pos()
    x -= cursor.get_width()/2
    y -= cursor.get_height()/2
    screen.blit(cursor, (x, y))
    pygame.display.flip()
