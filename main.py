import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from shot import Shot
from texter import UIElement



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    text = pygame.sprite.Group()

    Shot.containers = (shots,updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    UIElement.containers = (updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for a in asteroids:
            if player.collides_with(a):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()

        screen.fill("black")
        bg = pygame.image.load("sprites/Bg_Star_1280_720.png")
        screen.blit(bg,(0,0))

        for obj in drawable:
            obj.draw(screen)
        testtext()
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        

def testtext():
        BLUE = (106, 159, 181)
        WHITE = (255, 255, 255)
        uielement = UIElement(
            center_position=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),
            font_size=30,
            bg_rgb=BLUE,
            text_rgb=WHITE,
            text="Hello World",
            )



if __name__ == "__main__":
    main()
