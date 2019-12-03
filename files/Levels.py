import pygame
class Level():
	""" This is a generic super-class used to define a level. """

	def __init__(self):
		self.tileList = []
		self.enemy_list = pygame.sprite.Group()

		# Background image
		self.background = None
		self.testMap = game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
					['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
					['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
					['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
					['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
					['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
					['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
					['1','1','2','0','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
					['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
					['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
					['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
					['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
					['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

# Update everythign on this level

	def genMap(self,map,display):
		green = pygame.image.load("assets/gameData/Green.jpg")
		blue = pygame.image.load("assets/gameData/Blue.jpg")
		self.currentPlatforms = []
		y = 0
		for row in map:
			x = 0
			for platform in row:
				if platform == '1':
					display.blit(green,(x*32,y*32))
				if platform == '2':
					display.blit(blue,(x*32,y*32))
				if platform != '0':
					self.currentPlatforms.append(pygame.Rect(x*32,y*32,32,32))
				x += 1
			y += 1

	def update(self):
		self.platform_list.update()
		self.enemy_list.update()

	def draw(self, screen):
		# Draw the background
		screen.fill(BLUE)

		# Draw all the sprite lists that we have
		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)
