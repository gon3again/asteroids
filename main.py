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
player_is_alive = True
def main():
    pygame.init()
    global player_is_alive
    player_is_alive = True
    global player_score
    player_score = 0
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

    
    
    while player_is_alive:
        log_state()
        check_exit()
        print(asteroids)
        updatable.update(dt)
        for a in asteroids:
            if player.collides_with(a):
                log_event("player_hit")
                print("Game over!")
                player_is_alive = False
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
        score_text.draw_text(f"score: {player_score}",(4,4),30,False)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    
    while not player_is_alive:
        # for event in pygame.event.get():
        #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #         player_is_alive = True
        #         main()
        check_exit()

        
        # screen.fill("red")
        t = Texter(screen)
        t.draw_text("Game Over",(SCREEN_WIDTH/2,SCREEN_HEIGHT/2),100,True)
        pygame.display.flip()
    


def score_change(change,screen):
        global player_score
        player_score += change

def check_exit():
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            print("exit")
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or keys[pygame.K_r]:
            main()

    


if __name__ == "__main__":
    main()



