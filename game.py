import sys, pygame, queue
from constants import *
pygame.init()
#size = width, height = 1366, 768
size = width, height = LARGURA_TELA, ALTURA_TELA

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()
bg = pygame.image.load("images/space.png")

from Nave import Nave

balas_group = pygame.sprite.RenderPlain()
naves = [Nave(balas_group.add),Nave(balas_group.add),Nave(balas_group.add),Nave(balas_group.add),Nave(balas_group.add),Nave(balas_group.add)]

allsprites = pygame.sprite.RenderPlain(naves)


while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                for sp in allsprites.sprites():
                    sp.tiro()
    allsprites.update()
    balas_group.update()
    screen.blit(bg,(0,0))
    allsprites.draw(screen)
    balas_group.draw(screen)
    pygame.display.flip()

    colide = pygame.sprite.groupcollide(allsprites,balas_group,False,False)
    for nave,balas in colide.items():
        for bala in balas:
            if bala.nave != nave:
                allsprites.remove(nave)

