import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shots import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (bullets, updatable, drawable)

def main():
    pygame.init()
    fps_limiter = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable: #likewise for updateables
            obj.update(dt)
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
            if asteroid.collision(ship):
                return print("Game over!")
        screen.fill(BLACK)
        
        for obj in drawable: #draw everything in drawables group
            obj.draw(screen)
        print(f"Delta time: {round(dt, 3)} seconds")
        pygame.display.flip()
        delta = fps_limiter.tick(60)
        dt =  (delta / 1000)

if __name__ == "__main__":
    main()