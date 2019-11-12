import pygame
from files import Hero
from files import Platform

class Controller:

	def __init__(self, width = 640, height = 480):
		self.screen = pygame.display.set_mode((width,height))
		self.background = pygame.Surface(self.screen.get_size())
		self.width = width
		self.height = height
		self.Hero = Hero("Bob", (width/3 , height/3), "assets/gameData/kirby.png")
		self.STATE = "GAME"

	def mainloop(self):
		while True:
			if(self.STATE == "GAME"):
				self.gameloop()
			elif(self.STATE == "Exit"):
				self.endloop()

	def gameloop(self):
		pygame.key.set_repeat(1,50)
		while self.STATE == "GAME":
			self.background.fill(149, 249, 12)
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

	def endloop(self):
		self.hero.kill()
		myfont = pygame.font.SysFont(None, 30)
		message = myfont.render("Ayy Lmao", False, (0,0,0))
		self.screen.blit(message, (self.width/2, self.height/2))
		pygame.display.flip()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
