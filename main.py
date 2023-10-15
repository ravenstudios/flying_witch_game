from constants import *
import pygame
import witch
import background



pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))



background1 = background.Background(0)
background2 = background.Background(GAME_WIDTH)


witch_group = pygame.sprite.Group()
background_group = pygame.sprite.Group()
projectile_group = pygame.sprite.Group()

witch = witch.Witch(100, 100)
witch_group.add(witch)

background_group.add(background1)
background_group.add(background2)





def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background
    background_group.draw(surface)
    witch_group.draw(surface)
    projectile_group.draw(surface)
    pygame.display.flip()



def update():
    witch_group.update(projectile_group)
    background_group.update()
    projectile_group.update()



if __name__ == "__main__":
    main()
