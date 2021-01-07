import pygame 
from pygame.locals import *
import screen
import musuh
import time

'''Peluru player class'''
class Peluru(pygame.sprite.Sprite):
	def __init__(self, x, y,):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img_peluru/peluru.png')
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]

	def update(self):
		self.rect.y -= 9
		if self.rect.top > screen.lebar:
			self.kill()
		if pygame.sprite.spritecollide(self, group.musuh_group, False):
			self.kill()
			musuh.health_remaining -= 2