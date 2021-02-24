import pygame
import options
import sprites


class MainGame:

    def __init__(self, width=options.Settings.WIDTH, height=options.Settings.HEIGHT, fps=options.Settings.FPS):
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0

        self.all_sprites = pygame.sprite.Group()
        player = sprites.Player()
        self.all_sprites.add(player)

    def run(self):
        """
            The mainloop
        """
        running = True
        while running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.all_sprites.update()

            self.screen.fill(options.Colors.GRAY)
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

        pygame.quit()


###

if __name__ == '__main__':
    game = MainGame()
    game.run()
