from constants import *
from player import *
import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(
        SCREEN_WIDTH/2,
        SCREEN_HEIGHT/2,
        
    )
    

    

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
        for drawn in drawable:
            drawn.draw(screen)
        
        
        pygame.display.flip()



if __name__ == "__main__":
    main()