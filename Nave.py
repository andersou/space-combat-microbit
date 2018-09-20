import pygame
import random, pyganim

from Bala import Bala
from constants import *

naves = ["images/Ships/spaceShips_001.png",]
tempos = [100,]
frames_pyg = list(zip(naves,tempos))
print(frames_pyg)

class Nave(pygame.sprite.Sprite):
    def __init__(self,bala_render):
        super().__init__()
        self.bala_render = bala_render
        # nave = random.choice(naves)
        self.initAnim()

        self.image = self.anim.getCurrentFrame() #pygame.image.load(nave).convert_alpha()
        self.rect = self.anim.getRect()

        self.accel_x, self.accel_y = 0 , 0

        self.rect.center = random.randrange(0, LARGURA_TELA),random.randrange(0, ALTURA_TELA)

        self.angle = 90

    def initAnim(self):
        self.anim = pyganim.PygAnimation(frames_pyg)
        self.anim.scale((LARGURA_NAVE, int(
            LARGURA_NAVE / self.anim.getCurrentFrame().get_width() * self.anim.getCurrentFrame().get_height())))
        self.anim.makeTransformsPermanent()
        self.anim.play()

    def move_x(self, qtde):
        self.accel_x = qtde
    def move_y(self,qtde):
        self.accel_y = qtde
    def angulo(self,graus):

        if self.angle == graus:
            return
        centro = self.rect.center
        self.anim.clearTransforms()
        self.anim.rotate(90-graus)

        self.angle = graus
        self.rect = self.anim.getRect()
        self.rect.center = centro


    def do_move(self):
        if self.accel_x == 0 and self.accel_y == 0:
            return
        self.rect.move_ip(self.accel_x, self.accel_y)

    def update(self):
        self.image = self.anim.getCurrentFrame()  # pygame.image.load(nave).convert_alpha()

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