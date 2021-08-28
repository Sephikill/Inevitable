import pygame
from pygame import image
from pygame.sprite import spritecollide
from config import *
import math
import random

class Sky(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
			#Connect it with the game class
		self.game = game
		self._layer = SKY_LAYER

		#put it in All sprite in game
		self.groups = self.game.all_sprites

		#Actually connect it
		pygame.sprite.Sprite.__init__(self,self.groups)

		#Cords
		self.x = x * TILESIZE
		self.y = y * TILESIZE
		
		#size
		self.width = TILESIZE
		self.height = TILESIZE

		#Image and rect of the Block
		self.image = self.game.terrain_spritesheet.get_sprite(32,64,self.width,self.height)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y