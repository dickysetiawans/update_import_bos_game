import pygame 
from pygame.locals import *
import screen
import player
import musuh
import peluru
'''sprite group'''
ship1_group = pygame.sprite.Group()
musuh_group = pygame.sprite.Group()
peluru_group = pygame.sprite.Group()


ship1 = player.Pesawat(int(screen.panjang / 2), screen.lebar - 100, 100)
ship1_group.add(ship1)

musuh = musuh.Musuh(int(screen.panjang / 2), screen.lebar - 500, 900)
musuh_group.add(musuh)
