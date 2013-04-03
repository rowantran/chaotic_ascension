"""
Name: main.py
Version: 0.1
Author: BishopBlade

Main executable file for Chaotic Ascension
"""
import sys

import pygame
from pygame.locals import *

import dragonengine
from items import *
from maps import *
from monsters import *

pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()
font1 = pygame.font.SysFont("Open Sans Light", 60)
cursor = pygame.image.load("art/misc/cursor.png")
logo = pygame.image.load("art/misc/logo.png")
menu = MenuClass()
tut1 = Tut1Class()
newpressed = False
loadpressed = False
newgamebut = pygame.image.load("art/misc/newgame.png")
newgamepressedbut = pygame.image.load("art/misc/newgamepressed.png")
loadgamebut = pygame.image.load("art/misc/loadgame.png")
loadgamepressedbut = pygame.image.load("art/misc/loadgamepressed.png")

header1 = font1.render("Press ENTER to begin the game.", 1, (255, 255, 255))

fullscreen = True
screen = pygame.display.set_mode([1280, 800], FULLSCREEN)
pygame.display.set_caption("Chaotic Ascension")
current_map = menu


def levelmenu():
    global current_map
    screen.blit(menu.bg, (0, 0))
    screen.blit(logo, (360, 50))
    if newpressed is True:
        screen.blit(newgamepressedbut, (600, 400))
    else:
        screen.blit(newgamebut, (600, 400))
    if loadpressed is True:
        screen.blit(loadgamepressedbut, (600, 500))
    else:
        screen.blit(loadgamebut, (600, 500))
    pygame.display.flip()


def leveltut1():
    screen.blit(tut1.bg, (0, 0))
    pygame.display.flip()

while True:
    newpressed = False
    loadpressed = False
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

        elif event.type == KEYDOWN:
            if event.key == pygame.K_F11:
                if fullscreen is True:
                    pygame.display.set_mode([1280, 800])
                    fullscreen = False
                else:
                    pygame.display.set_mode([1280, 800], FULLSCREEN)
                    fullscreen = True
        elif event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x >= 600 and x <= 696 and y >= 400 and y <= 425:
                newpressed = True
                current_map = newgame
            if x >= 600 and x <= 696 and y >= 500 and y <= 525:
                loadpressed = True
    if current_map == menu:
        levelmenu()
    elif current_map == tut1:
        leveltut1()
    x, y = pygame.mouse.get_pos()
    x -= cursor.get_width()/2
    y -= cursor.get_height()/2
    screen.blit(cursor, (x, y))
    pygame.display.flip()
