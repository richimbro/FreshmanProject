from files.Level import Level

class Level1A(Level):
	def __init__(self, player):
		""" Create level 1. """

		# Call the parent constructor
		Level.__init__(self, player)
		self.background = pygame.image.load("background_01.png").convert()
		self.background.set_colorkey(constants.WHITE)
		self.player = player

		# Array with width, height, x, and y of platform
		Level = [[210, 70, 500, 500],
				[210, 70, 200, 400],
				[210, 70, 600, 300],
				]
		#platform = []
		#enemies = []
		#startstop = [(0,0),(50,100)]
		#Level = [platform,enemies,startstop]


		# Go through the array above and add platforms
		for platform in Level:
			block = Platform(platform[0], platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			block.player = self.player
			self.platform_list.add(block)
