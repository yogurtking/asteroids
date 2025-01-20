from circleshape import *
from constants import *

import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        

    def draw(self, screen):
        # pygame.draw.circle(surface, color, (x,y), radius, width)
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            first_angle = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
            second_angle = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            #spawn(self, radius, position, velocity):
            Asteroid(self.position.x, self.position.y, new_radius).velocity = first_angle
            Asteroid(self.position.x, self.position.y, new_radius).velocity = second_angle
            
            



        
