import pygame
import random
from files import Platform

class Hero(pygame.sprite.Sprite):
	def __init__(self, image, height, width, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.height = height
		self.width= width
		self.rect.x = x
		self.rect.y = y
		self.health = 3 #How many lives do we want him having?
		self.change_x = 0
		self.change_y = 0
		self.direction = ""
		self.levelDetails = None

	def move_left(self):
		self.change_x = -10
		self.direction = "L"
	def move_right(self):
		self.change_x = 10
		self.direction = "R"
	def jump(self): #going to have to fix this
		if self.rect.bottom >= 480:
			self.change_y = -10

			''' #check out adding this code to the jump function to check if there is a platform
			self.rect.y += 2
        	platform_hit_list = pygame.sprite.spritecollide(self, self.level.Platform, False)
        	self.rect.y -= 2

        	# If it is ok to jump, set our speed upwards
        	if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
			'''
#def shout(self, enemy):

# this function was from the player class in pyscroller
	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35

		# See if we are on the ground.
		if self.rect.y >= 480 - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = 480 - self.rect.height

	def update(self):
		#updated a lot in this function, we have to work on the self.levels.platform
		#and make it work again, we can work on that tomorrow
		self.calc_grav()
		self.rect.x += self.change_x
		# See if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.Platform.platform_list, False)
		for block in block_hit_list:
		# set our right side to the left side of the item we hit
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
		 	# Otherwise if we are moving left, do the opposite.
		 		self.rect.left = block.rect.right
		self.rect.y += self.change_y

		# Check and see if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.Platform.platform_list, False)
		for block in block_hit_list:
		# Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
		# Stop our vertical movement
		self.change_y = 0
