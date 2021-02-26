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
        self.direction = options.Directions.RIGHT

        self.snake_segments = []
        self.snake_segments.append(sprites.Player())
        self.snake_segments.append(sprites.Player())
        self.snake_segments.append(sprites.Player())

        x, y = sprites.size
        i = self.snake_segments[0]
        for segment in self.snake_segments:
            segment.rect.x = i.rect.x - x
            i = segment

        self.all_sprites = pygame.sprite.Group()
        self.apple = sprites.Apple()
        self.all_sprites.add(self.apple)
        for element in self.snake_segments:
            self.all_sprites.add(element)

    def run(self):

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
            self.move(self.direction)
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

        pygame.quit()

    def update_direction(self, direction):

        if (direction == options.Directions.RIGHT and self.snake_segments[0].direction == options.Directions.LEFT or
                direction == options.Directions.LEFT and self.snake_segments[0].direction == options.Directions.RIGHT):
            return
        elif (direction == options.Directions.UP and self.snake_segments[0].direction == options.Directions.DOWN or
                direction == options.Directions.DOWN and self.snake_segments[0].direction == options.Directions.UP):
            return

        self.direction = direction

    def move(self, direction):

        for i in range(0, len(self.snake_segments)):
            self.snake_segments[i].direction = direction

