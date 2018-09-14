import pygame

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/naves/nave2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(100, int(100/self.image.get_width() * self.image.get_height())))
        self.rect = self.image.get_rect()
        self.mov_x, self.mov_y = 0,0
        self.pos_x, self.pos_y = 0,0
        self.angle = 90
    def move_x(self, qtde):
        self.mov_x = qtde
    def move_y(self,qtde):
        self.mov_y = qtde
    def angulo(self,graus):
        if self.angle == graus:
            return
        self.image = pygame.transform.rotate(self.image, graus - self.angle)
        #self.rect = self.image.get_rect()

        self.angle = graus


    def do_move(self):
        if self.mov_x == 0 and self.mov_y == 0:
            return
        self.rect.move_ip(self.mov_x, self.mov_y)
        self.mov_x = 0
        self.mov_y = 0
    def update(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.angulo(0)
            self.move_x(2)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.angulo(180)
            self.move_x(-2)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.angulo(90)
            self.move_y(-2)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.angulo(-90)
            self.move_y(2)

        self.do_move()