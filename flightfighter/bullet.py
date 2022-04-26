import pygame
import variables


# Пуля
class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, object):
        pygame.sprite.Sprite.__init__(self)
        self.object = object
        self.image = pygame.Surface((8, 5))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = x
        self.rect.centerx = y
        self.speedx = 15
 
    # Метод обновления 
    def update(self):
        if self.object == "player":
            self.rect.x += self.speedx
        elif self.object == "enemy":
            self.rect.x -= self.speedx
        if self.rect.left > variables.WIDTH:
            self.kill()