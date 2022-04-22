import pygame
import variables
import bullet


# Игрок
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Health = 2
        self.image = pygame.Surface((40, 20))
        self.image.fill((0, 0, 255))
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

