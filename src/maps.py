import pygame

class Menu(pygame.sprite.Sprite):
    def __init__(self):
      self.bg = pygame.image.load("art/backgrounds/menu.png")
      self.id = "Menu"  

class Tut1(pygame.sprite.Sprite):
    def __init__(self):
        self.bg = pygame.image.load("art/backgrounds/bgtut1.png")
        self.id = "Tutorial part I"