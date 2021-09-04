import pygame

class Button:
	def __init__(self, x, y, width, height, fg, bg, content, fontsize):
		#Which file to get text from and content on button
		self.font = pygame.font.Font('text_buttons/ariblk.ttf',fontsize)
		self.content = content

		#Cords
		self.x = x
		self.y = y

		#Size
		self.width = width
		self.height = height

		#color of da thing
		self.fg = fg
		self.bg = bg

		#things looks
		self.image = pygame.Surface((self.width, self.height))
		self.image.fill(self.bg)
		self.rect = self.image.get_rect()

		self.rect.x = self.x
		self.rect.y = self.y

		#Text
		self.text = self.font.render(self.content, True, self.fg)
		self.text_rect = self.text.get_rect(center = (self.width / 2, self.height / 2) )
		self.image.blit(self.text,self.text_rect)

	#func is pressed. 
	def is_pressed(self,pos,pressed):
		if self.rect.collidepoint(pos):
			#if left clicked sinec python returns a list and one is true or not and right click is on pressed[1]?
			if pressed[0]:
				return True
			return False
		return False