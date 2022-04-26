import pygame
import random
import variables
import bullet
from os import path


class Shooting_enemies(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.enemy_sprite = pygame.image.load(path.join(variables.IMG_DIR, "Enemy.png")).convert_alpha()
        self.image = self.enemy_sprite
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(1050, 1150), (768 - 267 - (random.randrange(20, 300) + 60)))
        self.start_position_y = self.rect.centery
        self.speedx = 4
        self.speedy = 2
        
    def shoot(self):
        Bullet = bullet.Bullet(self.rect.centery, self.rect.left, "enemy")
        variables.ALL_SPRITES.add(Bullet)
        variables.ENEMYS_BULLETS.add(Bullet)

    def update(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.y > self.start_position_y + 50:
            self.speedy = -2
        elif self.rect.y < self.start_position_y - 50:
            self.speedy = 2
        if self.rect.right < -100:
            self.rect.center = (random.randrange(1050, 1150), (768 - 267 - (random.randrange(20, 300) + 60)))
            self.start_position_y = self.rect.centery