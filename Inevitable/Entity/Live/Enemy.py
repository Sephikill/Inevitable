import pygame
import random
import math

from config import *
from pygame.sprite import spritecollide


class Enemy(pygame.sprite.Sprite):
	def __init__(self, game, x ,y):
		
		self.game = game
		self._layer = ENEMY_LAYER
		self.groups = self.game.all_sprites, self.game.enemies
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.x = x * TILESIZE
		self.y = y * TILESIZE
		self.width = TILESIZE
		self.height = TILESIZE

		
		self.x_change = 0
		self.y_change = 0

		#Get image and maske it transperant
		self.image = self.game.enemy_spritesheet.get_sprite(0,0,self.width,self.height)
		self.image.set_colorkey(BLACK)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

		#Picks if facing left or right
		self.facing = random.choice(['left','right',])
		#Setup for if enemy move left or right and distance it does as well animations
		self.animation_loop = 1
		self.movement_loop = 0
		self.max_travel = random.randint(10,50)

	def gravity(self):
		block_touch = pygame.sprite.spritecollide(self, self.game.blocks, False)
		if not block_touch:
			self.y_change += 1

	def movement(self):
		if self.facing == 'left':
			self.x_change += ENEMY_SPEED
			self.movement_loop -= 1
			#every frame thing determines if it should turn right cuz its moving left now
			if self.movement_loop <= -self.max_travel:
				self.facing = 'right'

		if self.facing == 'right':
			self.x_change -= ENEMY_SPEED
			self.movement_loop += 1
			#every frame thing determines if it should turn left cuz its moving left now
			if self.movement_loop >= self.max_travel:
				self.facing = 'left'
	def animation(self):
		up_animations = [
			#Movement up
			self.game.enemy_spritesheet.get_sprite(0,0,self.width,self.height),
			self.game.enemy_spritesheet.get_sprite(32,0,self.width,self.height),
			self.game.enemy_spritesheet.get_sprite(64,0,self.width,self.height)
		]
		down_animation = [
			#Movement down
			self.game.enemy_spritesheet.get_sprite(0,32,self.width,self.height),
			self.game.enemy_spritesheet.get_sprite(32,32,self.width,self.height),
			self.game.enemy_spritesheet.get_sprite(64,32,self.width,self.height)
		]

		right_animation = [
			#Movement right
			self.game.enemy_spritesheet.get_sprite(0,64,self.width,self.height),
			self.game.enemy_spritesheet.get_sprite(32,64,self.width,self.height),
			self.game.enemy_spritesheet.get_sprite(64,64,self.width,self.height)
		]
		left_animation = [
			#Movement left
			self.game.enemy_spritesheet.get_sprite(0,96,self.width,self.height),
			self.game.enemy_spritesheet.get_sprite(32,96,self.width,self.height),
			self.game.enemy_spritesheet.get_sprite(64,96,self.width,self.height)
		]
		#Animation bs
		if self.facing == "down":
			if self.y_change == 0:
				self.image == self.game.enemy_spritesheet.get_sprite(0,32,self.width,self.height)
			else:
				self.image = down_animation[math.floor(self.animation_loop)]
				self.animation_loop += 0.1 
				if self.animation_loop >= 3:
					self.animation_loop = 1

		if self.facing == "up":
			if self.y_change == 0:
				self.image == self.game.enemy_spritesheet.get_sprite(0,0,self.width,self.height)
			else:
				self.image = up_animations[math.floor(self.animation_loop)]
				self.animation_loop += 0.1 
				if self.animation_loop >= 3:
					self.animation_loop = 1		

		if self.facing == "right":
			if self.x_change == 0:
				self.image == self.game.enemy_spritesheet.get_sprite(0,64,self.width,self.height)
			else:
				self.image = right_animation[math.floor(self.animation_loop)]
				self.animation_loop += 0.1 
				if self.animation_loop >= 3:
					self.animation_loop = 1	

		if self.facing == "left":
			if self.x_change == 0:
				self.image == self.game.enemy_spritesheet.get_sprite(0,96,self.width,self.height)
			else:
				self.image = left_animation[math.floor(self.animation_loop)]
				self.animation_loop += 0.1 
				if self.animation_loop >= 3:
					self.animation_loop = 1
	def collide_blocks(self, direction):
		#Function when player tries to go over obstacles that u can go over. eg rocks and trees
		if direction == "x":
			hits = pygame.sprite.spritecollide(self, self.game.blocks,False)
			if hits:
				#goes opposite way when hit rock
				if self.x_change > 0:
					self.rect.x = hits[0].rect.left - self.rect.width

				if self.x_change < 0:
					self.rect.x = hits[0].rect.right 

		if direction == "y":
			hits = pygame.sprite.spritecollide(self, self.game.blocks,False)
			if hits:
				#goes opposite way when hit rock
				if self.y_change > 0:
					self.rect.y = hits[0].rect.top - self.rect.height

				if self.y_change < 0:
					self.rect.y = hits[0].rect.bottom

	def barrier_death(self):
		is_dead = pygame.sprite.spritecollide(self, self.game.deaths, False)
		if is_dead:
			self.kill()

	def update(self):
		#Make it move in left or right and animate
		self.movement() 
		self.animation()
		
		#Gravity and if touch barrier death
		self.gravity()
		self.barrier_death()

		#change da sprite
		self.rect.x += self.x_change
		self.collide_blocks('x')
		self.rect.y += self.y_change
		self.collide_blocks('y')
		
		self.x_change = 0
		self.y_change = 0