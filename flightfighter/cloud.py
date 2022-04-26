import pygame
import variables
import random
from os import path


class Clouds(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cloud_width = random.randrange(250, 330)
        self.cloud_height = random.randrange(180, 220)
        self.image = pygame.image.load(path.join(variables.IMG_DIR, "Cloud.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.cloud_width, self.cloud_height))
        self.rect = self.image.get_rect()
        self.rect.right = random.randrange(1050, 1500)
        self.rect.centery = random.randrange(0, 500)
        self.speedx = 2
        
    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.rect.right = random.randrange(1050, 1500) + self.cloud_width + 50