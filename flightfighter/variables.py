from pickle import FALSE
import pygame
from os import path
import sys


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return path.join(sys._MEIPASS, relative)
    return path.join(relative)

# Пути для упаковки в exe
# BACKGROUND_PATH = resource_path(os.path.join('img', 'background.png'))
# PLAYER_SPRITE = resource_path(os.path.join('img', 'Player.png'))
# ENEMY_SPRITE = resource_path(os.path.join('img', 'Enemy.png'))
# BULLET_SPRITE = resource_path(os.path.join('img', 'Bullet.png'))
IMG_DIR = path.join(path.dirname(__file__), 'img')
BACKGROUND_PATH = path.join('img', 'background.png')
MENU_BACKGROUND = path.join('img', 'main_menu.jpg')
PLAYER_SPRITE = path.join('img', 'Player.png')
ENEMY_SPRITE = path.join('img', 'Enemy.png')
RUNNING = False
PAUSE = False
MENU = True
SCREEN = WIDTH, HEIGHT = (1024, 768)
FPS = 60
SCORE = 0
ALL_SPRITES = pygame.sprite.Group()
BULLETS = pygame.sprite.Group()
ENEMIES = pygame.sprite.Group()
TREES = pygame.sprite.Group()
CLOUDS = pygame.sprite.Group()
FONT_NAME = pygame.font.match_font("arial")
RESTART = True