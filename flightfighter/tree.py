import random
import pygame
import variables
from os import path

class Trees(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.tree_width = random.randrange(40, 80)
        self.tree_height = random.randrange(120, 200)
        self.image = pygame.image.load(path.join(variables.IMG_DIR, "Tree.png"))
        self.image = pygame.transform.scale(self.image, (self.tree_width, self.tree_height))
        self.rect = self.image.get_rect()
        self.rect.right = random.randrange(1100, 1500)
        self.rect.bottom = random.randrange(705, 715)
        self.speedx = 6

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < -80:
            self.rect.right = random.randrange(1100, 1500) + self.tree_width + 50
 
