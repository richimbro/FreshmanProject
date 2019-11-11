import pygame
import random

class Hero:

    def __init__(self, image, height, width, speed, health, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.height = height
        self.speed = speed
        self.width= width
        self.health = health
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.health = 1 #How many lives do we want him having?

    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed
    def jump(self): #going to have to fix this
        self.rect.y += self.speed
        self.rect.y -= self.speed

    def fight(self, enemy):
        #are we  having  an enemy?
