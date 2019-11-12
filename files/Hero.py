import pygame
import random

class Hero(pygame.sprite.Sprite):

	def __init__(self, image, height, width, speed, health, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load()
		self.rect = self.image.get_rect()
		self.height = height
		self.speed = speed
		self.width= width
		self.health = health
		self.rect.x = x
		self.rect.y = y
		self.speed = 3
		self.health = 3 #How many lives do we want him having?
		self.change_x = 0
		self.change_y = 0
		self.direction = ""

	def move_left(self):
		self.change_x = -10
		self.direction = "L"
	def move_right(self):
		self.change_x = 10
		self.direction = "R"
	def jump(self): #going to have to fix this
		self.rect.y += self.speed
		self.rect.y -= self.speed

#def shout(self, enemy):

	def update():
		self.rect.x += self.change_x
		self.rect.y += self.change_y
		self.change_x = 0
		self.change_y = 0
