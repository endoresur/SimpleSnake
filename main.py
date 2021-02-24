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
        self.player = sprites.Player()
        self.all_sprites.add(self.player)

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

                    if event.key == pygame.K_DOWN:
                        self.update_direction(options.Directions.DOWN)
                    elif event.key == pygame.K_UP:
                        self.update_direction(options.Directions.UP)
                    elif event.key == pygame.K_LEFT:
                        self.update_direction(options.Directions.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.update_direction(options.Directions.RIGHT)

            self.all_sprites.update()

            self.screen.fill(options.Colors.GRAY)
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

        pygame.quit()

    # TODO fix problem with wrong definition of direction
    def update_direction(self, direction):
        x, y = direction
        self.player.x += x
        self.player.y += y

        if self.player.x > options.Settings.WIDTH:
            self.player.x = 0
        elif self.player.x < 0:
            self.player.x = options.Settings.WIDTH
        elif self.player.y > options.Settings.HEIGHT:
            self.player.y = 0
        elif self.player.y < 0:
            self.player.y = options.Settings.HEIGHT

###

if __name__ == '__main__':
    game = MainGame()
    game.run()
