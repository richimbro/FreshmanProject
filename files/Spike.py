class Spike:

	def __init__(self, image, x, y, height, width):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load()
		self.x = x
		self.y = y
		self.height = height
		self.width = width

	def get_rect(self):
		return self.rect

	def draw(self):
		if self.bool == True:
			screen.blit(self.RIGHT, [self.position_x, self.position_y])
		else:
			screen.blit(self.LEFT, [self.position_x, self.position_y])

	def update(self):
		self.draw()
		self.get_rect()
