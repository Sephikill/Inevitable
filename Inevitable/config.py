#MAP SIZE and Tile Size
#Pygame window size
WIN_WIDTH = 640
WIN_HEIGHT = 470
#Game Fps
FPS = 60


#Size of each tile
TILESIZE = 32

#Draw Layers
PLAYER_LAYER = 5
ENEMY_LAYER = 4
ROCK_LAYER = 3
BARRIER_LAYER = 2
SKY_LAYER = 1

#Colors
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Player stuff
PLAYER_SPEED = 2

tilemap = [
	'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
	'B...........................................B',
	'B.........E..........RRRRR..................B',
	'B......RRRR.......................RRRRRR....B',
	'B......................E....................B',
	'B..E................RRRRR...................B',
	'BRRRRR.............................E........B',
	'B.........E....................RRRRRRRR.....B',
	'B......RRRRR...........RRRR.................B',
	'B...........................................B',
	'B.............RRRR.................E........B',
	'B........P.....................RRRRRRRR.....B',
	'B..RRRRRRRRRRRRR........RRR.................B',
	'B...........................................B',
	'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
]

#Enemies Stuff
ENEMY_SPEED = 2
ENEMY_ATK = 5