import pygame
import options

colors = options.Colors()
settings = options.Settings()
directions = options.Directions()

# TODO custom size of player
size = (40, 40)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(colors.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2)

        self.direction = directions.RIGHT
        self.x, self.y = self.direction

    def update(self):
        self.x, self.y = self.direction

        self.rect.x += self.x
        self.rect.y += self.y
        if self.rect.left > settings.WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = settings.WIDTH
        elif self.rect.bottom < 0:
            self.rect.top = settings.HEIGHT
        elif self.rect.top > settings.HEIGHT:
            self.rect.bottom = 0


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(colors.RED)
        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2)

        self.rect.x = 70
        self.rect.y = 90

    def update(self):
        pass
