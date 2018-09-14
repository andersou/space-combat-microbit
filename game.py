import sys, pygame
from Nave import Nave
pygame.init()

size = width, height = 1366, 768
#screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bg = pygame.image.load("images/space.png")
naves = (Nave())

allsprites = pygame.sprite.RenderPlain(naves)


while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    allsprites.update()

    screen.blit(bg,(0,0))
    allsprites.draw(screen)
    pygame.display.flip()
