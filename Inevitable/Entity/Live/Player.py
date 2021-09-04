import pygame
import math

from pygame import key
from Entity.Attack import Attack
import random

from pygame import image
from pygame import mouse
from pygame.sprite import spritecollide

from config import *



class Player(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		self.x = x
		self.y = y
		self.game = game

		self.screen = game.screen

		#Cooldown attack so u dont have weird thing
		self.last = pygame.time.get_ticks()
		
		self.COOLDOWN = 30

		#Cooldown for special attacks
		self.spec_last = pygame.time.get_ticks()

		self.spec_cooldown = 90



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
		self.MAX_HP = 500
		#when spawn max hp
		self.HP = self.MAX_HP 
		self.HP_change = 0

		#HP bar rect
		self.hp_bar_width = 150

		#Ratio thing
		self.HP_Ratio = self.MAX_HP / self.hp_bar_width


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

		#Atk var to tell if doing norm right atk or norm special
		#Flip - does flip animation, spin - spin animation - stop means halt animation or dont keep going
		self.cur_normAtk = ''

		#if facing a certain and shift will do certain animation
		#left_atk - spawns attack left side and vice versa for right - stop means halt animation or dont keep going
		self.cur_specialAtk = ''

		#Is attacking for norm and special
		self.is_atk = False

		self.is_spec_atk = False


		#atk animation for norm animation
		self.atk_animation_loop = 0
		#atk animation for special animation
		self.special_animation_loop = 0
	
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
			self.cur_normAtk = self.facing
			
		if keys[pygame.K_d]:
			for sprite in self.game.all_sprites:
				sprite.rect.x -= PLAYER_SPEED	


			self.x_change += PLAYER_SPEED
			self.facing = 'right'
			self.cur_normAtk = self.facing

		if keys[pygame.K_SPACE] or keys[pygame.K_w]:
			for sprite in self.game.all_sprites:
				sprite.rect.y += PLAYER_SPEED	

			#make jump thing
			self.animation_loop = 1			
			self.y_change -= (PLAYER_SPEED * 2)
			self.is_jumping = True
			self.cur_normAtk = 'up'

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
				self.image = self.game.player_spritesheet.get_sprite(0,0,self.width,self.height)
			
			if self.animation_loop >= 3:
				self.animation_loop = 1	

			self.image = jump_animations[math.floor(self.atk_animation_loop)]
			self.animation_loop += 0.1	
		else:
			self.image = self.game.player_spritesheet.get_sprite(0, 0, self.width, self.height)


		if self.facing == "left":
			if self.x_change == 0:
				self.image = self.game.player_spritesheet.get_sprite(0,0,self.width,self.height)
			else:
				self.image = left_animation[math.floor(self.animation_loop)]
				self.animation_loop += 0.1 
				if self.animation_loop >= 11:
					self.animation_loop = 1

		if self.facing == "right":
			if self.x_change == 0:
				self.image = self.game.player_spritesheet.get_sprite(0,0,self.width,self.height)
			else:
				self.image = right_animation[math.floor(self.animation_loop)]
				self.animation_loop += 0.1 
				if self.animation_loop >= 11:
					self.animation_loop = 1

	def atk_animate(self):
		#17 
		flip_animation = [
			self.game.player_spritesheet.get_sprite(0, 32, self.width, self.height),
			self.game.player_spritesheet.get_sprite(32, 32, self.width, self.height),
			self.game.player_spritesheet.get_sprite(64, 32, self.width, self.height),
			self.game.player_spritesheet.get_sprite(96, 32, self.width, self.height),
			self.game.player_spritesheet.get_sprite(128, 32, self.width, self.height),
			self.game.player_spritesheet.get_sprite(160, 32, self.width, self.height),
			self.game.player_spritesheet.get_sprite(190, 32, self.width, self.height),
			self.game.player_spritesheet.get_sprite(224, 32, self.width, self.height),
			self.game.player_spritesheet.get_sprite(0, 64, self.width, self.height),
			self.game.player_spritesheet.get_sprite(32, 64, self.width, self.height),
			self.game.player_spritesheet.get_sprite(64, 64, self.width, self.height),
			self.game.player_spritesheet.get_sprite(96, 64, self.width, self.height),
			self.game.player_spritesheet.get_sprite(128, 64, self.width, self.height),
			self.game.player_spritesheet.get_sprite(160, 64, self.width, self.height),
			self.game.player_spritesheet.get_sprite(192, 64, self.width, self.height),
			self.game.player_spritesheet.get_sprite(224, 64, self.width, self.height),
			self.game.player_spritesheet.get_sprite(0, 96, self.width, self.height)		
		]
		#18
		spin_animation = [
			self.game.player_spritesheet.get_sprite(32, 96, self.width, self.height),
			self.game.player_spritesheet.get_sprite(64, 96, self.width, self.height),
			self.game.player_spritesheet.get_sprite(96, 96, self.width, self.height),
			self.game.player_spritesheet.get_sprite(128, 96, self.width, self.height),
			self.game.player_spritesheet.get_sprite(160, 96, self.width, self.height),
			self.game.player_spritesheet.get_sprite(192, 96, self.width, self.height),
			self.game.player_spritesheet.get_sprite(224, 96, self.width, self.height),
			self.game.player_spritesheet.get_sprite(0, 128, self.width, self.height),
			self.game.player_spritesheet.get_sprite(32, 128, self.width, self.height),
			self.game.player_spritesheet.get_sprite(64, 128, self.width, self.height),
			self.game.player_spritesheet.get_sprite(96, 128, self.width, self.height),
			self.game.player_spritesheet.get_sprite(128, 128, self.width, self.height),
			self.game.player_spritesheet.get_sprite(160, 128, self.width, self.height),
			self.game.player_spritesheet.get_sprite(192, 128, self.width, self.height),
			self.game.player_spritesheet.get_sprite(224, 128, self.width, self.height),
			self.game.player_spritesheet.get_sprite(0, 160, self.width, self.height),
			self.game.player_spritesheet.get_sprite(32, 160, self.width, self.height),
			self.game.player_spritesheet.get_sprite(64, 160, self.width, self.height)
		]

		left_atk_animation = [
			self.game.player_spritesheet.get_sprite(224, 0, self.width, self.height),
			self.game.player_spritesheet.get_sprite(224, 0, self.width, self.height),
			self.game.player_spritesheet.get_sprite(224, 0, self.width, self.height),
			self.game.player_spritesheet.get_sprite(224, 0, self.width, self.height)
		]

		right_atk_animation = [
			self.game.player_spritesheet.get_sprite(192, 0, self.width, self.height),
			self.game.player_spritesheet.get_sprite(192, 0, self.width, self.height),
			self.game.player_spritesheet.get_sprite(192, 0, self.width, self.height),
			self.game.player_spritesheet.get_sprite(192, 0, self.width, self.height)
		]

		up_atk_animation = [
			self.game.player_spritesheet.get_sprite(160, 0, self.width, self.height),
			self.game.player_spritesheet.get_sprite(160, 0, self.width, self.height),
			self.game.player_spritesheet.get_sprite(160, 0, self.width, self.height),
			self.game.player_spritesheet.get_sprite(160, 0, self.width, self.height)
		]

		#Norm attacks and Animation bs
		if self.cur_normAtk == 'left' and self.is_atk == True:		#Animation bs			
			if self.atk_animation_loop >= 3:
				self.atk_animation_loop = 1
				self.cur_normAtk = 'stop'
				self.is_atk = False

			self.image = left_atk_animation[math.floor(self.atk_animation_loop)]
			self.atk_animation_loop += 0.1	

		if self.cur_normAtk == 'right' and self.is_atk == True:
			if self.atk_animation_loop >= 3:
				self.atk_animation_loop = 1
				self.cur_normAtk = 'stop'
				self.is_atk = False

			self.image = right_atk_animation[math.floor(self.atk_animation_loop)]
			self.atk_animation_loop += 0.1	

		if self.cur_normAtk == 'up'and self.is_atk == True:
			if self.atk_animation_loop >= 3:
				self.atk_animation_loop = 1
				self.cur_normAtk = 'stop'
				self.is_atk = False

			self.image = up_atk_animation[math.floor(self.atk_animation_loop)]
			self.atk_animation_loop += 0.1	

		#Speical attacks
		if self.cur_specialAtk == 'flip' and self.is_spec_atk == True:
			if self.special_animation_loop >= 14:
				self.special_animation_loop = 1.1
				self.cur_specialAtk = 'stop'
				self.is_spec_atk = False

			self.image = flip_animation[math.floor(self.special_animation_loop)]
			self.special_animation_loop += 0.1	

		if self.cur_specialAtk == 'spin'and self.is_spec_atk == True: 
			if self.special_animation_loop >= 17:
				self.special_animation_loop = 1
				self.cur_specialAtk = 'stop'
				self.is_spec_atk = False

			self.image = spin_animation[math.floor(self.special_animation_loop)]
			self.special_animation_loop += 0.1	


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
		#Game loop events
		if self.last >= self.COOLDOWN:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_LSHIFT]:
				self.is_atk = True
				#spawn attack
				if self.facing == 'left':
					Attack(self.game, self,self.rect.x - TILESIZE, self.rect.y,'left','none')

				if self.facing == 'right':		
					Attack(self.game, self, self.rect.x + TILESIZE, self.rect.y,'right','none')

				if self.is_jumping == True:
					self.facing = ''
					#Does attack that goes up with player
					Attack(self.game, self, self.rect.x, self.rect.y - TILESIZE,'up','up_spec')

			self.last = 0

	def special_atk(self):
		if self.spec_last >= self.spec_cooldown:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_1]:
				self.is_spec_atk = True
				self.cur_specialAtk = 'flip'
				if self.facing == 'left':
					Attack(self.game, self,self.rect.x - TILESIZE, self.rect.y,'left','flip_spec')

				if self.facing == 'right':		
					Attack(self.game, self, self.rect.x + TILESIZE, self.rect.y,'right','flip_spec')
			
			self.spec_last = 0

			if keys[pygame.K_2]:
				self.is_spec_atk = True
				self.cur_specialAtk = 'spin'
				if self.facing == 'left':
					Attack(self.game, self,self.rect.x - TILESIZE, self.rect.y,'left','spin_spec')

				if self.facing == 'right':		
					Attack(self.game, self, self.rect.x + TILESIZE, self.rect.y,'right','spin_spec')				

			self.spec_last = 0

	def update(self):
		#Apply movement
		self.movement()

		#Attack and cooldown to next attack decrease
		self.Attack()
		self.last += 1

		#Special attack and cooldown
		self.special_atk()
		self.spec_last += 1


		#Gravity
		self.gravity()

		self.animate()
		self.atk_animate()


		self.camera_move()

		self.collide_enemy()

		self.rect.x += self.x_change
		self.collide_blocks('x')
		self.rect.y += self.y_change
		self.collide_blocks('y')

		#Apply HP and draw bar
		self.HP += self.HP_change

		# Draw black bar and green bar
		black_rect = pygame.Rect(self.rect.x, self.rect.y - 15, self.hp_bar_width, 10)
		hp_rect = pygame.Rect(self.rect.x, self.rect.y - 15, int(self.hp_bar_width / self.MAX_HP)*self.HP, 10)

		pygame.draw.rect(self.screen, BLACK , black_rect)
		pygame.draw.rect(self.screen, GREEN , hp_rect)


		#Do the death thing
		self.die()

		#reset x and y change vars to 0 after movement
		self.x_change = 0
		self.y_change = 0

		#Reset stuff
		self.HP_change = 0

		self.is_jumping = False

