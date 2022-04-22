import pygame
import os.path
import sys


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


RUNNING = True
SCREEN = WIDTH, HEIGHT = (1024, 768)
FPS = 60
SCORE = 0
BACKGROUND_PATH = resource_path(os.path.join('img', 'background.png'))
ALL_SPRITES = pygame.sprite.Group()
BULLETS = pygame.sprite.Group()
ENEMIES = pygame.sprite.Group()
TREES = pygame.sprite.Group()
FONT_NAME = pygame.font.match_font("arial")