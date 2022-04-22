import random
import pygame


class Trees(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.tree_width = random.randrange(40, 80)
        self.tree_height = random.randrange(120, 200)
        self.image = pygame.Surface((self.tree_width, self.tree_height))
        self.image.fill((148, 68, 0))
        self.rect = self.image.get_rect()
        self.rect.right = random.randrange(1100, 1500)
        self.rect.bottom = 701
        self.speedx = 6

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < -80:
            self.rect.right = random.randrange(1100, 1500) + self.tree_width + 50
 
