#C
import pygame

COLOR_PURPLE = (209, 57, 159)
COLOR_WHITE = (255, 255, 255)
#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = dict(bground0=0, bground1=1, bground2=2, bground3=3, bground4=4, bground5=5, bground6=6, Player=3, Enemy1=2, Enemy2=1, PlayerShot=2, Enemy1Shot=5, Enemy2Shot=2)
ENTITY_HEALTH = dict(bground0=999, bground1=999, bground2=999, bground3=999, bground4=999, bground5=999, bground6=999, Player=300, PlayerShot=1, Enemy1Shot=1, Enemy2Shot=3,  Enemy1=50, Enemy2=70)
ENTITY_SHOT_DELAY = {
    'Player':20,
    'Enemy1':150,
    'Enemy2':208

}
#M
MENU_OPTION = ('PLAY DEMO',
               'SCORE',
               'EXIT')
#P
PLAYER_KEY_SHOT = {'Player': pygame.K_RCTRL}
#S
SPAWN_TIME = 4000
#W
WIN_WIDTH = 576
WIN_HEIGHT = 324