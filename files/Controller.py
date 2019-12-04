import pygame
import sys
import random
from files import Hero
from files import Platform
from files import Levels


class Controller:
	pygame.init()
	def __init__(self, width = 1200, height = 800):
		self.screen = pygame.display.set_mode((width,height))
		self.background = pygame.Surface(self.screen.get_size())
		self.width = width
		self.height = height
		self.STATE = "MENU"
		self.clock = pygame.time.Clock()
		self.myLevel = Levels.Level()
		self.counter = 0
		Level1 = self.myLevel.LevelList[6]
		Level2 = self.myLevel.LevelList[random.randrange(4,7)]
		self.LevelList = [Level1,Level2]



	def mainloop(self):
		while True:
			if(self.STATE == "GAME1"):
				self.gameloop1()
			if(self.STATE == "DEATH"):
				self.deathloop()
			if(self.STATE == "MENU"):
				self.menuloop()
			if(self.STATE == "WIN"):
				self.winloop()
			if(self.STATE == "LOAD"):
				self.loadloop()
			if(self.STATE == "Exit"):
				self.endloop()
			if(self.STATE == "CONTROL"):
				self.controlsloop()

	def gameloop1(self):
		background_image = pygame.image.load("assets/gameData/background.jpg").convert() #testimage, change later
		self.myLevel.genMap(self.LevelList[0],self.screen)
		self.Hero = Hero.Hero("assets/gameData/player.png", 32 , 32, 60, 352)


		pygame.key.set_repeat(1,50)
		while self.STATE == "GAME1":
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
						self.Hero.jump(self.myLevel.currentPlatforms, self.myLevel.currentDoor, self.myLevel.lava)
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
			self.screen.blit(self.background,(0,0))
			self.Hero.update(self.myLevel.currentPlatforms,self.myLevel.currentDoor, self.myLevel.lava)
			self.screen.blit(self.Hero.image, (self.Hero.rect.x, self.Hero.rect.y))
			self.myLevel.genMap(self.LevelList[0],self.screen)

			pygame.display.flip()
			self.clock.tick(60)
			if self.Hero.isTouchingdoor == True:
				if self.counter == 0:
					self.counter +=1
					self.Hero.isTouchingdoor = False
					self.STATE = "LOAD"
				elif self.counter == 1:
					self.STATE = "WIN"
			if self.Hero.dead == True:
				self.counter = 0
				self.STATE = "DEATH"
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
						self.STATE = "GAME1"
					if (event.key == pygame.K_c):
						self.STATE = "CONTROL"

	def deathloop(self):
		self.background.fill((224, 28, 18))
		self.screen.blit(self.background,(0,0))
		myfont = pygame.font.SysFont(None, 30)
		message = myfont.render("You died, press space to continue", False, (0,0,0))
		self.screen.blit(message, (0, self.height/2))
		pygame.display.update()
		while (self.STATE == "DEATH"):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if (event.key == pygame.K_SPACE):
						self.STATE = "GAME1"
					if (event.key == pygame.K_c):
						self.STATE = "CONTROL"

	def winloop(self):
		self.background.fill((224, 28, 18))
		self.screen.blit(self.background,(0,0))
		myfont = pygame.font.SysFont(None, 30)
		message = myfont.render("Congratulations, you won!", False, (0,0,0))
		self.screen.blit(message, (0, self.height/2))
		pygame.display.update()
		while (self.STATE == "WIN"):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

	def loadloop(self):
		self.background.fill((224, 28, 18))
		self.screen.blit(self.background,(0,0))
		myfont = pygame.font.SysFont(None, 30)
		message = myfont.render("Press space to continue", False, (0,0,0))
		self.screen.blit(message, (0, self.height/2))
		pygame.display.update()
		while (self.STATE == "LOAD"):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if (event.key == pygame.K_SPACE):
						self.STATE = "GAME1"


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
