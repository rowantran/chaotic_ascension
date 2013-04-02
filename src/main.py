"""
Name: main.py
Version: 0.1
Author: BishopBlade

Main executable file for Chaotic Ascension
"""
import dragonengine, pygame, sys
from pygame.locals import *
from items import *
from maps import *
from monsters import *

pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(0)

font1 = pygame.font.SysFont("Open Sans Light", 60)
cursor = pygame.image.load("art/misc/cursor.png")
logo = pygame.image.load("art/misc/logo.png")
menuclass = Menu()
tut1class = Tut1()

header1 = font1.render("Press ENTER to begin the game.", 1, (255, 255, 255))

fullscreen = True
screen = pygame.display.set_mode([1280, 800], FULLSCREEN)
pygame.display.set_caption("Chaotic Ascension")
current_map = menuclass


def menu():
    screen.blit(menuclass.bg, (0, 0))
    screen.blit(logo, (360, 50))
    screen.blit(header1, (340, 730))
    pygame.display.flip()


def tut1():
    screen.blit(tut1class.bg, (0, 0))
    pygame.display.flip()

while True:
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
            elif event.key == pygame.K_RETURN:
                if current_map == menuclass:
                    current_map = tut1class

    if current_map == menuclass:
        menu()
    elif current_map == tut1class:
        tut1()
    x, y = pygame.mouse.get_pos()
    x -= cursor.get_width()/2
    y -= cursor.get_height()/2
    screen.blit(cursor, (x, y))
    pygame.display.flip()
    