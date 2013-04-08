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
FPS = 100
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


class NewGameClass(pygame.sprite.Sprite):
    def __init__(self):
        self.bg = pygame.image.load("art/backgrounds/newgame.png")

        self.preview1 = pygame.image.load("art/players/player1preview.png")
        self.preview2 = pygame.image.load("art/players/player2preview.png")
        self.preview3 = pygame.image.load("art/players/player1preview2.png")
        self.preview4 = pygame.image.load("art/players/player2preview2.png")

        self.class1 = pygame.image.load("art/players/class-warrior.png")
        self.class2 = pygame.image.load("art/players/class-magician.png")
        self.class3 = pygame.image.load("art/players/class-rogue.png")
        self.class4 = pygame.image.load("art/players/class-warrior2.png")
        self.class5 = pygame.image.load("art/players/class-magician2.png")
        self.class6 = pygame.image.load("art/players/class-rogue2.png")

        self.click1 = False
        self.click2 = False

        self.cclick1 = False
        self.cclick2 = False
        self.cclick3 = False

        self.id = "New game"

    def play(self):
        global current_map
        screen.blit(self.bg, (0, 0))
        if self.click1:
            screen.blit(self.preview3, (100, 200))
        else:
            screen.blit(self.preview1, (100, 200))
        if self.click2:
            screen.blit(self.preview4, (400, 200))
        else:
            screen.blit(self.preview2, (400, 200))
        if self.cclick1:
            screen.blit(self.class4, (930, 300))
        else:
            screen.blit(self.class1, (930, 300))
        if self.cclick2:
            screen.blit(self.class5, (1030, 300))
        else:
            screen.blit(self.class2, (1030, 300))
        if self.cclick3:
            screen.blit(self.class6, (1130, 300))
        else:
            screen.blit(self.class3, (1130, 300))
        pygame.display.flip()

    def create_file(self):
        avatar = False
        pclass = False
        if self.click1 is True:
            image = "art/players/player1.png"
            avatar = True
        elif self.click2 is True:
            image = "art/players/player2.png"
            avatar = True
        if self.cclick1 is True:
            inventory = ["Trainee Warrior's Chestplate", "Trainee Warrior's Leggings", "Trainee Warrior's Sword", "Trainee Warrior's Shield"]
            pclass = True
        elif self.cclick2 is True:
            inventory = ["Apprentice Magician's Robes", "Apprentice Magician's Wand"]
            pclass = True
        elif self.cclick3 is True:
            inventory = ["Trainee Rogue's Robes", "Trainee Rogue's Daggers"]
            pclass = True
        if avatar and pclass:
            save = dragonengine.Save(inventory, 100, 100, image, tut1)
            dragonengine.save(save, "file1.sav")
        else:
            if not avatar:
                print "Please select an avatar!"
            if not pclass:
                print "Please select a class!"


class LoadGameClass(pygame.sprite.Sprite):
    def __init__(self):
        self.id = "Load game"

    def play(self):
        global player
        player = dragonengine.load("file1.sav", maps)
        print player.inventory


class Tut1Class(pygame.sprite.Sprite):
    def __init__(self):
        self.id = "Tutorial 1"


clock = pygame.time.Clock()
font1 = pygame.font.SysFont("Open Sans Light", 60)      # Create font object
cursor = pygame.image.load("art/misc/cursor.png")       # Load cursor file
logo = pygame.image.load("art/misc/logo.png")       # Load logo file for menu


# Create instances of level classes
maps = []
menu = MenuClass()
newgame = NewGameClass()
loadgame = LoadGameClass()
tut1 = Tut1Class()
maps = [menu, newgame, loadgame, tut1]


# Render text
header1 = font1.render("Press ENTER to begin the game.", 1, (255, 255, 255))


# Initialize display
fullscreen = True
screen = pygame.display.set_mode(WINDOWSIZE, FULLSCREEN)
pygame.display.set_caption("Chaotic Ascension")
current_map = menu


# Start event loop
while True:
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
            elif event.key == pygame.K_RETURN:
                if current_map == newgame:
                    newgame.create_file()
        elif event.type == MOUSEBUTTONDOWN:
            if current_map == menu:
                x, y = pygame.mouse.get_pos()
                if x >= 600 and x <= 696 and y >= 200 and y <= 425:
                    menu.newpressed = True
                    current_map = newgame
                if x >= 600 and x <= 696 and y >= 500 and y <= 525:
                    menu.loadpressed = True
                    current_map = loadgame
            elif current_map == newgame:
                if x >= 100 and x <= 195 and y >= 200 and y <= 390:
                    newgame.click1 = True
                    newgame.click2 = False
                elif x >= 400 and x <= 495 and y >= 200 and y <= 390:
                    newgame.click1 = False
                    newgame.click2 = True
                elif x >= 930 and x <= 997 and y >= 300 and y <= 367:
                    newgame.cclick1 = True
                    newgame.cclick2 = False
                    newgame.cclick3 = False
                elif x >= 1030 and x <= 1097 and y >= 300 and y <= 367:
                    newgame.cclick1 = False
                    newgame.cclick2 = True
                    newgame.cclick3 = False
                elif x >= 1130 and x <= 1197 and y >= 300 and y <= 367:
                    newgame.cclick1 = False
                    newgame.cclick2 = False
                    newgame.cclick3 = True
    current_map.play()
    x, y = pygame.mouse.get_pos()
    x -= cursor.get_width()/2
    y -= cursor.get_height()/2
    screen.blit(cursor, (x, y))
    pygame.display.flip()
