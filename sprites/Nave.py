import pygame
import random, pyganim

from microbit_helpers import Message
from sprites.Bala import Bala
from constants import *
from sprites.Username import Username

naves = ["images/Ships/spaceShips_001.png",]
tempos = [100,]
frames_pyg = list(zip(naves,tempos))
print(frames_pyg)




class Nave(pygame.sprite.Sprite):
    def __init__(self, bala_render, name_render, username):

        super().__init__()
       # self.screen_rect = screen_rect
        # renderizo o nome do usuario
        self.username = Username(name_render, username)
        #inicia pyganim (vou deixar impl pra se eu quiser animar dps)
        self.initAnim()

        # carrega atributos obrigatorios do sprite
        self.image = self.anim.getCurrentFrame() #pygame.image.load(nave).convert_alpha()
        self.rect = self.anim.getRect()

        #Começando parado
        self.accel_x, self.accel_y = 0 , 0

        #Posição inicial (aleatoria)
        self.rect.center = 50,50 #random.randrange(0, LARGURA_TELA),random.randrange(0, ALTURA_TELA)

        #Angulo inicial
        self.angle = 270

        # Renders para os filhos
        self.bala_render = bala_render


    def initAnim(self):
        self.anim = pyganim.PygAnimation(frames_pyg)
        self.anim.scale((LARGURA_NAVE, int(
            LARGURA_NAVE / self.anim.getCurrentFrame().get_width() * self.anim.getCurrentFrame().get_height())))
        self.anim.makeTransformsPermanent()
        self.anim.play()


    def angulo(self,graus):

        if self.angle == graus:
            return
        centro = self.rect.center
        self.anim.clearTransforms()
        self.anim.rotate(graus - 270)

        self.angle = graus
        self.rect = self.anim.getCurrentFrame().get_rect()
        self.rect.center = centro


    def do_move(self):
        if self.accel_x == 0 and self.accel_y == 0:
            return

        self.rect.move_ip(self.accel_x, self.accel_y)
    def update_username_pos(self):
        if self.angle >= 0 and self.angle <= 180:
            self.username.bot(self.rect.midbottom)
        else:
            self.username.top(self.rect.midtop)

    def update(self):
        self.image = self.anim.getCurrentFrame()  # pygame.image.load(nave).convert_alpha()


        self.testa_via_teclado()

        self.do_move()
        self.update_username_pos()

    def move_x(self, qtde):
        self.accel_x = qtde

    def move_y(self, qtde):
        self.accel_y = qtde

    def testa_via_teclado(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT] and teclas[pygame.K_UP]:
            self.angulo(45)
            self.move_x(VELOC_NAVE)
            self.move_y(-VELOC_NAVE)

        elif teclas[pygame.K_RIGHT] and teclas[pygame.K_DOWN]:
            self.angulo(-45)
            self.move_x(VELOC_NAVE)
            self.move_y(VELOC_NAVE)

        elif teclas[pygame.K_LEFT] and teclas[pygame.K_UP]:
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

    def tiro(self):
        bala = Bala(self.angle,*self.rect.center,self)
        self.bala_render.add(bala)

    def update_from_msg(self, msg: Message):
        self.angulo(msg.orientation)
        self.accel_x = msg.acc_x
        self.accel_y = msg.acc_y
        if(msg.a_press):
            self.tiro()


