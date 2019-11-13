import pygame
import sys
import os

class Platform:

	def __init__(self, x, y, image):
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
