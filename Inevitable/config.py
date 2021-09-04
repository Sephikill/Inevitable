#MAP SIZE and Tile Size
#Pygame window size
WIN_WIDTH = 640
WIN_HEIGHT = 470
SCREEN_SIZE = [640, 470]
#Game Fps
FPS = 60

#Game Vars
GRAVITY = 1


#Size of each tile
TILESIZE = 32

#Draw Layers
HP_LAYER = 7
PLAYER_LAYER = 6
ENEMY_LAYER = 5
CAMERA_LAYER = 4
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
PLAYER_ATTACK_POWER = 1

tilemap = [
	'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
	'B..................................................................B',
	'B.........E..........RRRRR.........................................B',
	'B......RRRR.......................RRRRRR....RRRRRRRRR...........RRRB',
	'B......................E...........................................B',
	'B..E.................RRRRR.........................................B',
	'BRRRRR.............................E.............RRRRRRRRRRRRR.....B',
	'B.........E....................RRRRRRRR............................B',
	'B......RRRRR...........RRRR......................................RRB',
	'B...................................................RRR............B',
	'B.............RRRR.................E...............................B',
	'B........P.....................RRRRRRRR............................B',
	'B..RRRRRRRRRRRRR........RRR....................RRRRRRRRRRRRRRR.....B',
	'B................................................................RRB',
	'B..................................................................B',
	'B....................RRRRR.........................RRR.............B',
	'B....RRRRRRRRRRRRR...................RRRRRRR.......................B',
	'B..................................................................B',
	'B.....RRRRRRRRRRRRRRRRRRR...RRRRRRRRRRRR......RRRRRRRRRRRRR....RRRRB',
	'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
]

#Enemies Stuff
ENEMY_SPEED = 2
ENEMY_ATK = 5