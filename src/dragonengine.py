"""
Name: dragonengine.py
Version: 0.1
Author: BishopBlade

Base component of framework
"""
import pygame, random
class Player(pygame.sprite.Sprite):
	"""
	A player
	"""
	def __init__(self, inventory, x, y):
		self.inventory = inventory
		self.image = pygame.image.load("player0.png")
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = x,y
		self.hp = 100
		self.mhp = 100
		self.mp = 50
		self.mmp = 50
		self.watk = 0
		self.matk = 0
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
	"""
	A base class for an item
	"""
	name = "Item"
	image = pygame.image.load("art/misc/cursor.png")
	rect = image.get_rect()
	watk = 0
	matk = 0
	wdef = 0
	mdef = 0
	fire = 0
	firedef = 0
	aqua = 0
	aquadef = 0
	lightning = 0
	lightningdef = 0
	earth = 0
	earthdef = 0
	light = 0
	lightdef = 0
	dark = 0
	darkdef = 0
	avoid = 0
	speed = 0
	mhp = 0
	mmp = 0
	def __init__(self, x, y):
		self.rect.left, self.rect.top = x,y

	def add_inv(self, player):
		player.inventory.append(self.name)

	def rm_inv(self, player):
		player.inventory.remove(self.name)

	def move(self, x, y):
		self.rect.left = x
		self.rect.top = y

class Monster(pygame.sprite.Sprite):
	"""
	An enemy
	"""
	def __init__(self, x, y):
		self.hp = 1
		self.damage = 1
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = x,y

	def attack(self, target):
		damage = random.randint(self.damage, self.damage*1.3)
		target.hp -= damage