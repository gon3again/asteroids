import pygame
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.spaceship_img = pygame.transform.flip(pygame.image.load("sprites/Spaceship#01(48x48).png"),False,True)
        self.rotation_img = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        #pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        img = pygame.transform.rotate(self.spaceship_img,self.rotation_img)
        spaceship_rect = img.get_rect(center =(self.position.x, self.position.y))
        screen.blit(img,(spaceship_rect))
        
        

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation_img -= PLAYER_TURN_SPEED * dt

        #self.scaled_spaceship_img = pygame.transform.rotate(self.scaled_spaceship_img, self.rotation)

        
    
    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def shoot(self, dt):
        if self.shot_timer > 0:
            return
        self.shot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot_vec = pygame.Vector2(0, 1)
        ##########################
        shot_vec = shot_vec.rotate(self.rotation)
        shot.velocity += PLAYER_SHOOT_SPEED * shot_vec