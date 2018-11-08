# -*- coding: utf-8 -*-

import sys, pygame
from constants import *
from microbit_helpers.Message import Message
from microbit_helpers.MicrobitComm import MicrobitComm
from queue import Queue
pygame.init()
import time
#
#   Configurações iniciais pygame
#
#size = width, height = 1366, 768
#size = width, height = LARGURA_TELA, ALTURA_TELA
screen = pygame.display.set_mode((0,0), pygame.DOUBLEBUF )#, pygame.FULLSCREEN)
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
bg = pygame.image.load("images/space.png")

#
#   Import de sprites
#
from sprites.Nave import Nave

#
#   Grupos de renderizacao
#
balas_render = pygame.sprite.RenderPlain()
naves_render = pygame.sprite.RenderPlain()
names_render = pygame.sprite.RenderPlain()

#
#  Teste
#

#naves_render.add(Nave(balas_render,names_render),Nave(balas_render,names_render),Nave(balas_render,names_render),Nave(balas_render,names_render),Nave(balas_render,names_render))
user_naves = {}
fila_msgs = Queue()

def new_message(msg):
    #print(msg.b_press)
    fila_msgs.put(msg)


mb_comm = MicrobitComm(new_message)

def remove_nave(nave):
    naves_render.remove(nave)
    names_render.remove(nave.username)
    user_naves.pop(nave.username.username)

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                for sp in naves_render.sprites():
                    sp.tiro()
    naves_render.update()
    balas_render.update()
    names_render.update()
    screen.blit(bg,(0,0))
    naves_render.draw(screen)
    balas_render.draw(screen)
    names_render.draw(screen)
    pygame.display.flip()

    colide = pygame.sprite.groupcollide(naves_render, balas_render, False, False)
    for nave,balas in colide.items():
        for bala in balas:
            if bala.nave != nave:
                remove_nave(nave)

    for bala in balas_render:
       if not bala.rect.colliderect(screen_rect):
           balas_render.remove(bala)

    now = time.time()
    for nave in naves_render:
        if now - nave.last > 3:
            remove_nave(nave)

    while not fila_msgs.empty():
        msg = fila_msgs.get()
        nave = user_naves.get(msg.user)
        if not nave:
            nave = Nave(balas_render, names_render, msg.user)
            naves_render.add(nave)
            user_naves[msg.user] = nave
        else:
            nave.update_from_msg(msg)

