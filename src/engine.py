"""
Name: engine.py
Version: 0.1
Author: BishopBlade
"""
import pygame
class Item(pygame.sprite.Sprite):
	def __init__(self, x, y):
		self.name = "Rock"
		self.rect = self.get_rect()
		self.rect.left = x
		self.rect.top = y
	def add_inv(self):
		player.inventory.append(self.name)
	def rm_inv(self):
		player.inventory.remove(self.name)
	def move(self, x, y):
		self.rect.left = x
		self.rect.top = y
class Weapon(Item):
	pass