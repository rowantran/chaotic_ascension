import pygame




class NewGameClass(pygame.sprite.Sprite):
    def __init__(self):
        self.bg = pygame.image.load("art/backgrounds/newgame.png")
        self.id = "New game"


class LoadGameClass(pygame.sprite.Sprite):
    def __init__(self):
        self.bg = pygame.image.load("art/backgrounds/loadgame.png")
        self.id = "Load game"


class Tut1Class(pygame.sprite.Sprite):
    def __init__(self):
        self.bg = pygame.image.load("art/backgrounds/bgtut1.png")
        self.id = "Tutorial part I"
