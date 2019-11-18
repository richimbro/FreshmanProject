class Levels(object):
	""" This is a generic super-class used to define a level.
		Create a child class for each level with level-specific
		info. """

	def __init__(self, player):
		""" Constructor. Pass in a handle to player. Needed for when moving platforms
			collide with the player. """
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player

		# Background image
		self.background = None

	# Update everythign on this level
	def update(self):
		self.platform_list.update()
		self.enemy_list.update()

	def draw(self, screen):
		# Draw the background
		screen.fill(BLUE)

		# Draw all the sprite lists that we have
		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)
