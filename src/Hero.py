import pygame
import random

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
		self.jumpcounter = 0
		self.direction = ""
		self.hitList = []
		self.isTouchingdoor = False
		self.dead = False


	def checkCollide(self, platforms, door,lava):
		'''checks if the Hero collides  with a platform'''
		self.hitList = []
		for tile in platforms:
			if self.rect.colliderect(tile):
					self.hitList.append(tile)
		if self.rect.colliderect(door):
			self.isTouchingdoor = True
		for tile in lava:
			if self.rect.colliderect(tile):
					self.dead = True


	'''these functions allow a player to move left/right and jump in  a level'''
	def move_left(self):
		self.change_x = -10
		self.direction = "L"
	def move_right(self):
		self.change_x = 10
		self.direction = "R"
	def jump(self,platforms, door, lava): #going to have to fix this

		self.rect.y += 2
		self.checkCollide(platforms, door, lava)
		self.rect.y -= 2

		# If it is ok to jump, set our speed upwards
		if len(self.hitList) > 0 or self.rect.bottom >= 800:
			self.change_y = -20

#def shout(self, enemy):
	'''allows the player to  retain gravity, the player is now able to float back down'''
# this function was from the player class in pyscroller
	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = 3
		else:
			self.change_y += 1.25

		# See if we are on the ground.
		if self.rect.y >= 800 - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = 800 - self.rect.height

	def update(self, platforms,door,lava):
		#updated a lot in this function, we have to work on the self.Platform.platform_list
		#and make it work again, we can work on that tomorrow
		''' updates a players current position and  blits him onto th screen'''
		self.calc_grav()
		self.rect.x += self.change_x
		# See if we hit anything
		self.checkCollide(platforms,door,lava)
		for block in self.hitList:
		# set our right side to the left side of the item we hit
			if self.change_x > 0:
				self.rect.right = block.left
			elif self.change_x < 0:
			# Otherwise if we are moving left, do the opposite.
				self.rect.left = block.right

		self.rect.y += self.change_y
		# Check and see if we hit anything
		self.checkCollide(platforms, door,lava)
		for block in self.hitList:
		# Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.top
			elif self.change_y < 0:
				self.rect.top = block.bottom
			self.change_y = 0
