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
        self.apple = sprites.Apple()
        self.all_sprites.add(self.apple)
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

    def update_direction(self, direction):

        if (direction == options.Directions.RIGHT and self.player.direction == options.Directions.LEFT or
                direction == options.Directions.LEFT and self.player.direction == options.Directions.RIGHT):
            return
        elif (direction == options.Directions.UP and self.player.direction == options.Directions.DOWN or
                direction == options.Directions.DOWN and self.player.direction == options.Directions.UP):
            return

        self.player.direction = direction


###

if __name__ == '__main__':
    game = MainGame()
    game.run()
