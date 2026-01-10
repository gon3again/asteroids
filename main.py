import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from shot import Shot
from texter import Texter


player_score = 0
def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    text_grp = pygame.sprite.Group()

    Shot.containers = (shots,updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField(screen)
    

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for t in text_grp:
            obj.update(False)

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
                    score_change(a.take_hit(),screen)
                if s.bullet_out_of_screen():
                    s.kill()

        screen.fill("black")
        
        
        bg = pygame.image.load("sprites/Bg_Star_1280_720.png")
        screen.blit(bg,(0,0))

        for obj in drawable:
            obj.draw(screen)
        

        score_text = Texter(screen)
        score_text.draw_text(f"score: {player_score}",(4,4))
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    


def score_change(change,screen):
        global player_score
        player_score += change


if __name__ == "__main__":
    main()



