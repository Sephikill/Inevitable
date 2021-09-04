import pygame
from config import*

class Death(pygame.sprite.Sprite):
	#If Player touches it dies,
	def __init__(self, game, x, y):
		self.game = game
		self._layer = BARRIER_LAYER

		#put it in All sprite in game
		self.groups = self.game.all_sprites, self.game.deaths

		#Actually connect it
		pygame.sprite.Sprite.__init__(self,self.groups)

		#Cords
		self.x = x * TILESIZE
		self.y = y * TILESIZE
		
		#size
		self.width = TILESIZE
		self.height = TILESIZE

		#Image and rect of the Block
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(WHITE)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y		