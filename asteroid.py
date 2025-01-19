from circleshape import *
from constants import *

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