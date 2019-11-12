import pygame
import sys
import os

class Enemy:

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
        self.speed = 3
        self.health = 1

    def shoot(self):
		hello

	def jump(self):
		while True:
			self.rect.x += 5
			self.rect.y -= 5

	def move(self):
		while True:
			self.rect.x += 5
			self.rect.x -= 5
