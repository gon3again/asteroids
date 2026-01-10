import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect


class Texter():
    def __init__(self):

        self.font = pygame.font.SysFont(None,30,False,False,)

    def draw_text(self, text,pos,my_screen):
        img = self.font.render(text,True,"white")
        my_screen.blit(img ,pos)
