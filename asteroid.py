import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event



class Asteroid(CircleShape):
    def __init__(self, x, y ,radius):
        super().__init__(x, y, radius)
        self.asteroid_1_img = pygame.image.load("sprites/asteroid_1(48x48).png")
        self.asteroid_2_img = pygame.image.load("sprites/asteroid_2(32x32).png")
        self.rotation = 0
        self.rotation_speed = random.uniform(-20,20)

        #self.asteroid_scale_dict = {
        #    "small": (self.asteroid_2_img, ASTEROID_SMALL_SCALE),
        #    "medium": (self.asteroid_1_img, ASTEROID_MEDIUM_SCALE),
        #    "large": (self.asteroid_1_img, ASTEROID_LARGE_SCALE)
        #    }

    def draw(self, screen):
        
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

        cur_asteroid_img = self.asteroid_1_img
        if self.radius <= ASTEROID_MIN_RADIUS:
            cur_asteroid_img = pygame.transform.scale(self.asteroid_2_img, (64,64))
        elif self.radius >= ASTEROID_MAX_RADIUS:
            cur_asteroid_img = pygame.transform.scale(self.asteroid_1_img, (180,180))
        else:
            cur_asteroid_img = pygame.transform.scale(self.asteroid_1_img, (120,120))
        
        img = pygame.transform.rotate(cur_asteroid_img, self.rotation)
        asteroid_rect = img.get_rect(center =(self.position.x, self.position.y))
        screen.blit(img,(asteroid_rect))

       




    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt

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