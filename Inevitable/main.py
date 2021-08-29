import pygame
import sys

from pygame.constants import QUIT
from pygame import display

from Entity.Attack import Attack
from Entity.Sprite_Sheet import Spritesheet

from Entity.Live.Player import Player
from Entity.Live.Enemy import Enemy

from Entity.Static.Sky import Sky
from Entity.Static.Rock import Rock
from Entity.Static.Barrier import Barrier
from Entity.Static.Death import Death

from text_buttons.Button import Button

from config import *


class Game:
	def __init__(self):
		#Game Start
		pygame.init()

		#Screen
		self.screen = pygame.display.set_mode( SCREEN_SIZE )


		#Window Name
		self.screen_name = pygame.display.set_caption('Inevitable')

		#FPS
		self.clock = pygame.time.Clock()

		#Font
		self.font = pygame.font.Font('text_buttons/ariblk.ttf', 32)

		#Running Var 
		self.running = True
		

		#SpriteSheets and Images 
		self.terrain_spritesheet = Spritesheet('img/Terrain_SpriteSheet.png')
		self.player_spritesheet = Spritesheet('img/Player_SpriteSheet.png')
		self.attack_spritesheet = Spritesheet('img/Player_Atk.png')
		self.enemy_spritesheet = Spritesheet('img/Enemy Piskel.png')
		self.barriers_img = Spritesheet('img/Special_Blocks.png')
		self.intro_background = pygame.image.load('img/Background.png')
		self.gameover_background = pygame.image.load('img/GameOver.png')

	def createTilemap(self):
		#Pass a Tile map to generate tiles and  terrain
		for i, row in enumerate(tilemap):
			for j, column in enumerate(row):
				Sky(self, j, i)
				if column == "P":
					self.player = Player(self, j, i)
				if column == "E":
					Enemy(self, j , i)
				if column == "R":
					Rock(self, j, i)
				if column == "B":
					Barrier(self, j, i)
				if column == "D":
					Death(self, j , i)


	
	def new(self):
		#Start actual Game
			#A new game starts
		self.playing = True

		#Controll all the sprites 
		self.all_sprites = pygame.sprite.LayeredUpdates()
		#Controll all the obstacles
		self.blocks = pygame.sprite.LayeredUpdates()
		#Controll all the eneimes
		self.enemies = pygame.sprite.LayeredUpdates()
		#Controll all the attaks
		self.attacks = pygame.sprite.LayeredUpdates()
		#Controll all the sprites that resolves in instance death on touching
		self.deaths = pygame.sprite.LayeredUpdates()
		#Controll HP 
		self.HP_BAR = pygame.sprite.LayeredUpdates()




		#Create where player spawns and the terrain
		self.createTilemap()


	
	def events(self):
		#Game loop events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.playing = False
				self.running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LSHIFT:
					#spawn attack
					if self.player.facing == 'left':
						Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y,'left','none')

					if self.player.facing == 'right':			
						Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y,'right','none')

					#Add horrizontal attack
					#Add Flip Attack
	
	def update(self):
		#game loop update and update sprites in all the sprites using the update func in each sprite
		self.all_sprites.update()

	def draw(self):
		#Game Loop draws all da sprites on the screen 
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		self.clock.tick(FPS)
		pygame.display.update()

	def main(self):
		#Game loop
		while self.playing == True:
			#do all the stuff in loop 
			self.events()
			self.update()
			self.draw()
	
	def game_over(self):
		text = self.font.render('U ARE DED', True, WHITE)
		text_rect = text.get_rect(center = (WIN_WIDTH / 2, WIN_HEIGHT / 2))

		restart_button =  Button(WIN_HEIGHT / 2, WIN_WIDTH / 2, 120, 50, WHITE, BLACK, 'Restart?',26)
		
		for sprite in self.all_sprites:
			sprite.kill()
		
		while self.running:
			for event in pygame.event.get():
				if event == pygame.QUIT:
					self.playing = False
					self.running = False


				mouse_pos = pygame.mouse.get_pos()
				mouse_pressed = pygame.mouse.get_pressed()

				if restart_button.is_pressed(mouse_pos, mouse_pressed):
					#Start new game
					self.new()
					self.main()
				#Display da button and text
				self.screen.blit(self.gameover_background, (0,0))
				self.screen.blit(text, text_rect)
				self.screen.blit(restart_button.image, restart_button.rect)
				self.clock.tick(FPS)
				pygame.display.update()

	def intro_screen(self):
		intro = True

		title = self.font.render('Inevitable', True, BLACK)
		title_rect = title.get_rect(x = 10, y = 10)

		play_button = Button(10,50,100,50,RED,BLACK,'Live',32)
		
		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					intro = False
					self.running = False
			mouse_pos = pygame.mouse.get_pos()
			mouse_pressed = pygame.mouse.get_pressed()

			if play_button.is_pressed(mouse_pos, mouse_pressed):
				intro = False
		
			self.screen.blit(self.intro_background, (0,0))
			self.screen.blit(title, title_rect)
			self.screen.blit(play_button.image, play_button.rect)
			self.clock.tick(FPS)
			pygame.display.update()


g = Game()
g.intro_screen()
g.new()
while g.running:
	g.main()
	g.game_over()

pygame.quit() 
sys.exit()