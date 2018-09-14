import sys, pygame
pygame.init()

size = width, height = 1366, 768
#, pygame.FULLSCREEN
screen = pygame.display.set_mode(size)

bg = pygame.image.load("images/space.png")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KE


    screen.blit(bg,(0,0))
    pygame.display.flip()
