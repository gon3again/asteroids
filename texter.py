import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect


class Texter():
    def __init__(self,screen:pygame.Surface):
        
        # self.font = pygame.font.SysFont(None,30,False,False,)
        self.screen = screen
    


    def draw_text(self, text,pos,font_size:int, centered_anchor:bool):
        my_font = pygame.font.SysFont(None,font_size,False,False,)
        img = my_font.render(text,True,"white")

        if centered_anchor:
            text_rect = img.get_rect(center=pos)
            self.screen.blit(img ,text_rect)
            return
        self.screen.blit(img , pos)

