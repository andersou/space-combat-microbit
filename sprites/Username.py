import pygame
font = pygame.font.Font(None, 18)
class Username(pygame.sprite.Sprite):
    def __init__(self, render, username):
        super().__init__()
        self.username = username
        self.image = font.render(username, True, (10, 10, 10), (200, 200, 200))
        self.rect = self.image.get_rect()
        render.add(self);
    def top(self, coord):

        self.rect.midbottom = (coord[0], coord[1]-10)

    def bot(self,coord):
        self.rect.midtop = (coord[0], coord[1]+10)