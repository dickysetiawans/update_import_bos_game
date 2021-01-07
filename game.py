import pygame 
from pygame.locals import *
import screen
import background
import player
import group
import musuh
import peluru

run = True 
while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    background.back_ground.update1()
    background.back_ground.render()

    group.ship1.update()
    group.musuh_group.update()

    group.musuh_group.draw(screen.tampilan) 
    group.ship1_group.draw(screen.tampilan)

    pygame.display.update()

pygame.quit()