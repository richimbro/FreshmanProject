class Level1A:

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
