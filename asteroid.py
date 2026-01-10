import pygame
import random
import time
from circleshape import CircleShape
from constants import *
from logger import log_event
from texter import Texter





class Asteroid(CircleShape):
    def __init__(self, x, y ,radius ,screen):
        super().__init__(x, y, radius)
        self.asteroid_1_img = pygame.image.load("sprites/asteroid_1(48x48).png")
        self.asteroid_2_img = pygame.image.load("sprites/asteroid_2(32x32).png")
        self.asteroid_1_img_hit = pygame.image.load("sprites/asteroid_1(48x48)_hit.png")
        self.asteroid_2_img_hit = pygame.image.load("sprites/asteroid_2(32x32)_hit.png")
        self.rotation = 0
        self.rotation_speed = random.uniform(-20,20)
        self.screen = screen
        self.hit_Text = Texter(self.screen)
        self.time_since_hit = float("inf")
        
        
        self.asteroid_stats = {
           "small": {"image":self.asteroid_2_img,"hitimage":self.asteroid_2_img_hit,"scale": (64,64),"hits":1},
           "medium": {"image":self.asteroid_1_img,"hitimage":self.asteroid_1_img_hit,"scale": (120,120),"hits":2},
           "large": {"image":self.asteroid_1_img,"hitimage":self.asteroid_1_img_hit,"scale": (180,180),"hits":3}
           }
        self.asteroid_size ,self.asteroid_score = self.check_asteroid_type()
        self.hits_taken = 0
        self.req_hits = self.asteroid_stats[self.asteroid_size]["hits"]
        #print(f"req hits: {self.req_hits}")

    def draw(self, screen):
        
        #pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    
        cur_stats = self.asteroid_stats[self.asteroid_size]
        cur_img = cur_stats["image"]
        if self.hit_recently():
            cur_img = cur_stats["hitimage"]
        
        cur_scale = cur_stats["scale"]
        self.req_hits = cur_stats["hits"]
        cur_scaled_asteroid_img = pygame.transform.scale(cur_img, cur_scale)

        
        img = pygame.transform.rotate(cur_scaled_asteroid_img, self.rotation)
        asteroid_rect = img.get_rect(center =(self.position.x, self.position.y))
        screen.blit(img,(asteroid_rect))
        self.hit_Text.draw_text(f"{self.hits_taken}",self.position,30,True)

       




    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt
        self.time_since_hit += dt
        if not self.hit_recently() and self.hits_taken >= self.req_hits:
            self.split()
        

    def take_hit(self):
        self.time_since_hit = 0
        self.hits_taken += 1
        score_to_add = 0

        if self.hits_taken >= self.req_hits:
            #self.split()
            score_to_add = self.asteroid_score
        return score_to_add
    
    def hit_recently(self):
        return self.time_since_hit < 0.03
        



    def split(self):
        self.kill()
        #player.score_change(self.asteroid_score)
        if self.asteroid_size == "small": 
            return self.asteroid_score
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        split_vector_1 = self.velocity.rotate(split_angle)
        split_vector_2 = self.velocity.rotate(-split_angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_1 = Asteroid(self.position.x, self.position.y, split_radius, self.screen)
        split_asteroid_1.velocity = split_vector_1 * 1.2
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, split_radius, self.screen)
        split_asteroid_2.velocity = split_vector_2 *1.2


    def check_asteroid_type(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            asteroid_size = "small"
            asteroid_score = 100
        elif self.radius >= ASTEROID_MAX_RADIUS:
            asteroid_size = "large"
            asteroid_score = 300
        else:
            asteroid_size = "medium"
            asteroid_score = 200
        return asteroid_size ,asteroid_score
        
        