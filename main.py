import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable, updatable)

    player = Player(
        SCREEN_WIDTH/2,
        SCREEN_HEIGHT/2,
        
    )

    asteroidfield = AsteroidField()
    

    

    print(updatable)

    print("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        dt = clock.tick(60)/1000
         
        for updated in updatable:
            updated.update(dt)
        

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                return
            for bullet in shots:
                if asteroid.collide(bullet):
                    bullet.kill()
                    asteroid.split()
            
            
                
        for drawn in drawable:
            drawn.draw(screen)
        
        
        pygame.display.flip()



if __name__ == "__main__":
    main()