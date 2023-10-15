import main_entity
import pygame
import projectile

class Witch(main_entity.Main_entity):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.speed = 3
        self.vert_speed = 0
        self.horz_speed = 0

    def update(self, projectile_group):
        self.rect.topleft = (self.x, self.y)

        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x += -self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP]:
            self.y += -self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        if keys[pygame.K_SPACE]:
            projectile_group.add(projectile.Projectile(self.rect.right, self.rect.bottom  - self.rect.height // 2))
