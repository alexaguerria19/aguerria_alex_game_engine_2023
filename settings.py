# game settings 
WIDTH = 400
HEIGHT = 650
FPS = 30

# player settings
PLAYER_JUMP = 25
PLAYER_GRAV = 1
PLAYER_FRIC = 0.2
PLAYER_SIZE = 50
JUMP_STRENGTH = -15

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "moving"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"moving"),
                 (125, HEIGHT - 350, 100, 20, "normal"),
                 (222, 200, 100, 20, "moving"),
                 (175, 100, 50, 20, "moving")]

                
