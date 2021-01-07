import pygame
from pygame.locals import *
import screen
'''Background bergerak'''    
class Background():
      def __init__(self):
            self.bgimage = pygame.image.load('image/background3.png')
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingUpSpeed = 5
         
      def update1(self):
        self.bgY1 -= self.movingUpSpeed
        self.bgY2 -= self.movingUpSpeed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
             
      def render(self):
         screen.tampilan.blit(self.bgimage, (self.bgX1, self.bgY1))
         screen.tampilan.blit(self.bgimage, (self.bgX2, self.bgY2))


back_ground = Background()