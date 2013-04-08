"""
Name: items.py
Version: 0.1
Author: BishopBlade

Item classes
"""

import pygame

import dragonengine

# HELMETS

# Add helmets here


# UPPER ARMOR

class TraineeWarriorsChestplate(pygame.sprite.Sprite):
    name = "Trainee Warrior's Chestplate"
    wdef = 1
    image = pygame.image.load("art/items/upper-armor/trainee-warriors-chestplate.png")


# LOWER ARMOR

class TraineeWarriorsLeggings(pygame.sprite.Sprite):
    name = "Trainee Warrior's Leggings"
    wdef = 1
    image = pygame.image.load("art/items/lower-armor/trainee-warriors-leggings.png")


# ROBES

class ApprenticeMagiciansRobes(pygame.sprite.Sprite):
    name = "Apprentice Magician's Robes"
    mdef = 1.5
    wdef = 0.2
    image = pygame.image.load("art/items/robes/apprentice-magicians-robes.png")


class TraineeRoguesRobes(pygame.sprite.Sprite):
    name = "Trainee Rogue's Robes"
    wdef = 1.25
    image = pygame.image.load("art/items/robes/trainee-rogues-robes.png")


# SWORDS

class TraineeWarriorsSword(pygame.sprite.Sprite):
    name = "Trainee Warrior's Sword"
    watk = 4
    image = pygame.image.load("art/items/weapons/swords/trainee-warriors-sword.png")


# SHIELDS

class TraineeWarriorsShield(pygame.sprite.Sprite):
    name = "Trainee Warrior's Shield"
    wdef = 1
    image = pygame.image.load("art/items/shields/trainee-warriors-shield.png")


# WANDS/STAFFS

class ApprenticeMagiciansWand(pygame.sprite.Sprite):
    name = "Apprentice Magician's Shield"
    matk = 3
    image = pygame.image.load("art/items/weapons/wands/apprentice-magicians-wand.png")


# DAGGERS

class TraineeRoguesDaggers(pygame.sprite.Sprite):
    name = "Trainee Rogue's Daggers"
    watk = 2.5
    image = pygame.image.load("art/items/weapons/wands/apprentice-magicians-wand.png")
