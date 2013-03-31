"""
Name: dragonengine.py
Version: 0.1
Author: BishopBlade
"""
import pygame, random
class Player(pygame.sprite.Sprite):
	def __init__(self, inventory):
		self.inventory = inventory
		self.hp = 100
		self.mhp = 100
		self.mp = 50
		self.mmp = 50
		if inventory["weapon"] == "Trainee's Sabre":
			self.watk = 5
			self.matk = 0
		elif inventory["weapon"] == "Beginner Rogue's Dual Blades":
			self.watk = 4
			self.matk = 0
		elif inventory["weapon"] == "Apprentice's Wand":
			self.watk = 0
			self.matk = 4
		self.wdef = 2
		self.mdef = 2
		self.avoid = 4
		self.speed = 5
		self.fire = 0
		self.aqua = 0
		self.lightning = 0
		self.earth = 0
		self.light = 0
		self.dark = 0

	def attack(self, target):
		damage = random.randint(self.watk, self.watk*1.5)
		crit = random.choice([True, False])
		if crit:
			damage = damage * 1.3
		target.hp -= damage
		
	def skill(skillname, target):
		# Temporary D:
		exec(skills[skillname])

class Item(pygame.sprite.Sprite):
	def __init__(self, x, y):
		self.name = "Item"
		self.rect = self.get_rect()
		self.rect.left = x
		self.rect.top = y
		self.watk = 0
		self.matk = 0
		self.wdef = 0
		self.mdef = 0
		self.fire = 0
		self.aqua = 0
		self.lightning = 0
		self.earth = 0
		self.light = 0
		self.dark = 0
		self.avoid = 0
		self.speed = 0
		self.mhp = 0
		self.mmp = 0

	def add_inv(self, player):
		player.inventory.append(self.name)

	def rm_inv(self, player):
		player.inventory.remove(self.name)

	def move(self, x, y):
		self.rect.left = x
		self.rect.top = y