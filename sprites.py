import pygame
import options

colors = options.Colors()
settings = options.Settings()

# TODO custom size of player
size = (50, 50)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(colors.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2)

        self.x = 5
        self.y = 5

    # TODO understand with direction and speed
    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y
        if self.rect.left > settings.WIDTH:
            self.rect.right = 0

