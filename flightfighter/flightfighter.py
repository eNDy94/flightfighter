import pygame
import player
import enemy
import shooting_enemy
import variables
import tree
import cloud
from os import path


# Основной класс игры 
class GameManager():

    # Конструктор класса
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(variables.SCREEN)
        self.background = pygame.image.load(path.join(variables.IMG_DIR, "background.png")).convert_alpha()
        self.background_rect = self.background.get_rect()
        pygame.display.set_caption("Flight Fighter")
        self.clock = pygame.time.Clock()
        self.Shooting_enemy = shooting_enemy.Shooting_enemies()
        for x in range(3):
            self.Cloud = cloud.Clouds()
            variables.ALL_SPRITES.add(self.Cloud)
        for x in range(3):
            self.Tree = tree.Trees()
            self.Enem = enemy.Enemies()
            variables.ALL_SPRITES.add(self.Enem)
            variables.ALL_SPRITES.add(self.Tree)
            variables.ENEMIES.add(self.Enem) 
            variables.TREES.add(self.Tree)
        self.Player = player.Player()
        variables.ALL_SPRITES.add(self.Player)
        variables.ALL_SPRITES.add(self.Shooting_enemy)
        variables.SHOOTING_ENEMIES.add(self.Shooting_enemy)
        
    # Отрисовка текста    
    def draw_text(self, surf, text, size, x, y, color = None):
        font = pygame.font.Font(variables.FONT_NAME, size)
        if color is not None:
            text_surface = font.render(text, True, color)
        else:
            text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect) 
    
    # Отображение главного меню
    def show_menu(self):
        while variables.MENU:
            self.clock.tick(variables.FPS)
            self.background = pygame.image.load(path.join(variables.IMG_DIR, "background.png")).convert_alpha()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    variables.RUNNING = False
                    variables.MENU = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        variables.MENU = False
                        variables.RUNNING = True
                        variables.RESTART = True
                        self.run_game()

            self.screen.blit(self.background, (0, 0))
            self.draw_text(self.screen, "Press ENTER", 50, variables.WIDTH/2, variables.HEIGHT/2)
            pygame.display.flip()

    # Пауза            
    def pause(self):
        variables.PAUSE = True
        while variables.PAUSE:
            self.clock.tick(10)
            self.draw_text(self.screen, "PAUSE", 50, variables.WIDTH/2, variables.HEIGHT/2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    variables.RUNNING = False
                    variables.PAUSE = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        variables.PAUSE = False

            pygame.display.update()

    # Основной цикл игры
    def run_game(self):
        while variables.RUNNING:
            
            # Проверка на рестарт игры и перезапуск всех игровых объектов
            if variables.RESTART:
                self.show_menu()
                variables.RESTART = False
                variables.ALL_SPRITES = pygame.sprite.Group()
                self.background = pygame.image.load(path.join(variables.IMG_DIR, "background.png")).convert_alpha()
                variables.BULLETS = pygame.sprite.Group()
                variables.ENEMIES = pygame.sprite.Group()
                variables.TREES = pygame.sprite.Group()
                variables.SCORE = 0
                self.Shooting_enemy = shooting_enemy.Shooting_enemies()
                for x in range(3):
                    self.Cloud = cloud.Clouds()
                    variables.ALL_SPRITES.add(self.Cloud)
                for x in range(3):
                    self.Tree = tree.Trees()
                    self.Enem = enemy.Enemies()
                    variables.ALL_SPRITES.add(self.Enem)
                    variables.ALL_SPRITES.add(self.Tree)
                    variables.ENEMIES.add(self.Enem) 
                    variables.TREES.add(self.Tree)   
                self.Player = player.Player()
                self.time_spawn_player = pygame.time.get_ticks()
                variables.ALL_SPRITES.add(self.Player)   
                variables.ALL_SPRITES.add(self.Shooting_enemy)
                variables.SHOOTING_ENEMIES.add(self.Shooting_enemy)     
                variables.SCORE = 0
            self.clock.tick(variables.FPS)
            
            # Проверка на события
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    variables.RUNNING = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(list(variables.BULLETS)) < 20:
                        self.Player.shoot()
                    if event.key == pygame.K_p:
                        variables.PAUSE = True
                        self.pause()   
                    if event.key == pygame.K_ESCAPE:
                        variables.RUNNING = False
                        variables.MENU = True                                   
            
            # Коллизии 
            collision_with_enemies = pygame.sprite.spritecollide(self.Player, variables.ENEMIES, True)
            if collision_with_enemies:
                self.Enem = enemy.Enemies()
                variables.ALL_SPRITES.add(self.Enem)
                variables.ENEMIES.add(self.Enem) 
                self.Player.death()
                    
            collision_with_shooting_enemies = pygame.sprite.spritecollide(self.Player, variables.SHOOTING_ENEMIES, True)
            if collision_with_shooting_enemies:
                self.Shooting_enemy = shooting_enemy.Shooting_enemies()
                variables.ALL_SPRITES.add(self.Shooting_enemy)
                variables.SHOOTING_ENEMIES.add(self.Shooting_enemy) 
                self.Player.death()

            collision_with_enemies_bullet = pygame.sprite.spritecollide(self.Player, variables.ENEMYS_BULLETS, True)
            if collision_with_enemies_bullet:
                self.time_player_collision = pygame.time.get_ticks()
                self.Player.death()

            hits = pygame.sprite.groupcollide(variables.ENEMIES, variables.BULLETS, True, True)
            for hit in hits:
                variables.SCORE += 1
                self.Enem = enemy.Enemies()
                variables.ALL_SPRITES.add(self.Enem)
                variables.ENEMIES.add(self.Enem)
            
            hits_shooting_enemy = pygame.sprite.groupcollide(variables.SHOOTING_ENEMIES, variables.BULLETS, True, True)
            for hit in hits_shooting_enemy:
                variables.SCORE += 1
                self.Shooting_enemy = shooting_enemy.Shooting_enemies()
                variables.ALL_SPRITES.add(self.Shooting_enemy)
                variables.SHOOTING_ENEMIES.add(self.Shooting_enemy)
            ticks_in_sec = round(pygame.time.get_ticks()/1000, 0)
            if variables.TIMER < int(ticks_in_sec):
                variables.TIMER = ticks_in_sec
                if variables.TIMER % 2 == 0:
                    self.Shooting_enemy.shoot()                

            collision_with_trees = pygame.sprite.spritecollide(self.Player, variables.TREES, True)
            if collision_with_trees:
                self.Player.death()
                self.Tree = tree.Trees()
                variables.ALL_SPRITES.add(self.Tree)
                variables.TREES.add(self.Tree)
            
            
            # Обновление всех спрайтов
            variables.ALL_SPRITES.update()        
            
            
            # Отрисовка на экране
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))
            variables.ALL_SPRITES.draw(self.screen)
            self.draw_text(self.screen, f"Score: {variables.SCORE}", 18, variables.WIDTH/2, 10)
            self.draw_text(self.screen, f"Health: {self.Player.Health + 1}", 18, 50, 10)
            pygame.display.flip()


if __name__ == "__main__":
    Game = GameManager()
    Game.show_menu()
    pygame.quit()