import main_entity
from constants import *
class Projectile(main_entity.Main_entity):
    def __init__(self, x, y):
        super().__init__(x, y, BLOCK_SIZE // 4, BLOCK_SIZE // 4)
        self.x = x
        self.y = y
        self.speed = 6

    def update(self):
        self.rect.left += self.speed
        if self.rect.left < 0 or self.rect.right > GAME_WIDTH:
            self.kill()
