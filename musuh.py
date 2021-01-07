import pygame 
from pygame.locals import *
import screen
import time
'''Musuh class'''
class Musuh(pygame.sprite.Sprite):
	def __init__(self, x, y, health):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('image/bos.png')
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]
		self.health_start = health
		self.health_remaining = 1000
		self.move_counter = 7
		self.move_direction = 1
		self.last_alien_shoot = pygame.time.get_ticks()
		self.alien_colldown = 250

	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 180:
			self.move_direction *= -1
			self.move_counter *= self.move_direction
		
		time_now = pygame.time.get_ticks()