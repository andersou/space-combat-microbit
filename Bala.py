import pygame

from constants import *
BALA_IMG = pygame.image.load("images/spaceMissiles_001.png").convert_alpha()
BALA = pygame.transform.scale(BALA_IMG, (
LARGURA_BALA, int(LARGURA_BALA / BALA_IMG.get_width() * BALA_IMG.get_height())))
ACCEL = {
    0: (VELOC_BALA, 0),
    45: (VELOC_BALA, -VELOC_BALA),
    90: (0, -VELOC_BALA),
    135: (-VELOC_BALA, -VELOC_BALA),
    180: (-VELOC_BALA, 0),
    225: (-VELOC_BALA, VELOC_BALA),
    -90: (0, VELOC_BALA),
    -45: (VELOC_BALA, VELOC_BALA)
}

class Bala(pygame.sprite.Sprite):
    def __init__(self,angle,x,y, nave):
        super().__init__()
        self.accel_x, self.accel_y = ACCEL[angle]
        self.angulo(angle,x,y)
        self.nave = nave

    def angulo(self, graus,x,y):
        self.image = pygame.transform.rotate(BALA.copy(), graus - 90)
        self.angle = graus
        self.rect = self.image.get_rect()
        self.rect.center = x,y

    def update(self):
        self.rect.move_ip(self.accel_x,self.accel_y)
