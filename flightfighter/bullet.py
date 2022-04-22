import pygame
import variables


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((8, 5))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = x
        self.rect.centerx = y
        self.speedx = 15
     
    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > variables.WIDTH:
            self.kill()