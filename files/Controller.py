import pygame
from files import Hero
from files import Platform

class Controller:

	def __init__(self, width = 640, height = 480):
		self.screen = pygame.display.set_mode((width,height))
		self.background = pygame.Surface(self.screen.get_size())
		self.width = width
		self.height = height
		self.Hero = Hero.Hero("assets/gameData/kirby.png", 3 , 3, 320, 240)
		self.STATE = "GAME"
		self.clock = pygame.time.Clock()


	def mainloop(self):
		while True:
			if(self.STATE == "GAME"):
				self.gameloop()
			elif(self.STATE == "Exit"):
				self.endloop()

	def gameloop(self):
		pygame.key.set_repeat(1,50)
		while self.STATE == "GAME":
			self.background.fill((149, 100, 12))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if (event.key == pygame.K_RIGHT):
						self.Hero.move_right()
					elif (event.key == pygame.K_LEFT):
						self.Hero.move_left()
					elif(event.key == pygame.K_SPACE):
						self.Hero.jump()
			self.Hero.update()
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.Hero.image, (self.Hero.rect.x, self.Hero.rect.y))
			pygame.display.update()
			self.clock.tick(60)

	def endloop(self):
		self.Hero.kill()
		myfont = pygame.font.SysFont(None, 30)
		message = myfont.render("Ayy Lmao", False, (0,0,0))
		self.screen.blit(message, (self.width/2, self.height/2))
		pygame.display.flip()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
