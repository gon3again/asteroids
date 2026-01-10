import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect


class Texter():
    def __init__(self,screen):
        
        self.font = pygame.font.SysFont(None,30,False,False,)
        self.screen = screen
    


    def draw_text(self, text,pos):
        img = self.font.render(text,True,"white")
        self.screen.blit(img ,pos)

