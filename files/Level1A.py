class Level1A(Level):

		def __init__(self, player):
	 		""" Create level 1. """

			# Call the parent constructor
			Level.__init__(self, player)
			# Array with width, height, x, and y of platform
			level = [[210, 70, 500, 500],
					[210, 70, 200, 400],
					[210, 70, 600, 300],
					]

			# Go through the array above and add platforms
			for platform in level:
				block = Platform(platform[0], platform[1])
				block.rect.x = platform[2]
				block.rect.y = platform[3]
				block.player = self.player
				self.platform_list.add(block)
