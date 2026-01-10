from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y ,radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt  
            

    def bullet_out_of_screen(self):
        x = self.position.x
        y = self.position.y
        if x < 0 or x > SCREEN_WIDTH or self.position.y < 0 or y > SCREEN_HEIGHT :
            self.kill()