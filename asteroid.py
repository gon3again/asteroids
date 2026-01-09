import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y ,radius):
        super().__init__(x, y, radius)

        

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        split_vector_1 = self.velocity.rotate(split_angle)
        split_vector_2 = self.velocity.rotate(-split_angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_1 = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid_1.velocity = split_vector_1 * 1.2
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid_2.velocity = split_vector_2 *1.2

      
