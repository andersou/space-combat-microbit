import pygame
import random

from Bala import Bala
from constants import *

naves = ["images/Ships/spaceShips_001.png","images/Ships/spaceShips_002.png","images/Ships/spaceShips_003.png","images/Ships/spaceShips_004.png","images/Ships/spaceShips_005.png","images/Ships/spaceShips_006.png","images/Ships/spaceShips_007.png","images/Ships/spaceShips_008.png","images/Ships/spaceShips_009.png"]
class Nave(pygame.sprite.Sprite):
    def __init__(self,bala_render):
        super().__init__()
        self.bala_render = bala_render
        nave = random.choice(naves)
        self.image = pygame.image.load(nave).convert_alpha()
        self.original = self.image = pygame.transform.scale(self.image,(LARGURA_NAVE, int(LARGURA_NAVE/self.image.get_width() * self.image.get_height())))
        self.rect = self.image.get_rect()
        self.accel_x, self.accel_y = 0 , 0
        self.rect.center = random.randrange(0, LARGURA_TELA),random.randrange(0, ALTURA_TELA)
        self.angle = 90
    def move_x(self, qtde):
        self.accel_x = qtde
    def move_y(self,qtde):
        self.accel_y = qtde
    def angulo(self,graus):

        if self.angle == graus:
            return
        centro = self.rect.center
        self.image = pygame.transform.rotate(self.original, graus - 90)
        self.angle = graus
        self.rect = self.image.get_rect()
        self.rect.center = centro


    def do_move(self):
        if self.accel_x == 0 and self.accel_y == 0:
            return
        self.rect.move_ip(self.accel_x, self.accel_y)
        self.accel_x = 0
        self.accel_y = 0
    def update(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT] and teclas[pygame.K_UP] :
            self.angulo(45)
            self.move_x(VELOC_NAVE)
            self.move_y(-VELOC_NAVE)

        elif teclas[pygame.K_RIGHT] and teclas[pygame.K_DOWN] :
            self.angulo(-45)
            self.move_x(VELOC_NAVE)
            self.move_y(VELOC_NAVE)

        elif teclas[pygame.K_LEFT] and teclas[pygame.K_UP] :
            self.angulo(135)
            self.move_x(-VELOC_NAVE)
            self.move_y(-VELOC_NAVE)
        elif teclas[pygame.K_LEFT] and teclas[pygame.K_DOWN]:
            self.angulo(225)
            self.move_x(-VELOC_NAVE)
            self.move_y(VELOC_NAVE)

        elif teclas[pygame.K_RIGHT]:
            self.angulo(0)
            self.move_x(VELOC_NAVE)
        elif teclas[pygame.K_LEFT]:
            self.angulo(180)
            self.move_x(-VELOC_NAVE)
        elif teclas[pygame.K_UP]:
            self.angulo(90)
            self.move_y(-VELOC_NAVE)
        elif teclas[pygame.K_DOWN]:
            self.angulo(-90)
            self.move_y(VELOC_NAVE)
        self.do_move()

    def tiro(self):
        bala = Bala(self.angle,*self.rect.center,self)
        self.bala_render(bala)