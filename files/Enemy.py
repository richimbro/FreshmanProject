import pygame
import sys
import os

class Enemy(pygame.sprite.Sprite):

	def __init__(self, x , y, image, height, width):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load()
		self.rect = self.image.get_rect()
		self.height = height
		self.speed = speed
		self.width= width
		self.health = health
		self.rect.x = x
		self.rect.y = y
		self.speed = 10
		self.health = 1

	def shoot(self): #adjust  this for tracking
		b = Bullet(self.hero.direction, self.hero.rect.centerx, self.hero.rect.centery)
		self.bullets.add(b)


	def jump(self):
		while True:
			self.rect.y += 5  #fix these variables based on size of obj later
			self.rect.y -= 5

	def move(self):
		while True:
			self.rect.x += 5 #same here
			self.rect.x -= 10
			self.rect.x += 10
