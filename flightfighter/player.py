import pygame
import variables
import bullet
import flightfighter
from os import path


# Игрок
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Player_sprite = pygame.image.load(path.join(variables.IMG_DIR, "Player.png")).convert_alpha()
        self.Health = 2
        self.image = self.Player_sprite
        self.rect = self.image.get_rect()
        self.rect.center = (100, variables.HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def shoot(self):
        Bullet = bullet.Bullet(self.rect.centery, self.rect.right)
        variables.ALL_SPRITES.add(Bullet)
        variables.BULLETS.add(Bullet)

    def death(self):
        if self.Health <= 0:
            variables.RUNNING = False
            variables.MENU = True
            Game = flightfighter.GameManager()
            Game.show_menu()
        else:
            self.Health -= 1
            self.rect.center = (100, variables.HEIGHT / 2)

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx -= 5
        if keystate[pygame.K_RIGHT]:
            self.speedx += 5
        if keystate[pygame.K_UP]:
            self.speedy -= 5
        if keystate[pygame.K_DOWN]:
            self.speedy += 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > variables.WIDTH:
            self.rect.right = variables.WIDTH
        if self.rect.left < 30:
            self.rect.left = 30
        if self.rect.top < 50:
            self.rect.top = 50
        if self.rect.bottom > 700:
            self.death()

