import pygame
import sys
from files import Hero
from files import Platform
from files import Levels
from files import Level1B


class Controller:
	pygame.init()
	def __init__(self, width = 1200, height = 800):
		self.screen = pygame.display.set_mode((width,height))
		self.background = pygame.Surface(self.screen.get_size())
		self.width = width
		self.height = height
		self.Hero = Hero.Hero("assets/gameData/shittyPlayer.jpg", 32 , 32, 200, 200)
		self.STATE = "MENU"
		self.clock = pygame.time.Clock()
		self.myLevel = Levels.Level()


	def mainloop(self):
		while True:
			if(self.STATE == "GAME"):
				self.gameloop()
			elif(self.STATE == "MENU"):
				self.menuloop()
			elif(self.STATE == "Exit"):
				self.endloop()
			elif(self.STATE == "CONTROL"):
				self.controlsloop()

	def gameloop(self):
		background_image = pygame.image.load("assets/gameData/background.jpg").convert() #testimage, change later
		self.myLevel.genMap(self.myLevel.testMap,self.screen)

		pygame.key.set_repeat(1,50)
		while self.STATE == "GAME":
			#self.background.fill((45, 18, 224))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
##################### Player Controls Below #####################
				elif event.type == pygame.KEYDOWN:
					if (event.key == pygame.K_RIGHT):
						self.Hero.move_right()
					elif (event.key == pygame.K_LEFT):
						self.Hero.move_left()
					elif(event.key == pygame.K_SPACE):
						self.Hero.jump()
					elif(event.key == pygame.K_q):
						self.STATE = "MENU"
				elif event.type == pygame.KEYUP:
					if (event.key == pygame.K_RIGHT):
						self.Hero.change_x = 0
					elif (event.key == pygame.K_LEFT):
						self.Hero.change_x = 0
##################### Player Controls Above #####################
#####################     Updating Below    #####################
			self.background.fill((224, 28, 18))
			self.Hero.update(self.myLevel.currentPlatforms)
			self.myLevel.genMap(self.myLevel.testMap,self.screen)
			self.screen.blit(self.Hero.image, (self.Hero.rect.x, self.Hero.rect.y))
			pygame.display.flip()
			self.clock.tick(60)
#####################     Updating Above    #####################

	def menuloop(self):
		self.background.fill((224, 28, 18))
		self.screen.blit(self.background,(0,0))
		myfont = pygame.font.SysFont(None, 30)
		message = myfont.render("Press space to start. Press C for Instructions", False, (0,0,0))
		self.screen.blit(message, (0, self.height/2))
		pygame.display.update()
		while (self.STATE == "MENU"):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if (event.key == pygame.K_SPACE):
						self.STATE = "GAME"
					if (event.key == pygame.K_c):
						self.STATE = "CONTROL"

	def controlsloop(self):
		self.background.fill((69, 245, 66))
		self.screen.blit(self.background,(0,0))
		myfont = pygame.font.SysFont(None, 30)
		message1 = myfont.render("Use the arrow keys to move and space to jump.", False, (0,0,0))
		self.screen.blit(message1, (self.width/4, self.height/2))
		message2 = myfont.render("Press M for Menu", False, (0,0,0))
		self.screen.blit(message2, (self.width/4, self.height/3))
		message3 = myfont.render("Do  not hit into  the spikes", False, (0,0,0))
		self.screen.blit(message3, (self.width/4, self.height/1.5))
		message4 = myfont.render("Good Luck", False, (0,0,0))
		self.screen.blit(message4, (self.width/4, self.height/1.25))
		pygame.display.update()
		while (self.STATE == "CONTROL"):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if (event.key == pygame.K_m):
						self.STATE = "MENU"


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
