from ast import While
import pygame
import player
import enemy
import variables
import tree
from os import path


class GameManager():

    def __init__(self):
        pygame.init()
        self.background = pygame.image.load(path.join(variables.IMG_DIR, "background.png"))
        self.background_rect = self.background.get_rect()
        self.screen = pygame.display.set_mode(variables.SCREEN)
        pygame.display.set_caption("Flight Fighter")
        self.clock = pygame.time.Clock()
        self.Player = player.Player()
        variables.ALL_SPRITES.add(self.Player)
        for x in range(3):
            self.Tree = tree.Trees()
            self.Enem = enemy.Enemies()
            variables.ALL_SPRITES.add(self.Enem)
            variables.ALL_SPRITES.add(self.Tree)
            variables.ENEMIES.add(self.Enem) 
            variables.TREES.add(self.Tree)

    def draw_text(self, surf, text, size, x, y, color = None):
        font = pygame.font.Font(variables.FONT_NAME, size)
        if color is not None:
            text_surface = font.render(text, True, color)
        else:
            text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect) 
    
    def show_menu(self):
        while variables.MENU:
            self.clock.tick(variables.FPS)
            self.background = pygame.image.load(path.join(variables.IMG_DIR, "background.png"))
            
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

    def run_game(self):
        while variables.RUNNING:
            if variables.RESTART:
                self.show_menu()
                variables.RESTART = False
                variables.ALL_SPRITES = pygame.sprite.Group()
                self.background = pygame.image.load(path.join(variables.IMG_DIR, "background.png"))
                variables.BULLETS = pygame.sprite.Group()
                variables.ENEMIES = pygame.sprite.Group()
                variables.TREES = pygame.sprite.Group()
                self.Player = player.Player()
                variables.SCORE = 0
                variables.ALL_SPRITES.add(self.Player)
                for x in range(3):
                    self.Tree = tree.Trees()
                    self.Enem = enemy.Enemies()
                    variables.ALL_SPRITES.add(self.Enem)
                    variables.ALL_SPRITES.add(self.Tree)
                    variables.ENEMIES.add(self.Enem) 
                    variables.TREES.add(self.Tree)            
                variables.SCORE = 0
            self.clock.tick(variables.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    variables.RUNNING = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(list(variables.BULLETS)) < 5:
                        self.Player.shoot()
                    if event.key == pygame.K_p:
                        variables.PAUSE = True
                        self.pause()   
                    if event.key == pygame.K_ESCAPE:
                        variables.RUNNING = False
                        variables.MENU = True                                   

            variables.ALL_SPRITES.update()


            collision_with_enemies = pygame.sprite.spritecollide(self.Player, variables.ENEMIES, True)
            if collision_with_enemies:
                self.Player.death()
                self.Enem = enemy.Enemies()
                variables.ALL_SPRITES.add(self.Enem)
                variables.ENEMIES.add(self.Enem) 

            hits = pygame.sprite.groupcollide(variables.ENEMIES, variables.BULLETS, True, True)
            for hit in hits:
                variables.SCORE += 1
                self.Enem = enemy.Enemies()
                variables.ALL_SPRITES.add(self.Enem)
                variables.ENEMIES.add(self.Enem)

            collision_with_trees = pygame.sprite.spritecollide(self.Player, variables.TREES, True)
            if collision_with_trees:
                self.Player.death()
                self.Tree = tree.Trees()
                variables.ALL_SPRITES.add(self.Tree)
                variables.TREES.add(self.Tree)
            
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