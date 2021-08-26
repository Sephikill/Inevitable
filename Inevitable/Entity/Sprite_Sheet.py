import pygame
from pygame import image
from pygame.sprite import spritecollide
from config import *
import math
import random

class Spritesheet:
	def __init__(self, file):
		self.sheet = pygame.image.load(file).convert()
	
	def get_sprite(self, x, y ,width, height):
		sprite = pygame.Surface([width, height])
		sprite.blit(self.sheet,(0,0), (x, y, width, height))
		sprite.set_colorkey(BLACK)
		return sprite 