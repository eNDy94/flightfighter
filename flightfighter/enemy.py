import pygame
import random
import variables
from os import path


class Enemies(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.enemy_sprite = pygame.image.load(path.join(variables.IMG_DIR, "Enemy.png")).convert_alpha()
        self.image = self.enemy_sprite
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(1050, 1150), (768 - 267 - (random.randrange(20, 300) + 60))) 
        self.speedx = random.randrange(3, 8)

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < -100:
            self.rect.x = random.randrange(1050, 1150)
            self.rect.y = 768 - 267 - (random.randrange(20, 300) + 60)