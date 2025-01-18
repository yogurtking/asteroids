import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    fps_limiter = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        ship.update(dt)
        screen.fill(BLACK)
        ship.draw(screen)
        print(f"Delta time: {round(dt, 3)} seconds")
        pygame.display.flip()
        delta = fps_limiter.tick(60)
        dt =  (delta / 1000)

if __name__ == "__main__":
    main()