from constants import *
import pygame

class Main_entity(pygame.sprite.Sprite):

    """
        # TODO:

    """
    def __init__(self, x, y, width=BLOCK_SIZE, height=BLOCK_SIZE):
        super().__init__()
        self.width = width
        self.height = height

        # self.spritesheet = pygame.image.load(SPRITESHEET).convert()
        # self.y_sprite_sheet_index = y_sprite_sheet_index

        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))
        # self.image = self.get_image_from_sprite_sheet(0, self.y_sprite_sheet_index)
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x, y)

        # self.frame = 0
        # self.max_frame = (self.spritesheet.get_width() // BLOCK_SIZE) - 1
        # self.animation_speed = TICK_RATE / self.max_frame / 100
        #
        # self.coords = pygame.math.Vector2(self.rect.x, self.rect.y)



    def update(self):
        pass
