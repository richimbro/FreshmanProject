import pygame
import sys
import os

class Platform(pygame.sprite.Sprite):

	def __init__(self, x, y, image, width=100, height=100):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.image.load(os.path.join('images',image)).convert()
		#Please explain this to me when you see it, going to use same image load
		#that hero has for now.
		self.image = pygame.image.load(image)
		#self.image.convert_alpha()
		#self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
		self.width = width
		self.height = height

		#make every title the same with width and height and just plug a
		#platform in at  the desired x and y
