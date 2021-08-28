import pygame
from pygame import image
from pygame import mouse
from pygame.sprite import spritecollide
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		self.x = x
		self.y = y
		self.game = game

		self._layer = PLAYER_LAYER
		self.groups = game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)

		#Cords and Size of Sprtie and Facing
		self.x = x * TILESIZE
		self.y = y * TILESIZE

		self.width = TILESIZE
		self.height = TILESIZE 

		self.x_change = 0
		self.y_change = 0

		#Player HP
		self.MAX_HP = 100
		#when spawn max hp
		self.HP = self.MAX_HP 
		self.HP_change = 0

		#HP bar rect
		self.healthRectW = 100

		#Player Attack
		self.Atk = 0

		self.facing = 'down'
		self.animation_loop = 1

		#Bool for stuff like attacking, special attacks and jumping
		self.is_jumping = False

		#Needed stuff for pygame to show the sprite
		#Png file for looks of Main Char and sprite sheet
		self.image = self.game.player_spritesheet.get_sprite(0,0,self.width,self.height)
		self.image.set_colorkey(BLACK)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

		#Atk bool
		self.is_normAtk = False
		self.is_specialAtk = False
	
	def movement(self):
		#Get key pressed
		keys = pygame.key.get_pressed()

		#wasd keys to move stuff
		if keys[pygame.K_a]:
			#Camera to da left
			for sprite in self.game.all_sprites:
				sprite.rect.x += PLAYER_SPEED

			self.x_change -= PLAYER_SPEED
			self.facing = 'left'
			
		if keys[pygame.K_d]:
			for sprite in self.game.all_sprites:
				sprite.rect.x -= PLAYER_SPEED	

			self.x_change += PLAYER_SPEED
			self.facing = 'right'

		if keys[pygame.K_SPACE] or keys[pygame.K_w]:
			for sprite in self.game.all_sprites:
				sprite.rect.y += PLAYER_SPEED	


			#make jump thing
			self.animation_loop = 1			
			self.y_change -= (PLAYER_SPEED * 3)
			self.is_jumping = True

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

				#going down in block
				if self.y_change > 0:
					self.rect.y = hits[0].rect.top - self.rect.height
					
				#going up into block
				if self.y_change < 0:
					self.rect.y = hits[0].rect.bottom 
			

	def animate(self):
		jump_animations = [
			#Jump up
			self.game.player_spritesheet.get_sprite(32,0,self.width,self.height),
			self.game.player_spritesheet.get_sprite(64,0,self.width,self.height),
			self.game.player_spritesheet.get_sprite(96,0,self.width,self.height),
			self.game.player_spritesheet.get_sprite(128,0,self.width,self.height),			
		]

		left_animation = [
			#Movement right
			self.game.player_spritesheet.get_sprite(96,160,self.width,self.height),
			self.game.player_spritesheet.get_sprite(128,160,self.width,self.height),
			self.game.player_spritesheet.get_sprite(160,160,self.width,self.height),
			self.game.player_spritesheet.get_sprite(192,160,self.width,self.height),
			self.game.player_spritesheet.get_sprite(224,160,self.width,self.height),
			self.game.player_spritesheet.get_sprite(0,192,self.width,self.height),
			self.game.player_spritesheet.get_sprite(32,192,self.width,self.height),
			self.game.player_spritesheet.get_sprite(64,192,self.width,self.height),
			self.game.player_spritesheet.get_sprite(96,192,self.width,self.height),
			self.game.player_spritesheet.get_sprite(128,192,self.width,self.height),
			self.game.player_spritesheet.get_sprite(160,192,self.width,self.height)
		]
		right_animation = [
			#Movement left
			self.game.player_spritesheet.get_sprite(192,192,self.width,self.height),
			self.game.player_spritesheet.get_sprite(224,192,self.width,self.height),
			self.game.player_spritesheet.get_sprite(0,224,self.width,self.height),
			self.game.player_spritesheet.get_sprite(32,224,self.width,self.height),
			self.game.player_spritesheet.get_sprite(64,224,self.width,self.height),
			self.game.player_spritesheet.get_sprite(96,224,self.width,self.height),
			self.game.player_spritesheet.get_sprite(128,224,self.width,self.height),
			self.game.player_spritesheet.get_sprite(160,224,self.width,self.height),
			self.game.player_spritesheet.get_sprite(192,224,self.width,self.height),
			self.game.player_spritesheet.get_sprite(224,224,self.width,self.height),
			self.game.player_spritesheet.get_sprite(0,256,self.width,self.height)
		]

		#Animation bs
		if self.is_jumping == True:
			if self.y_change == 0:
				self.image == self.game.player_spritesheet.get_sprite(0,0,self.width,self.height)
			
			if self.animation_loop >= 3:
				self.animation_loop = 1	

			self.image = jump_animations[math.floor(self.animation_loop)]
			self.animation_loop += 0.1	
		else:
			self.image = self.game.player_spritesheet.get_sprite(0, 0, self.width, self.height)


		if self.facing == "left":
			if self.x_change == 0:
				self.image == self.game.player_spritesheet.get_sprite(0,0,self.width,self.height)
			else:
				self.image = left_animation[math.floor(self.animation_loop)]
				self.animation_loop += 0.1 
				if self.animation_loop >= 11:
					self.animation_loop = 1

		if self.facing == "right":
			if self.x_change == 0:
				self.image == self.game.player_spritesheet.get_sprite(0,0,self.width,self.height)
			else:
				self.image = right_animation[math.floor(self.animation_loop)]
				self.animation_loop += 0.1 
				if self.animation_loop >= 11:
					self.animation_loop = 1


	def camera_move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			#Camera to da left
			for sprite in self.game.all_sprites:
				sprite.rect.x += PLAYER_SPEED

		if keys[pygame.K_RIGHT]:
			#Camera to da right
			for sprite in self.game.all_sprites:
				sprite.rect.x -= PLAYER_SPEED

		if keys[pygame.K_UP]:
			#Camera to da up
			for sprite in self.game.all_sprites:
				sprite.rect.y += PLAYER_SPEED

		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			#Camera to da down
			for sprite in self.game.all_sprites:
				sprite.rect.y -= PLAYER_SPEED

	def collide_enemy(self):
		#If Hit Enemy
		hits1 = pygame.sprite.spritecollide(self, self.game.enemies, False)
		hits2 = pygame.sprite.spritecollide(self, self.game.deaths, False)
		if hits1:
			if self.HP >= 1:
				self.HP_change -= ENEMY_ATK
		if hits2:
			self.kill()
			self.game.playing = False
			self.game.game_over()
	
	def die(self):
		if self.HP <= 0:
			self.kill()
			self.game.playing = False
	
	def gravity(self):
		block_touch = pygame.sprite.spritecollide(self, self.game.blocks,False)

		if not block_touch:
			#Player fall down
			self.y_change += GRAVITY	

	def Attack(self):
		pass

	def ATK_animation(self):
		pass

	def draw_hpbar(self):

		# drawing the background rect in black
		pygame.draw.rect(self.game.screen, (BLACK), [self.rect.x, self.rect.y + 15, self.healthRectW, 50])
		# drawing the real health bar 
		pygame.draw.rect(self.game.screen, (GREEN), [self.rect.x, self.rect.y + 15, int(self.healthRectW/self.MAX_HP)*self.HP, 50])


	def update(self):
		#Apply movement
		self.movement()

		#Gravity
		self.gravity()

		self.animate()
		self.camera_move()

		self.collide_enemy()

		#Other
		#self.draw_hpbar()
		# drawing the background rect in black
		pygame.draw.rect(self.game.screen, (BLACK), [self.rect.x, self.rect.y + 15, self.healthRectW, 10])
		# drawing the real health bar 
		pygame.draw.rect(self.game.screen, (GREEN), [self.rect.x, self.rect.y + 15, int(self.healthRectW/self.MAX_HP)*self.HP, 10])

		self.rect.x += self.x_change
		self.collide_blocks('x')
		self.rect.y += self.y_change
		self.collide_blocks('y')

		#Apply damage and other stuff
		self.HP += self.HP_change

		#Do the death thing
		self.die()

		#reset x and y change vars to 0 after movement
		self.x_change = 0
		self.y_change = 0

		#Reset stuff
		self.HP_change = 0

		self.is_jumping = False