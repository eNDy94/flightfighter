import pygame
import player
import enemy
import variables
import tree


class GameManager():

    def __init__(self):
        pygame.init()
        self.background = pygame.image.load(variables.BACKGROUND_PATH)
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

    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font(variables.FONT_NAME, size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)    

    def run_game(self):
        while variables.RUNNING:
            self.clock.tick(variables.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    variables.RUNNING = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(list(variables.BULLETS)) < 5:
                        self.Player.shoot()

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
            

            self.screen.blit(self.background, (0, 0))
            variables.ALL_SPRITES.draw(self.screen)
            self.draw_text(self.screen, f"Score: {variables.SCORE}", 18, variables.WIDTH/2, 10)
            self.draw_text(self.screen, f"Health: {self.Player.Health + 1}", 18, 50, 10)
            pygame.display.flip()


if __name__ == "__main__":
    Game = GameManager()
    Game.run_game()
    pygame.quit()