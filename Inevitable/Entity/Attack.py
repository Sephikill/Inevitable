import pygame
import math

from config import*

class Attack(pygame.sprite.Sprite):
	
	def __init__(self, game, x ,y, direction, special):

		self.game = game

		self._layer = PLAYER_LAYER

		#put in group
		self.groups = self.game.all_sprites, self.game.attacks
		#Actually connect it
		pygame.sprite.Sprite.__init__(self,self.groups)

		self.x = x
		self.y = y
		self.width = TILESIZE
		self.height = TILESIZE

		self.animation_loop = 0

		self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height)
		self.rect = self.image.get_rect()
		
		self.rect.x = self.x
		self.rect.y = self.y

		#Tells which way the attack is going
		self.direction = direction

		#is special attacking and which one
		#if says spin do 'spin' attack and vice versa for 'flip' else nothing
		#if says anything but 'spin' or 'flip' do nothing
		self.special = special
		

	def update(self):
		self.animate()
	

	def animate(self):

		attack_animation = [
			self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
			self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
			self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),

			self.game.attack_spritesheet.get_sprite(0, 32, self.width, self.height),
			self.game.attack_spritesheet.get_sprite(32, 32, self.width, self.height),
			self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height),

			self.game.attack_spritesheet.get_sprite(0, 64, self.width, self.height),
			self.game.attack_spritesheet.get_sprite(32, 64, self.width, self.height),
			self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height),

			self.game.attack_spritesheet.get_sprite(0, 96, self.width, self.height)
		]

		if self.direction == 'up' or self.direction == 'right' or self.direction == 'left':
			self.image = attack_animation[math.floor(self.animation_loop)]
			self.animation_loop += .5

			if self.animation_loop >= 10:
				self.kill()
	
	def spin_atk(self):
		#Player does spin animation and attack object 
		#just telport right side stay there and telport left side and stay there
		pass

	def flip_atk(self):
		#Player does spin animation
		#Atk object moves around the player in a circular fashion at all times
		pass