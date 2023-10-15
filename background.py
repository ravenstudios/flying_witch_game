from constants import *
import pygame

class Background(pygame.sprite.Sprite):

    """
        # TODO:

    """
    def __init__(self, x):
        super().__init__()


        self.image = pygame.image.load("images/forest.jpeg").convert()
        self.image = pygame.transform.scale(self.image, (GAME_WIDTH, GAME_HEIGHT))

        self.image_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))

        self.image_surface.blit(self.image, (0, 0, GAME_WIDTH, GAME_HEIGHT))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x, 0)

        self.speed = -5

    def update(self):
        self.rect.left += self.speed
        if self.rect.right <= 0:
            self.rect.left = GAME_WIDTH
