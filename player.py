import pygame 
from pygame.locals import *
import screen
import time
import peluru

class Pesawat(pygame.sprite.Sprite):
	def __init__(self,x,y,darah):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('image/ship1.png')
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]
		self.health_start = darah
		self.health_remaining = darah
		self.last_shoot = pygame.time.get_ticks()

	def update(self):
		'''Kecepatan bergegerak'''
		kecepatan = 8
		speed = 5 # Ecepatan bergerak ke atas bawah
		colldown = 500
		COLLDOWN = 100

		key = pygame.key.get_pressed()
		if key[pygame.K_a] and self.rect.left > 0:
			self.rect.x -= kecepatan
		if key[pygame.K_d] and self.rect.right < screen.panjang:
			self.rect.x += kecepatan
		if key[pygame.K_w] and self.rect.top > 0:
			self.rect.y -= speed
		if key[pygame.K_s] and self.rect.bottom < screen.lebar:
			self.rect.y += speed
		
		time_now = pygame.time.get_ticks()

		'''Tembak'''
		if key[pygame.K_SPACE] and time_now - self.last_shoot > colldown:
			peluru = peluru.Peluru(self.rect.centerx, self.rect.top)
			peluru_group.add(peluru)
			self.last_shoot = time_now
