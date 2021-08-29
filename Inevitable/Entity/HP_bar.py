import pygame
from config import*



class HP_BAR(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, entity):
		#Connect it with the game class
		self.game = entity.game
		self._layer = HP_LAYER

		self.entity = entity

		#Connect with Entity class like Player or enemy

		#put it in All sprite in game
		self.groups = self.game.all_sprites, self.game.HP_BAR

		#Actually connect it
		pygame.sprite.Sprite.__init__(self,self.groups)

		#Cords
		self.x = x * TILESIZE
		self.y = y * TILESIZE
		
		#size
		self.width = width
		self.height = height

		#Image and rect of the Block
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

	#Move HP bar
	def move(self, x_change, y_change):
		self.x += x_change
		self.y += y_change

	#Change the length of HP bar
	def HP_Change(self, amount):
		self.width += amount
	
	def set_HP(self, amount):
		self.width = amount
	
	def update(self):
		pass

